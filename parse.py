
import libxml2
import sys
import os
import commands
import re
import sys
import MySQLdb
from xml.dom.minidom import parse, parseString

# for converting dict to xml
from cStringIO import StringIO
from xml.parsers import expat
from bs4 import BeautifulSoup

def get_elms_for_atr_val(tag, atr, val):
	lst=[]
	elms = dom.getElementsByTagName(tag)

	return lst

# get all text recursively to the bottom
def get_text(e):
	lst=[]
	# base case: node type 3 | 4
	if e.nodeType in (3,4)
		# get data
		lst.append(e.data)
	else:
		# loop thru child nodes
		# for each child in e.childNodes ...
	return lst
	
# replace whitespace chars
def replace_white_space(str):
	p = re.compile(r'\s+')
	new = p.sub(' ', str) # a lot of \n\t\t\t\t\t\t
	return new.strip()

# replace but these chars including ':'
def replace_non_alpha_numeric(s):
	p = re.compile(r'[^a-zA-Z0-9:-]+')
	#   p = re.compile(r'\W+') # replace whitespace chars
	new = p.sub(' ', s)
	return new.strip()

def extract_values(dm):
	lst = []
	l = get_elms_for_atr_val('table', 'class','most_actives')
	# ............
	#    get_text(e)
	# ............
	return lst
	
# mysql> describe most_active;
def insert_to_db(l,tbl):
	# ............
	return

# convert to xhtml
def html_to_xml(fn):
	# return xhtml_file
	xhtml_file = fn + ".xhtml"
	cmd = "tidy -asxhtml -numeric -quiet -e -o " + xhtml_file + " " + fn + ".html"
	os.system(cmd)
	return xhtml_file

def main():
	html_fn = sys.argv[1]
	fn = html_fn.replace('.html', '')
	xhtml_fn = html_to_xml(fn)
	
	global dom
	dom = parse(xhtml_fn)
	
	# print dom.getElementsByTagName('tr')

	# lst = extract_values(dom)

	# make sure your mysql server is up and running
	# cursor = insert_to_db(lst,fn) # fn = table name for mysql

	# l = select_from_db(cursor,fn) # display the table on the screen

	# make sure the Apache web server is up and running
	# write a PHP script to display the table(s) on your browser

	# return xml

if __name__ == "__main__":
	 main()
	