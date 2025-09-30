"""
File that contains xml serialization and deserialization
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Function that serialize a dictionary to an xml"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        ET.SubElement(root, key).text = value

    # write in a file
    tree = ET.ElementTree(root)
    tree.write(filename)
