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

	def test_read(self):
		s = "1 10\n"
		i, j = collatz_read(s)
		self.assertEqual(i,  1)
		self.assertEqual(j, 10)

	def test_read_2(self):
		s = "100 200\n"
		i, j = collatz_read(s)
		self.assertEqual(i,  100)
		self.assertEqual(j, 200)

	def test_read_3(self):
		s = "-12 2000\n"
		i, j = collatz_read(s)
		self.assertEqual(i,  -12)
		self.assertEqual(j, 2000)

	def test_read_4(self):
		s = "45 97\n"
		i, j = collatz_read(s)
		self.assertEqual(i,  45)
		self.assertEqual(j, 97)

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
		v = collatz_eval(16, 5)
		self.assertEqual(v, 5)

    # Test for assert failures

	def test_eval_6(self):
		a = False
		try:
			v = collatz_eval(0, 0)
		except AssertionError:
			a = True
		self.assertTrue(a)

	def test_eval_7(self):
		a = False
		try:
			v = collatz_eval(-5, 16)
		except AssertionError:
			a = True
		self.assertTrue(a)




	# -----
	# print
	# -----

	def test_print(self):
		w = StringIO()
		collatz_print(w, 1, 10, 20)
		self.assertEqual(w.getvalue(), "1 10 20\n")

	def test_print_1(self):
		w = StringIO()
		collatz_print(w, 900, 1000, 174)
		self.assertEqual(w.getvalue(), "900 1000 174\n")

	def test_print_2(self):
		w = StringIO()
		collatz_print(w, 14, 56, 113)
		self.assertEqual(w.getvalue(), "14 56 113\n")

	def test_print_3(self):
		w = StringIO()
		collatz_print(w, 395, 2606, 209)
		self.assertEqual(w.getvalue(), "395 2606 209\n")


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
		r = StringIO("14 56\n395 2606\n15 192\n1 1\n")
		w = StringIO()
		collatz_solve(r, w)
		self.assertEqual(
			w.getvalue(), "14 56 113\n395 2606 209\n15 192 125\n1 1 1\n")

	def test_solve_3(self):
		r = StringIO("48 285\n5 529\n124 465\n253 263\n")
		w = StringIO()
		collatz_solve(r, w)
		self.assertEqual(
			w.getvalue(), "48 285 128\n5 529 144\n124 465 144\n253 263 123\n")

	def test_solve_4(self):
		r = StringIO("124 853\n1000 2000\n528 10393\n540 785\n")
		w = StringIO()
		collatz_solve(r, w)
		self.assertEqual(
			w.getvalue(), "124 853 171\n1000 2000 182\n528 10393 262\n540 785 171\n")

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
