# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

""" 
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Ex 1)
n = 3 
F(3) = F(2) + F(1) = 1 +1 = 2
"""

# Recursive version
# Time Complexity: O(2^n)
# Space Complexity: O(N)
class Solution:
    def fib(self, n:int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-2) + self.(n-1)


# Use Memoizaition with Bottom-Top Approach
# Time Complexity: O(N)
# Space Compelxity: O(N)

mem ={}
class Solution:
    def fib(self, n: int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n-1 not in mem:
            mem[n-1] = self.fib(n-1)
        if n-2 not in mem:
            mem[n-2] = self.fib(n-2)
        return mem[n-1] + mem[n-2]


