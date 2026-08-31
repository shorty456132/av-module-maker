"""Extron wrapper of xml.sax.saxutils."""

__all__ = [
    'escape',
    'unescape',
    'quoteattr',
    'XMLGenerator',
    'XMLFilterBase',
    'prepare_input_source'
    ]

from xml.sax.saxutils import (XMLFilterBase, XMLGenerator, escape,
                              prepare_input_source, quoteattr, unescape)
