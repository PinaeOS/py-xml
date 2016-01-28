# coding=utf-8

import py_xml
    
bind_obj = py_xml.parse('test.xml')
print bind_obj.get('root').get('parent')[0].get('child')[0].get('name').get('_attr_') #print: jim
print bind_obj.get('root').get('parent')[0].get('child')[0].get('address').get('_node_') #print: Shenzhen
    
print py_xml.to_xml(bind_obj) #print above xml
