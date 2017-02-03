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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_compute

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
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)
        
    def test_read_2(self):
        s = "134 987654\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 134)
        self.assertEqual(j, 987654)
        
    def test_read_3(self):
        s = "548 125464\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 548)
        self.assertEqual(j, 125464)
        
    # ----
    # compute
    # ----

    def test_compute_1(self):
        v = collatz_compute(465)
        self.assertEqual(v, 36)

    def test_compute_2(self):
        v = collatz_compute(645543)
        self.assertEqual(v, 173)

    def test_compute_3(self):
        v = collatz_compute(100000)
        self.assertEqual(v, 129)
        
        
    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(2, 2)
        self.assertEqual(v, 2)
        
    def test_eval_4(self):
        v = collatz_eval(516734, 866286)
        self.assertEqual(v, 525)
        
    def test_eval_5(self):
        v = collatz_eval(1, 9999)
        self.assertEqual(v, 262)
        
    def test_eval_6(self):
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)
        
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
        r = StringIO("20 545\n1 1\n899000 900000\n10 200\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "20 545 144\n1 1 1\n899000 900000 295\n10 200 125\n")
            
    def test_solve_3(self):
        r = StringIO("1 10\n100 200\n1000 2000\n10000 20000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n1000 2000 182\n10000 20000 279\n")

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
