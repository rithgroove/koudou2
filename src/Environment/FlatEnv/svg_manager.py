import xml.etree.ElementTree as ET

NAMESPACE_SVG = "http://www.w3.org/2000/svg"
NAMESPACE_INKSCAPE = "http://www.inkscape.org/namespaces/inkscape"

def get_key(namespace,key):
	"""
	[Function] get_key
	Helper function to create key 
	
	Parameters:
		- file : filename.

	Returns: [List of Dictionary] data
	"""
	dict_key = "{"
	if (namespace.lower() == "svg"):
		dict_key += NAMESPACE_SVG
	elif (namespace.lower == "ink" or namespace.lower == "inkscape"):
		dict_key += NAMESPACE_INKSCAPE
	else:
		dict_key += namespace
	dict_key += "}"
	dict_key += key
	return dict_key

def read_svg(filepath):
	tree = ET.parse(filepath)
	root = tree.getroot()
	root_info = read_root_info(root)
	read_environment(root)

def read_root_info(root):
	svg_attribute = {}
	for x in root.attrib:
		svg_attribute[x] = root.attrib[x]
	return svg_attribute

def read_environment(root):

	root_svg = root.findall(get_key("svg","g"))
	print(root_svg)
	for x in root_svg:
		print(x.attrib)



# print(root)
# print("\n")
# print(root.tag)
# print("\n")
# print(root.attrib)
# print("\n")

# #print(root[0])


# for child in root:
# 	print("\n")
# 	print(child.tag, child.attrib)
# 	print("\n")
