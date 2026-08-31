"""Extron wrapper of xml.dom.pulldom"""

__all__ = [
    'CHARACTERS',
    'COMMENT',
    'END_DOCUMENT',
    'END_ELEMENT',
    'IGNORABLE_WHITESPACE',
    'PROCESSING_INSTRUCTION',
    'SAX2DOM',
    'START_DOCUMENT',
    'START_ELEMENT',
    'DOMEventStream',
    'PullDOM',
    'default_bufsize',
    'parse',
    'parseString'
]

from xml.dom.pulldom import (CHARACTERS, COMMENT, END_DOCUMENT, END_ELEMENT,
                             IGNORABLE_WHITESPACE, PROCESSING_INSTRUCTION,
                             SAX2DOM, START_DOCUMENT, START_ELEMENT,
                             DOMEventStream, PullDOM, default_bufsize, parse,
                             parseString)
