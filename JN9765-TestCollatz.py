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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz,collatz_eval1, collatz_helper

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
        
    def test_read1(self):
    	s = "2 40\n"
    	i,j = collatz_read(s)
    	self.assertEqual(i, 2)
    	self.assertEqual(j,40)
    	
    def test_read2(self):
    	s = "10000 40000\n"
    	i,j = collatz_read(s)
    	self.assertEqual(i, 10000)
    	self.assertEqual(j,40000)
    	
    def test_read3(self):
    	s = "20000000 40000000\n"
    	i,j = collatz_read(s)
    	self.assertEqual(i, 20000000)
    	self.assertEqual(j,40000000)
    
    
    
    def test_chelper(self):
    
    	v = collatz_helper(136446, 21390)
    	self.assertEqual(v,354)
    	
    def test_chelper2(self):
    	v = collatz_helper(500455, 200000)
    	self.assertEqual(v,449)
    	
    def test_chelpe3r(self):
    	v = collatz_helper(136446, 136447)
    	self.assertEqual(v,344)
    	
    def test_chelper4(self):
    	v = collatz_helper(136446, 210393)
    	self.assertEqual(v,383)
    
    def test_chelper5(self):
    	v = collatz_helper(20001,40000)
    	self.assertEqual(v,324)
    # ----
    # eval
    # ----
    
    
    def test_eval(self):
    	v = collatz_eval(81385,914551)
    	self.assertEqual(v,525)
    	
    def test_eval1(self):
    	v = collatz_eval(656571, 337514)
    	self.assertEqual(v,509)
    	
    def test_eval2(self):
    	v = collatz_eval(154120, 2166)
    	self.assertEqual(v,375)
    	
    def test_eval3(self):
    	v = collatz_eval(390271, 450121)
    	self.assertEqual(v,449)
    	
    	
   
    
    
    # ----
    # eval1
    # ----

    def test_eval_1(self):
        v = collatz_eval1(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval1(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval1(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval1(900, 1000)
        self.assertEqual(v, 174)
        
        
    def test_eval_5(self):
    	v = collatz_eval1(450,600)
    	self.assertEqual(v,142)
    
    def test_eval_6(self):
    	v = collatz_eval1(10000,11000)
    	self.assertEqual(v,268) 
    	
    def test_eval_7(self):
    	v = collatz_eval1(20000,30000)
    	self.assertEqual(v,308)
    
    def test_eval_8(self):
    	v = collatz_eval1(400,600)
    	self.assertEqual(v,142)
    	
    	
    
    
    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
        
    def test_print1(self):
    	w = StringIO()
    	collatz_print(w,200,1000,314)
    	self.assertEqual(w.getvalue(),"200 1000 314\n")
    	
    def test_print2(self):
    	w = StringIO()
    	collatz_print(w,4121212,212121212,456)
    	self.assertEqual(w.getvalue(),"4121212 212121212 456\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
            
            
    def test_solve1(self):
        r = StringIO("10 20\n400 600\n1000 1500\n1501 2000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 20 21\n400 600 142\n1000 1500 182\n1501 2000 180\n")
            
    def test_solve2(self):
        r = StringIO("600 659\n6000 6400\n1000 1230\n5000 6000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "600 659 145\n6000 6400 262\n1000 1230 182\n5000 6000 236\n")
            
  	# -----
	# Collatz
	# -----
   
    def test_collatz(self):
    	v = collatz(68)
    	self.assertEqual(v,15)
   
    def test_collatz1(self):
    	v = collatz(6000)
    	self.assertEqual(v,50)
    	
    def test_collatz2(self):
    	v = collatz(85311)
    	self.assertEqual(v,103)
	

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
