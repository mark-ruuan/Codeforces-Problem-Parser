#!/usr/bin/python3
from sys import argv
from subprocess import run, PIPE
from time import time

# This denotes the end of a test case, mandatory after every test case
BREAK = "END OF TESTCASE\n"

check = len(argv) > 1 and int(argv[1])
inp = open('prac.txt', 'r')
out = open('prac.out','r')
num_cases = int(inp.readline())
if int(out.readline()) != num_cases and check:
	print("Error: Number of Testcases in input and output file are different")
	exit()
for i in range(1, num_cases + 1):
	case_input = ""
	line = inp.readline()
	while line != BREAK:
		case_input += line
		line = inp.readline()
	start_time = time()

#runs ./a.out in ubuntu can be changed to a.exe
	output = run(["./a.out"],
		input=case_input.encode('utf-8'),stdout=PIPE).stdout.decode('utf-8')
	time_taken = time() - start_time
	if check:
		case_output = ""
		line = out.readline()
		while line != BREAK:
			case_output += line
			line = out.readline()
		print("Case #{}:{}".format(i, case_output == output))
		print("Time Taken: {}".format(time_taken))
		if case_output != output:
			print("Input:")
			print(case_input, end = '')
			print("Your output:")
			print(output, end ='')
			print("Correct output:")
			print(case_output, end = '')
	else:
		print("Case #{}:".format(i))
		print(output, end = '')
		print("Time Taken: {}".format(time_taken))
	print()
inp.close()
out.close()
