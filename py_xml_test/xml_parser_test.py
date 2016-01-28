# coding=utf-8

from py_xml import xml_parser
import unittest

class XmlParserTest(unittest.TestCase):
    
    def test_parse(self):
        parser = xml_parser.XmlParser()
        result = parser.parse('test.xml')
        print result