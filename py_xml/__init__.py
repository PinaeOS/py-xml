# coding=utf-8

__version__ = '1.0'

from py_xml import xml_parser
from py_xml import xml_builder

def parse(filename):
    return xml_parser.XmlParser().parse(filename)

def parse_string(xml_str):
    return xml_parser.XmlParser().parse_string(xml_str)

def to_xml(node):
    return xml_builder.XmlBuilder().to_xml(node)

def write_xml(node, filename):
    return xml_builder.XmlBuilder().write_xml(node)