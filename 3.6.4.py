from xml.etree import ElementTree

tree = ElementTree.ElementTree(ElementTree.fromstring(input()))
root = tree.getroot()
colors = {"red": 0, "green": 0, "blue": 0}
def poisk(vetka, depth=1):
    colors[vetka.attrib["color"]] += depth
    for elem in vetka:
        poisk(elem, depth + 1)
poisk(root)
print(colors["red"], colors["green"], colors["blue"])
