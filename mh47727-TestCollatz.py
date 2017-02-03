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
        s = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j,  1)

    def test_read_2(self):
        s = "999999 69\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 999999)
        self.assertEqual(j, 69)

    def test_read_3(self):
        s = "3 1337\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 3)
        self.assertEqual(j, 1337)

    def test_read_4(self):
        s = "5000 4000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 5000)
        self.assertEqual(j, 4000)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1337, 454)
        self.assertEqual(v, 182)

    def test_eval_2(self):
        v = collatz_eval(888, 777)
        self.assertEqual(v, 179)

    def test_eval_3(self):
        v = collatz_eval(666, 777)
        self.assertEqual(v, 171)

    def test_eval_4(self):
        v = collatz_eval(2012, 2016)
        self.assertEqual(v, 113)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 69, 1337, 323)
        self.assertEqual(w.getvalue(), "69 1337 323\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 2, 2, 17)
        self.assertEqual(w.getvalue(), "2 2 17\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 12, 25, 16)
        self.assertEqual(w.getvalue(), "12 25 16\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("10 1\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("426 5440\n10 4170\n947 5992\n1373 409\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "426 5440 238\n10 4170 238\n947 5992 238\n1373 409 182\n")

    def test_solve_3(self):
        r = StringIO("69 1\n59 4069\n3056 3419\n69 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "69 1 113\n59 4069 238\n3056 3419 199\n69 1 113\n")


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
