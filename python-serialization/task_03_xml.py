"""
File that contains xml serialization and deserialization
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Function that serialize a dictionary to an xml"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        ET.SubElement(root, key).text = str(value)

    # write in a file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Function to deserialize from an xml file"""
    tree = ET.parse(filename)
    root = tree.getroot()
    res = {}
    for child in root:
        res[child.tag] = child.text

    return res
