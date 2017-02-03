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
        s = "150 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  150)
        self.assertEqual(j, 200)

    def test_read_3(self):
        s = "201 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  201)
        self.assertEqual(j, 1000)

    def test_read_4(self):
        s = "1001 2000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1001)
        self.assertEqual(j, 2000)


    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(150, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 1000)
        self.assertEqual(v, 179)

    def test_eval_4(self):
        v = collatz_eval(1001, 2000)
        self.assertEqual(v, 182)

    def test_eval_5(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 150, 200, 125)
        self.assertEqual(w.getvalue(), "150 200 125\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 201, 1000, 179)
        self.assertEqual(w.getvalue(), "201 1000 179\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 1001, 2000, 182)
        self.assertEqual(w.getvalue(), "1001 2000 182\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n2 20\n3 30\n4 40\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n2 20 21\n3 30 112\n4 40 112\n")
    
    def test_solve_2(self):
        r = StringIO("150 200\n201 250\n251 300\n301 350\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "150 200 125\n201 250 128\n251 300 123\n301 350 144\n")

    def test_solve_3(self):
        r = StringIO("1 1000\n1001 2000\n2001 3000\n3001 4000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1000 179\n1001 2000 182\n2001 3000 217\n3001 4000 238\n")

    def test_solve_4(self):
        r = StringIO("1 1000\n1001 2000\n2001 3000\n3001 4000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1000 179\n1001 2000 182\n2001 3000 217\n3001 4000 238\n")

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
