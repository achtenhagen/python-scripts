
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

# convert list to dictionary
def to_dict(l):
	keys = ['rank', 'title', 'volume', 'price', 'diff', 'perc_diff']
	d = []
	d.append(dict(zip(keys, l)))
	return d

def get_elms_for_atr_val(tag, atr, val):
	lst=[]
	elms = dom.getElementsByTagName(tag)
	for node in elms:
		for attrName, attrValue in node.attributes.items():
			if attrName == atr and attrValue == val:
				lst = list(filter(lambda x: x.nodeType == 1, node.childNodes))				
	return lst

# get all text recursively to the bottom
def get_text(e):
	lst = []
	if e.nodeType in (3,4):
		if e.data != ' ':
			return [e.data]
	else:
		for child in e.childNodes:
			lst = lst + get_text(child)
	return lst

def extract_values(dm):
	lst = []
	temp = []
	l = get_elms_for_atr_val('table', 'class', 'mdcTable') # list or trs
	l.pop(0)
	for tr in l:
		tds = list(filter(lambda x: x.nodeType == 1, tr.childNodes))
		for td in tds:
			item = get_text(td)
			temp.append(item[0].replace('\n', ''))
		lst.append(to_dict(temp))
		temp = []
	return lst
	
# mysql> describe most_active;
def insert_to_db(l, tbl):
	db = MySQLdb.connect(host="localhost", user="root", passwd="", db="stocks")
	c = db.cursor()
	c.execute("""CREATE TABLE IF NOT EXISTS `%s` (
	`rank` VARCHAR(50),
	`title` VARCHAR(255),
	`volume` VARCHAR(50),
	`price` VARCHAR(50),
	`diff`VARCHAR(50),
	`perc_diff` VARCHAR(50)
	)""" % (tbl))
	
	for d in l:
		query = """INSERT INTO `%s` (rank, title, volume, price, diff, perc_diff) VALUES ("%s", "%s", "%s", "%s", "%s", "%s");""" % (tbl, d['rank'], d['title'], d['volume'], d['price'], d['diff'], d['perc_diff'])
		print query
		c.execute(query)
		db.commit()
	c.close()
	db.close()
	return

# convert to xhtml
def html_to_xml(fn):
	xhtml_file = fn + ".xhtml"
	# os.system("tidy -asxhtml -numeric -quiet -o %s %s.html" % (xhtml_file, fn))
	return xhtml_file

def main():
	html_fn = sys.argv[1]
	fn = html_fn.replace('.html', '')
	xhtml_fn = html_to_xml(fn)
	
	global dom
	dom = parse(xhtml_fn)
	lst = extract_values(dom)

	# make sure your mysql server is up and running
	for stock in lst:
		cursor = insert_to_db(stock, fn)

	# l = select_from_db(cursor,fn) # display the table on the screen

	# make sure the Apache web server is up and running
	# write a PHP script to display the table(s) on your browser

	return True

if __name__ == "__main__":
	 main()
	