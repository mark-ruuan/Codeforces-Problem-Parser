CODEFORCES PROBLEM PARSER

This repo contains two scripts(get_problem.py & run.py) which are complemenatry to each other. "get_problem.py" fetches the sample test of the problem and puts them into two separate input and output text files. "run.py" run yours executable code on all the sample testcases and consists of provision to check whether your output is correct or not.


USAGE

To get the sample test cases of the problem you need to know the problem no(generally the contest no), which is given in the problemset(can also be found in the url), for example if the problem no is 255 A then run the command:
	
	./get_problem.py 255 A

and the test cases will be download in the current directory in the file "prac.txt"(sample input) and "prac.out"(output).

After compiling your code and executable file "./a.out" should be generated. After that run the following command:
	
	./run.py

if u want to check the answers then run the following command:
	
	./run.py 1
	
If you want to add more custom testcases, just the no of testcases at the top of the file in "prac.txt" and enter the new testcase with correct BREAK statement at end of every new test(BREAK can be found at the top in both the script) and do the same in "prac.out".

