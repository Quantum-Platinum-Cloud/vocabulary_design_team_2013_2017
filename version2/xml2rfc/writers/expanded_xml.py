# --------------------------------------------------
# Copyright The IETF Trust 2011, All Rights Reserved
# --------------------------------------------------

import lxml.etree
import xml2rfc


class ExpandedXmlWriter:
    """ Writes a duplicate XML file but with all references expanded """
    
    # Note -- we don't need to subclass BaseRfcWriter because the behavior
    # is so different and so trivial
    
    def __init__(self, xmlrfc, quiet=False, verbose=False):
        self.root = xmlrfc.getroot()
        self.quiet = quiet
        self.verbose = verbose
    
    def write(self, filename):
        # Use lxml's built-in serialization
        file = open(filename, 'w')
        file.write(lxml.etree.tostring(self.root, pretty_print=True))

        if not self.quiet:
            xml2rfc.log.write('Created file', filename)
