## 509. Fibonacci Number
## https://leetcode.com/problems/fibonacci-number/

# O(2^n) solution 

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0 
        if n == 1: return 1
        return self.fib(n-1) + self.fib(n-2)

# O(n) with space O(n)

mem = {}
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0 
        if n == 1: return 1
        if n-1 not in mem:
            mem[n-1] = self.fib(n-1)
        if n-2 not in mem:
            mem[n-2] = self.fib(n-2)
        return mem[n-1] + mem[n-2]

# O(n) with space O(1)

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        cur=0
        pre1=1
        pre2=1
        for i in range(3, n+1):
            cur=pre1+pre2
            pre2 = pre1
            pre1 = cur
        return cur