"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  if x <= 1:
    return x
  else:
    ra = foo(x-1)
    rb = foo(x-2)
    return ra + rb

def longest_run(mylist, key):
    current = 0
    longest = 0
    for i in mylist:
      if i == key:
        current += 1
        longest = max(longest, current)
      else: 
        current = 0
    return longest


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
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    # If we have a length of zero we have no run
    if len(mylist) == 0:
      return Result(0, 0, 0, True)
    # If we have a length of one we need to check whether or not the key exists
    elif len(mylist) == 1:
      if mylist[0] == key:
        return Result(1, 1, 1, True)
      else:
        return Result(0, 0, 0, False)
    # Recursive case
    else:
      # First we create left and right halves of the list
      mid = len(mylist) // 2
      left_result = longest_run_recursive(mylist[:mid], key)
      right_result = longest_run_recursive(mylist[mid:], key)

      is_entire_range = left_result.is_entire_range and right_result.is_entire_range
      
      # Extract the longest size from each result
      left_size = left_result.left_size
      right_size = right_result.right_size

      
      if mylist[mid] == key and mylist[mid-1] == key:
        mid_run = left_result.right_size + right_result.left_size
      else:
        mid_run = 0

      if left_result.is_entire_range:
        left_size = left_size + right_result.left_size
      if right_result.is_entire_range:
        right_size = right_size + left_result.right_size
      # Set the longest size to the max of our three counters
      longest_size = max(left_result.longest_size, right_result.longest_size, mid_run)


      return Result(left_size, right_size, longest_size, is_entire_range)



