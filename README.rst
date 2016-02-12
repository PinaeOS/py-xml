py-xml
============================================

XML bindng library for Python

Installation
--------------

The lastest stable is py-xml-1.0.tar.gz

.. code-block:: shell

    python setup.py install

.. code-block:: shell

    pip install py-xml

    
Getting Start
--------------

xml data(test.xml):

.. code-block:: xml

	<root>
		<group name="test">
			<family>green</family>
		</group>
		<parent name="green">
			<child name="jim" age="23" sex="male">
				<address>Shenzhen</address>
				<phone>18607578001</phone>
			</child>
			<child name="lucy" age="21" sex="female" address="Chongqing">
				<address>Guangzhou</address>
				<phone>18607578002</phone>
			</child>
		</parent>
	</root>


demo for py-xml:

.. code-block:: python

	import py_xml
	    
	bind_obj = py_xml.parse('test.xml')
	print bind_obj.get('root').get('parent')[0].get('child')[0].get('name').get('_attr_') #print: jim
	print bind_obj.get('root').get('parent')[0].get('child')[0].get('address').get('_node_') #print: Shenzhen
	    
	print py_xml.to_xml(bind_obj) #print above xml

Documentation
--------------

Full documentation is hosted on [HERE](). 
Sources are available in the ``docs/`` directory.

License
--------------

py-xml is licensed under the Apache License, Version 2.0. See LICENSE for full license text