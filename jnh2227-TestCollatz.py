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
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "1 27\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 27)

    def test_read_3(self):
        s = "1000 10000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1000)
        self.assertEqual(j, 10000)

    def test_read_4(self):
        s = "900 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 900)
        self.assertEqual(j, 1000)
        
    def test_read_5(self):
        s = "1 100000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 100000)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(27, 1)
        self.assertEqual(v, 112)

    def test_eval_3(self):
        v = collatz_eval(1000, 10000)
        self.assertEqual(v, 262)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(1, 100000)
        self.assertEqual(v, 351)
        

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 1, 27, 112)
        self.assertEqual(w.getvalue(), "1 27 112\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1000, 10000, 262)
        self.assertEqual(w.getvalue(), "1000 10000 262\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")

    def test_print_5(self):
        w = StringIO()
        collatz_print(w, 1, 100000, 351)
        self.assertEqual(w.getvalue(), "1 100000 351\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n1 27\n1000 10000\n900 1000\n1 100000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n1 27 112\n1000 10000 262\n900 1000 174\n1 100000 351\n")

    def test_solve_2(self):
        r = StringIO("1 10\n1 27\n1000 10000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n1 27 112\n1000 10000 262\n")

    def test_solve_3(self):
        r = StringIO("900 1000\n1 100000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "900 1000 174\n1 100000 351\n")


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
