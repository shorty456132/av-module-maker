"""Extron wrapper of xml.etree.ElementTree."""

__all__ = [
    "Comment",
    "dump",
    "Element",
    "ElementTree",
    "fromstring",
    "fromstringlist",
    "iselement",
    "iterparse",
    "parse",
    "ParseError",
    "PI",
    "ProcessingInstruction",
    "QName",
    "SubElement",
    "tostring",
    "tostringlist",
    "TreeBuilder",
    "VERSION",
    "XML",
    "XMLID",
    "XMLParser",
    "register_namespace",
]

from xml.etree.ElementTree import (PI, VERSION, XML, XMLID, Comment, Element,
                                   ElementTree, ParseError,
                                   ProcessingInstruction, QName, SubElement,
                                   TreeBuilder, XMLParser, dump, fromstring,
                                   fromstringlist, iselement, iterparse, parse,
                                   register_namespace, tostring, tostringlist)



class ParseError(ParseError):
   
    @property
    def end_lineno(self):
        """exception end lineno"""
        pass

    @property
    def end_offset(self):
        """exception end offset"""
        pass