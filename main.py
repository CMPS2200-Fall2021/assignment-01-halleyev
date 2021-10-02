"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
    #iterative sequential version
    tempcounter = 0
    finalcount = 0
    for i in mylist:
        if i != key:
            if tempcounter > finalcount:
                finalcount = tempcounter
            tempcounter = 0
        else:
            tempcounter += 1
            if tempcounter > finalcount:
                finalcount = tempcounter
    return finalcount


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key

    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))


def longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if key in mylist:
            return Result(1,1,1,True)
        else:
            return Result(0,0,0,False)
    half= len(mylist)//2
    right = longest_run_recursive(mylist[half:],key)
    left = longest_run_recursive(mylist[:half],key)
    if right.is_entire_range == True and left.is_entire_range == True:
        return Result(left.longest_size, right.longest_size, len(mylist), True)
    elif right.is_entire_range == True:
        return Result(left.left_size,right.longest_size + left.right_size,right.longest_size + left.right_size,False)
    elif left.is_entire_range == True:
        return Result(left.longest_size + right.left_size,right.right_size, left.longest_size + right.left_size,False)
    elif mylist[half] == key and mylist[half - 1] == key:
        ans = max(left.longest_size, right.longest_size, right.left_size + left.right_size)
        return Result(left.right_size,right.left_size,ans, False)
    else:
        return Result(left.left_size, right.right_size,max(right.longest_size,left.longest_size),False)


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
