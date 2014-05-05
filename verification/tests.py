"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Extra": []
}
from random import randint

for i in range(1000):            
     i = randint(0,100)
     w = randint(0,1)*2-1
     # g = balance((i<<5)+11331, w)
     TESTS["Extra"].append({"input": ((i<<5)+11331 ,w), "answer": i*w }) 

