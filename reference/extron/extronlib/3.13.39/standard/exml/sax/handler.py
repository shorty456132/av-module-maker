"""Extron wrapper of xml.sax.handler."""

__all__ = [
    'ContentHandler',
    'DTDHandler',
    'EntityResolver',
    'ErrorHandler',
    'LexicalHandler',
    'all_features',
    'all_properties',
    'feature_external_ges',
    'feature_external_pes',
    'feature_namespace_prefixes',
    'feature_namespaces',
    'feature_string_interning',
    'feature_validation',
    'property_declaration_handler',
    'property_dom_node',
    'property_encoding',
    'property_interning_dict',
    'property_lexical_handler',
    'property_xml_string',
    'version'
]

from xml.sax.handler import (ContentHandler, DTDHandler, EntityResolver,
                             ErrorHandler, all_features, all_properties,
                             feature_external_ges, feature_external_pes,
                             feature_namespace_prefixes, feature_namespaces,
                             feature_string_interning, feature_validation,
                             property_declaration_handler, property_dom_node,
                             property_encoding, property_interning_dict,
                             property_lexical_handler, property_xml_string,
                             version)


class LexicalHandler:
    """Optional SAX2 handler for lexical events.

    This handler is used to obtain lexical information about an XML
    document, that is, information about how the document was encoded
    (as opposed to what it contains, which is reported to the
    ContentHandler), such as comments and CDATA marked section
    boundaries.

    To set the LexicalHandler of an XMLReader, use the setProperty
    method with the property identifier
    '`<http://xml.org/sax/properties/lexical-handler>`_'.
    """

    def comment(self, content):
        """Reports a comment anywhere in the document (including the DTD
        and outside the document element).

        content is a string that holds the contents of the comment.
        """
        pass

    def endCDATA(self):
        """Reports the end of a CDATA marked section."""
        pass

    def endDTD(self):
        """Signals the end of DTD declarations."""
        pass

    def startCDATA(self):
        """Reports the beginning of a CDATA marked section.

        The contents of the CDATA marked section will be reported
        through the characters event.
        """
        pass

    def startDTD(self, name, public_id, system_id):
        """Report the start of the DTD declarations, if the document has an
        associated DTD.

        A startEntity event will be reported before declaration events
        from the external DTD subset are reported, and this can be used
        to infer from which subset DTD declarations derive.

        name is the name of the document element type, public_id the
        public identifier of the DTD (or None if none were supplied) and
        system_id the system identfier of the external subset (or None
        if none were supplied).
        """
        pass
