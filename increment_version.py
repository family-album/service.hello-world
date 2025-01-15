import xml.etree.ElementTree as ET

def increment_version(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    version = root.attrib['version']
    major, minor, patch = map(int, version.split('.'))
    patch += 1
    new_version = f"{major}.{minor}.{patch}"
    root.attrib['version'] = new_version
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    increment_version('addon.xml')
