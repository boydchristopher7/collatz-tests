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

        s = "15 45\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 15)
        self.assertEqual(j, 45)

        s = "1717 2222\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1717)
        self.assertEqual(j, 2222)

        s = "214 1210\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 214)
        self.assertEqual(j, 1210)

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
        v = collatz_eval(800, 500)
        self.assertEqual(v, 171)
        
    def test_eval_6(self):
        v = collatz_eval(500, 800)
        self.assertEqual(v, 171)
        
    def test_eval_7(self):
        v = collatz_eval(99, 100)
        self.assertEqual(v, 26)
        
    def test_eval_8(self):
        v = collatz_eval(2600, 5177)
        self.assertEqual(v, 238)

    def test_eval_9(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)
    # -----
    # print
    # -----

    def test_print1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print2(self):
        w = StringIO()
        collatz_print(w, 17, 19, 21)
        self.assertEqual(w.getvalue(), "17 19 21\n")

    def test_print3(self):
        w = StringIO()
        collatz_print(w, 81, 96, 111)
        self.assertEqual(w.getvalue(), "81 96 111\n")

    def test_print4(self):
        w = StringIO()
        collatz_print(w, 700, 7, 145)
        self.assertEqual(w.getvalue(), "700 7 145\n")

    # -----
    # solve
    # -----

    def test_solve1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        r = StringIO("214 1210\n99 100\n1 1\n800 500\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "214 1210 182\n99 100 26\n1 1 1\n800 500 171\n")

    def test_solve3(self):
        r = StringIO("2600 5177\n444 777\n501 550\n53 35\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "2600 5177 238\n444 777 171\n501 550 137\n53 35 110\n")

    def test_solve4(self):
        r = StringIO("13457 98111\n456 789\n32415 87969\n17 19\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "13457 98111 351\n456 789 171\n32415 87969 351\n17 19 21\n")




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
