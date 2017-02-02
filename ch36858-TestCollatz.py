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

    def test_read1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read2(self):
        s = "11 20\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  11)
        self.assertEqual(j, 20)

    def test_read3(self):
        s = "21 30\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  21)
        self.assertEqual(j, 30)




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
        v = collatz_eval(300, 400)
        self.assertEqual(v, 144)

    def test_eval_6(self):
        v = collatz_eval(401, 500)
        self.assertEqual(v, 142)

    def test_eval_7(self):
        v = collatz_eval(501, 600)
        self.assertEqual(v, 137)

    def test_eval_8(self):
        v = collatz_eval(601, 700)
        self.assertEqual(v, 145)


    def test_eval_9(self):
        v = collatz_eval(701, 800)
        self.assertEqual(v, 171)

    def test_eval_10(self):
        v = collatz_eval(801, 900)
        self.assertEqual(v, 179)

    def test_eval_11(self):
        v = collatz_eval(901, 1000)
        self.assertEqual(v, 174)

    def test_eval_12(self):
        v = collatz_eval(1001, 1100)
        self.assertEqual(v, 169)



    # -----
    # print
    # -----

    def test_print1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

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
        r = StringIO("300 400\n401 500\n501 600\n601 700\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "300 400 144\n401 500 142\n501 600 137\n601 700 145\n")

    def test_solve3(self):
        r = StringIO("701 800\n801 900\n901 1000\n1001 1100\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "701 800 171\n801 900 179\n901 1000 174\n1001 1100 169\n")
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
