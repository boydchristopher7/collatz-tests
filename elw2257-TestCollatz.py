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
        s = "11 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  11)
        self.assertEqual(j, 100)

    def test_read_3(self):
        s = "127 100"
        i, j = collatz_read(s)
        self.assertEqual(i,  127)
        self.assertEqual(j, 100)
    def test_read_4(self):
        s = "200 400"
        i, j = collatz_read(s)
        self.assertEqual(i,  200)
        self.assertEqual(j, 400)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10, dictionary = {})
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200, dictionary = {})
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210, dictionary = {})
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000, dictionary = {})
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(1000, 1500, dictionary = {})
        self.assertEqual(v, 182)

    def test_eval_6(self):
        v = collatz_eval(27, 43, dictionary = {})
        self.assertEqual(v, 112)

    def test_eval_7(self):
        v = collatz_eval(15001, 20000, dictionary = {})
        self.assertEqual(v, 279)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 27, 43, 112)
        self.assertEqual(w.getvalue(), "27 43 112\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 15001, 20000, 279)
        self.assertEqual(w.getvalue(), "15001 20000 279\n")        
    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n1000 1500 182\n27 43 112\n15001 20000 279\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n1000 1500 182\n27 43 112\n15001 20000 279\n")

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
