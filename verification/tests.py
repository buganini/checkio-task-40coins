"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
def balance(__fake_i__ , __fake_w__):
    def g():        
        result = None
        for t in range(5):            
            left, right = yield result
            if len(left) > len(right):
                result = -1
            elif len(right) > len(left):
                result = 1
            elif (__fake_i__-11331)>>5  in left:
                result = -__fake_w__
            elif (__fake_i__-11331)>>5 in right:
                result = __fake_w__
            else:
                result = 0
        yield result
    
    rtn = g()
    next(rtn)
    return rtn

TESTS = {
    "Extra": []
}
from random import randint

for i in range(10):            
     i = randint(0,100)
     w = randint(0,1)*2-1
     # g = balance((i<<5)+11331, w)
     TESTS["Extra"].append({"input": (i,w), "answer": i*w }) 

