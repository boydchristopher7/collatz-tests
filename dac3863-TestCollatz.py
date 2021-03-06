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
        s = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j,  1)
    def test_read_3(self):
        s = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j,  1)
    def test_read_4(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        assert type(i) == int, "collatz_read did not output an int for the 1st #"
        assert type(i) == int, "collatz_read did not output an int for the 2nd #"
    def test_read_5(self):
        s = "1"
        with self.assertRaises(IndexError):
            collatz_read(s)

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
        v = collatz_eval(753, 746)
        self.assertEqual(v, 140)

    def test_eval_6(self):
        v = collatz_eval(5, 5)
        self.assertEqual(v, 6)
        
    def test_eval_7(self):
        with self.assertRaises(TypeError):
            collatz_eval(5)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")
    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 5, 5, 6)
        self.assertEqual(w.getvalue(), "5 5 6\n")
    def test_print_4(self):
        w = StringIO()
        with self.assertRaises(TypeError):
            collatz_print(w, 5, 5)

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    def test_solve_2(self):
        r = StringIO("800 749\n79 79\n1258 1289\n99 78\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "800 749 153\n79 79 36\n1258 1289 177\n99 78 119\n")
    def test_solve_3(self):
        r = StringIO("500")
        w = StringIO()
        with self.assertRaises(IndexError):
            collatz_solve(r, w)
    def test_solve_4(self):
        r = StringIO("\n")
        w = StringIO()
        collatz_solve(r, w)

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
