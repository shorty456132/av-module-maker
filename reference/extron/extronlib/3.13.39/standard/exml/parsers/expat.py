"""Extron wrapper of xml.parsers.expat."""

__all__ = [
    'EXPAT_VERSION',
    'XML_PARAM_ENTITY_PARSING_ALWAYS',
    'XML_PARAM_ENTITY_PARSING_NEVER',
    'XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE',
    'ErrorString',
    'ExpatError',
    'ParserCreate',
    'XMLParserType',
    'error',
    'errors',
    'features',
    'model',
    'native_encoding',
    'version_info'
]

from pyexpat import (EXPAT_VERSION, XML_PARAM_ENTITY_PARSING_ALWAYS,
                     XML_PARAM_ENTITY_PARSING_NEVER,
                     XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE, ErrorString,
                     ExpatError, ParserCreate, XMLParserType, error, errors,
                     features, model, native_encoding, version_info)
