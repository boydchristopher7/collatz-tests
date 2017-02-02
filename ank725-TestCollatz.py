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
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100)
        self.assertEqual(j, 200)

    def test_read_3(self):
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  201)
        self.assertEqual(j, 210)

    def test_read_4(self):
        s = "511000 613555\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  511000)
        self.assertEqual(j, 613555)

    def test_read_5(self):
        s = "1 1555\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 1555)

    def test_read_6(self):
        s = "10020 10100\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  10020)
        self.assertEqual(j, 10100)



    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(340, 50000)
        self.assertEqual(v, 324)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_6(self):
        v = collatz_eval(10020, 10100)
        self.assertEqual(v, 224)

    def test_eval_7(self):
        v = collatz_eval(511000, 613000)
        self.assertEqual(v, 470)

    def test_eval_8(self):
        v = collatz_eval(510500, 613555)
        self.assertEqual(v, 470)

    def test_eval_9(self):
        v = collatz_eval(511500, 511600)
        self.assertEqual(v, 227)

    def test_eval_10(self):
        v = collatz_eval(1, 1555)
        self.assertEqual(v, 182)

    def test_eval_11(self):
        v = collatz_eval(1, 1000000)
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
        collatz_print(w, 340, 50000, 324)
        self.assertEqual(w.getvalue(), "340 50000 324\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n340 50000\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n340 50000 324\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("190138 451670\n889718 238518\n429607 732976\n698903 475562\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "190138 451670 449\n889718 238518 525\n429607 732976 509\n698903 475562 509\n")

    def test_solve_3(self):
        r = StringIO("187254 944240\n202662 890034\n978460 910327\n581197 831916\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "187254 944240 525\n202662 890034 525\n978460 910327 507\n581197 831916 509\n")



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
