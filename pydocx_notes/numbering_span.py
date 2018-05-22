# coding: utf-8
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from pydocx.export import numbering_span


class NumberingSpanBuilder(numbering_span.NumberingSpanBuilder):
    def get_left_position_for_paragraph(self, paragraph):
        if paragraph is None:
            return 0
        return super(NumberingSpanBuilder, self).get_left_position_for_paragraph(paragraph)
