#coding=utf-8

import types
import xml.dom.minidom

class XmlBuilder():
    def __init__(self):
        pass
    
    def to_xml(self, node):
        if node == None or type(node) != types.DictionaryType:
            return None
        
        impl = xml.dom.minidom.getDOMImplementation()
        
        root_node_key = None
        for _node_key in node.keys():
            if _node_key != '':
                root_node_key = _node_key
                break
        
        if root_node_key != None:
            dom = impl.createDocument(None, root_node_key, None)
            root = dom.documentElement
        
            self.__fetch_element(dom, root, node.get(root_node_key))
            self.__indent(dom, dom.documentElement)
            return root.toxml()
        else:
            return None
        
    def write_xml(self, node, filename):
        xml_str = self.to_xml(node)
        
        xml_file = open(filename, 'w')
        try:
            xml_file.write(xml_str)
        finally:
            xml_file.close( )
            
    def __fetch_element(self, dom, pelement, node):
        if node != None:
            for node_name in node.keys():
                node_value = node.get(node_name)
                if type(node_value) == types.DictionaryType:
                    self.__create_element(dom, pelement, node_name, node_value)
                elif type(node_value) == types.ListType:
                    for node_item in node_value:
                        self.__create_element(dom, pelement, node_name, node_item)
    
    def __create_element(self, dom, pelement, node_name, node_value):
        if node_value.has_key('_attr_'):
            pelement.setAttribute(node_name, node_value.get('_attr_'))
        elif node_value.has_key('_node_') or node_value.has_key('_cdata_'):
            element = dom.createElement(node_name)
            if node_value.has_key('_node_'):
                text = dom.createTextNode(node_value.get('_node_'))
            else:
                text = dom.createCDATASection(node_value.get('_node_'))
            element.appendChild(text)
            pelement.appendChild(element)
        else:
            element = dom.createElement(node_name)
            self.__fetch_element(dom, element, node_value)
            pelement.appendChild(element)
            
    def __indent(self, dom, node, indent_deep = 0):
        # Copy child list because it will change soon
        children = node.childNodes[:]
        # Main node doesn't need to be indent_deeped
        if indent_deep:
            text = dom.createTextNode('\n' + '\t' * indent_deep)
            node.parentNode.insertBefore(text, node)
        if children:
            # Append newline after last child, except for text nodes
            if children[-1].nodeType == node.ELEMENT_NODE:
                text = dom.createTextNode('\n' + '\t' * indent_deep)
                node.appendChild(text)
                # indent_deep children which are elements
            for n in children:
                if n.nodeType == node.ELEMENT_NODE:
                    self.__indent(dom, n, indent_deep + 1)
        