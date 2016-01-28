# coding=utf-8

import unittest

from py_xml import xml_parser
from py_xml import xml_builder

class XmlBuilderTest(unittest.TestCase):
    
    def test_to_xml(self):
        parser = xml_parser.XmlParser()
        result = parser.parse('test.xml')
        builder = xml_builder.XmlBuilder()
        print builder.to_xml(result)