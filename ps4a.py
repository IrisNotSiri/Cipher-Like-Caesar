# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # base case: if sequence is a single character
      # return a singleton list containing sequence
    sequlist = []  #resulting list
    if len(sequence) == 1:
      sequlist.append(sequence)
      return sequlist
    
    # a permutation of sequence except the first letter
    for x, letter in enumerate(sequence):
      # print (list(enumerate(sequence)))
      for remain_letter in get_permutations(sequence[:x]+sequence[x+1:]):
        # print (remain_letter)
        sequlist += [letter + remain_letter]
        # the first letter
     
    
    return sequlist
    

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

  example_input1 = 'ab'
  print ('Input:', example_input1)
  print ('Expected Output: ',['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
  print ('Actual Output: ',get_permutations(example_input1))
  print ()
  example_input2 = 'one'
  print ('Input:', example_input2)
  print ('Expected Output: ',['one', 'oen', 'noe', 'noe', 'eon', 'eno'])
  print ('Actual Output: ',get_permutations(example_input2))
  print ()
  example_input3 = 'cup'
  print ('Input:', example_input3)
  print ('Expected Output: ',['cup', 'cpu', 'ucp', 'upc', 'pcu', 'puc'])
  print ('Actual Output: ',get_permutations(example_input3))

  

