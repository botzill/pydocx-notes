# coding: utf-8
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
)

from pydocx import export
from pydocx_notes.mixin import PyDocXHTMLExporterNotesMixin


class PyDocXHTMLExporter(PyDocXHTMLExporterNotesMixin, export.PyDocXHTMLExporter):
    pass


class PyDocX(object):
    @staticmethod
    def to_html(path_or_stream):
        return PyDocXHTMLExporter(path_or_stream).export()

    @staticmethod
    def to_markdown(path_or_stream):
        return export.PyDocXMarkdownExporter(path_or_stream).export()
