
#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
	# ----
	# read
	# ----

	def test_read_1(self):
		s = "1 10\n"
		i, j = collatz_read(s)
		self.assertEqual(i,  1)
		self.assertEqual(j, 10)

	def test_read_2(self):
		s = "2 30\n"
		i, j = collatz_read(s)
		self.assertEqual(i, 2)
		self.assertEqual(j, 30)

	def test_read_3(self):
		s = "5 100\n"
		i, j = collatz_read(s)
		self.assertEqual(i, 5)
		self.assertEqual(j, 100)

	def test_read_4(self):
		s = "40 20\n"
		i, j = collatz_read(s)
		self.assertEqual(i, 40)
		self.assertEqual(j, 20)

	def test_read_5(self):
		s = "\n"
		i,j = collatz_read(s)
		self.assertEqual(i,0)
		self.assertEqual(j,0)


		# ----
		# eval
		# ----

	def test_eval_1(self):
		v = collatz_eval(1, 10)
		self.assertEqual(v, 20)

	def test_eval_2(self):
		v = collatz_eval(100, 200)
		self.assertEqual(v, 125)

	def test_eval_3(self):
		v = collatz_eval(201, 210)
		self.assertEqual(v, 89)

	def test_eval_4(self):
		v = collatz_eval(900, 1000)
		self.assertEqual(v, 174)

	def test_eval_5(self):
		v = collatz_eval(200,100)
		self.assertEqual(v,125)

	# -----
	# print
	# -----

	def test_print_1(self):
		w = StringIO()
		collatz_print(w, 1, 10, 20)
		self.assertEqual(w.getvalue(), "1 10 20\n")

	def test_print_2(self):
		w = StringIO()
		collatz_print(w, 5, 15, 20)
		self.assertEqual(w.getvalue(), "5 15 20\n")

	def test_print_3(self):
		w = StringIO()
		collatz_print(w, 2, 30, 112)
		self.assertEqual(w.getvalue(), "2 30 112\n")


		# -----
		# solve
		# -----

	def test_solve_1(self):
		r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
		w = StringIO()
		collatz_solve(r, w)
		self.assertEqual(
			w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

	def test_solve_2(self):
		r = StringIO("2 40\n60 500\n30 60\n45 55\n")
		w = StringIO()
		collatz_solve(r, w)
		self.assertEqual(
			w.getvalue(), "2 40 112\n60 500 144\n30 60 113\n45 55 113\n")

	def test_solve_3(self):
		r = StringIO("500 700\n12 36\n907664 870520\n1800 18\n")
		w = StringIO()
		collatz_solve(r, w)
		self.assertEqual(
			w.getvalue(), "500 700 145\n12 36 112\n907664 870520 445\n1800 18 182\n")

	def test_solve_4(self):
		r = StringIO("\n")
		w = StringIO()
		collatz_solve(r,w)
		self.assertEqual(
			w.getvalue(), "\n")

# ----
# main
# ----

if __name__ == "__main__":
	main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1
% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
% coverage-3.5 report -m                   >> TestCollatz.out
% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""