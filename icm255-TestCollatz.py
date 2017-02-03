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

    #Read 2 numbers
    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    #Read another 2 numbers
    def test_read_2(self):
        s = "7805 15899\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  7805)
        self.assertEqual(j, 15899)

    #Read another 2 numbers
    def test_read_3(self):
        s = "17 28\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  17)
        self.assertEqual(j, 28)

    #Read negative numbers
    def test_read_4(self):
        s = "-29 -40\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  -29)
        self.assertEqual(j, -40)

    #Read the same number
    def test_read_5(self):
        s = "3 3\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 3)
        self.assertEqual(j, 3)

    #Read a different set of 2 numbers
    def test_read_6(self):
        s = "50 380\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  50)
        self.assertEqual(j, 380)
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
        v = collatz_eval(1200, 1500)
        self.assertEqual(v, 177)

    def test_eval_6(self):
        v = collatz_eval(5000, 500000)
        self.assertEqual(v, 449)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")

    def test_print_5(self):
        w = StringIO()
        collatz_print(w, 1200, 1500, 177)
        self.assertEqual(w.getvalue(), "1200 1500 177\n")

    def test_print_6(self):
        w = StringIO()
        collatz_print(w, 5000, 500000, 449)
        self.assertEqual(w.getvalue(), "5000 500000 449\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    #Test backwards numbers
    def test_solve_2(self):
        r = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    #Test negative numbers
    def test_solve_3(self):
        r = StringIO("-1 -10\n-100 200\n-201 210\n-668 -995\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "-1 -10 20\n-100 200 125\n-201 210 89\n-668 -995 179\n")

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
