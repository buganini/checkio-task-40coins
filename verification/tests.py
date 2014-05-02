"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ([1, 3, 2, 4], 2) ,
            "answer": 8,
            "explanation": "2*4=?"
        },
        {
            "input": ([5, 7,1,1,1,1,5], 3),
            "answer": 35,
            "explanation": "5*7*1=?"
        }
    ],
    "Extra": []
}
from random import randint
def prod(l):
    r = 1
    for x in l:
        r*=x
    return r
def f(l,n):
    return max(prod(l[i:i+n]) for i in range(len(l)-n+1))
for i in range(10):
     n = randint(2,10)
     l = [randint(1, 100) for x in range(10**4)]
     TESTS["Extra"].append({"input": (l,n), "answer": f(l,n)}) 

