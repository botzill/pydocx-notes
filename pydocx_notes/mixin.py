# coding: utf-8
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
)

from pydocx.export.html import HtmlTag
from pydocx.export.numbering_span import NumberingItem
from pydocx.openxml import wordprocessing
from pydocx.util.memoize import memoized


class PyDocXHTMLExporterNotesMixin(object):
    # Set here types of notes that we want to export
    NOTES_TYPES = ['note', 'warning', 'caution', 'sample']

    # Tag used to wrap notes
    NOTES_WRAPPER_TAG_NAME = 'div'

    # Remove <p> tag from list items
    REMOVE_P_TAG_FROM_LISTS = True

    def __init__(self, *args, **kwargs):
        super(PyDocXHTMLExporterNotesMixin, self).__init__(*args, **kwargs)
        self.node_type_to_export_func_map[wordprocessing.Bookmark] = self.export_bookmark

    @memoized
    def get_bookmark_name(self, bookmark):
        name = bookmark.name
        if name:
            # The _Goback bookmark enables to go to the previous edit functionality
            # (ShiftF5) across sessions. It is a hidden bookmark so we skip it
            if name.lower() in ('_goback',):
                return None
        return name

    def export_bookmark(self, bookmark):
        # Check if this method is implement in parent classes
        results = getattr(super, 'export_bookmark', None)

        attrs = {}

        bookmark_name = self.get_bookmark_name(bookmark)

        if bookmark_name:
            attrs['id'] = bookmark_name

            tag = HtmlTag('a', **attrs)

            return tag.apply(results, allow_empty=True)

    def export_textbox_content(self, textbox_content):
        """Override this method so that we export in textbox lists"""

        numbering_spans = self.yield_numbering_spans(textbox_content.children)
        return self.yield_nested(numbering_spans, self.export_node)

    def get_textbox_note_type(self, textbox):
        """Get the textbox type based on the string of the first paragraph."""

        try:
            note_type = textbox.children[0].children[0].get_text().strip(':').strip().lower()

            if note_type in self.NOTES_TYPES:
                return note_type
        except Exception:
            pass

        return None

    def get_textbox_attributes(self, textbox):
        """Here we create the textbox attributes. Especially we create the class name for the
        note type for the textbox"""

        attrs = {}
        note_type = self.get_textbox_note_type(textbox)

        if note_type:
            attrs['class'] = '{note_type}-box'.format(note_type=note_type)

        return attrs

    def export_textbox(self, textbox):
        results = super(PyDocXHTMLExporterNotesMixin, self).export_textbox(textbox)

        tag = HtmlTag(self.NOTES_WRAPPER_TAG_NAME, **self.get_textbox_attributes(textbox))

        return tag.apply(results)

    def get_paragraph_tag(self, paragraph):
        """Override this method so that we remove the <p> tag from the lists items"""

        if self.REMOVE_P_TAG_FROM_LISTS:
            if isinstance(paragraph.parent, NumberingItem):
                return

        return super(PyDocXHTMLExporterNotesMixin, self).get_paragraph_tag(paragraph)
