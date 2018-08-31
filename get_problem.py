#!/usr/bin/python3
from urllib.request import urlopen
from sys import argv
from html.parser import HTMLParser

# This denotes the end of a test case, mandatory after every test case
BREAK = "END OF TESTCASE\n"

class problem_parser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.reading = False
		self.input = []
		self.output = []
		self.buffer = ""
		self.xr = 0
		
	def handle_starttag(self, tag, attrs):
		if tag == "pre":
			self.xr ^= 1
			self.reading = True
	
	def handle_endtag(self, tag):
		if tag == "pre":
			self.reading = False
			if self.xr == 1:
				self.input.append(self.buffer)
			else:
				self.output.append(self.buffer)
			self.buffer = ""
	
	def handle_data(self, data):
		if self.reading:
			self.buffer += data + '\n'
			

#This is contest no given in the url of the problem
problem_no = argv[1]  
#This is the problem no (A, B, C, D, E..)
problem_letter = argv[2]    


#This is the URL of the problem
url = 'https://codeforces.com/problemset/problem/' + problem_no + '/' + problem_letter
problem = urlopen(url)
flag = 0
if problem.geturl() != url:
	flag = 1
	print("URL RELATED ERROR\n")
else:
	print("Fetching Problem", problem_no, problem_letter)
	text = problem.read()
	parser = problem_parser()
	parser.feed(text.decode('utf-8'))
	if len(parser.input) != len(parser.output):
		flag = 1
		print("Error in Parsing the problem")
	else:
		inp = open('prac.txt', 'w')
		inp.write(str(len(parser.input)) + '\n')
		for test_case in parser.input:
			inp.write(test_case)
			inp.write(BREAK)
		inp.close()
		out = open('prac.out', 'w')
		out.write(str(len(parser.output)) + '\n')
		for test_case in parser.output:
			out.write(test_case)
			out.write(BREAK)
		out.close()
if flag == 0:
	print("Fetch successful")
else:
	print("Fetch unsuccessful")
