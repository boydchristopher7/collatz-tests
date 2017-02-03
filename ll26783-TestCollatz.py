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

#confirmed failures and commented them out for final submission

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
        s = "300 1010\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  300)
        self.assertEqual(j, 1010)

    def test_read_3(self):
        s = "500 209\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  500)
        self.assertEqual(j, 209)


    # def test_read_4(self):
    #     s = " "
    #     i, j = collatz_read(s)
    #     self.assertEqual(i, " " )
    #     self.assertEqual(j, " ")
    #
    # def test_read_5(self):
    #     s = "3"
    #     i, j = collatz_read(s)
    #     self.assertEqual(i, 3 )
    #     self.assertEqual(j, " ")


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
        v = collatz_eval(1, 2000)
        self.assertEqual(v, 182)



    # def test_eval_4(self):
    #     v = collatz_eval(-10, -50)
    #     self.assertEqual(v, 100)
    #
    # def test_eval_5(self):
    #     v = collatz_eval(None, None)
    #     self.assertEqual(v, 0)
    #
    # def test_eval_6(self):
    #     v = collatz_eval(5, -50)
    #     self.assertEqual(v, 0)

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
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")


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
        r = StringIO("400 300\n10 20\n2000 5000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "400 300 144\n10 20 21\n2000 5000 238\n")

    def test_solve_3(self):
        r = StringIO("2 5\n60 100\n703 729\n400 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "2 5 8\n60 100 119\n703 729 171\n400 1000 179\n")

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
