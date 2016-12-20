# bookstore.py
# Created by Maurice Achtenhagen on 12/18/16.

import re
from xml.dom.minidom import parse, parseString

def process_dom_tree(dm):
	lst = []
	elms = dm.getElementsByTagName('book')
	for elm in elms:
		l = get_text(elm)
		lst.append(l)
	return lst

def get_text(elm):
	lst = []
	if elm.nodeType in (3,4):
		if not elm.data.isspace():
			lst.append(elm.data)
	else:
		for child in elm.childNodes:
			lst = lst + get_text(child)
	return lst
	
# Retrieve all the text strings for the books published before 1990.
def get_old_books():
	return list(filter(lambda x: int(x[2]) < 1990, process_dom_tree(dom)))

def main():
	lst = []
	global dom
	dom = parse('bookstore.xml')
	lst = process_dom_tree(dom)
	print(lst)
	print("\nBooks published before 1990:")
	print(get_old_books())
	return lst

if __name__ == "__main__":
	main()