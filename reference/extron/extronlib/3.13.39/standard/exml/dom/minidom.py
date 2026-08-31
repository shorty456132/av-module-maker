"""Extron wrapper of xml.dom.minidom"""

__all__ = [
    'Attr',
    'CDATASection',
    'Document',
    'DocumentType',
    'Element',
    'NamedNodeMap',
    'Node',
    'NodeList',
    'ProcessingInstruction',
    'Text',
    'parse',
    'parseString'
]

from xml.dom.minidom import (Attr, CDATASection, Document, DocumentType,
                             Element, NamedNodeMap, Node,
                             ProcessingInstruction, Text, parse, parseString)

class NodeList(list):
    
    @property
    def length(self):
        """The number of nodes in the NodeList."""
        pass
