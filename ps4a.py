# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

'''
# mit_course_number_6.0001_problem_set4_solutions

MIT Course 6.0001: Introduction to Computer Science and Programming in Python

Author: Eshgin Guluzade

Specialty: Mechanical Engineer

Country: Azerbaijan

My LinkedIn: https://www.linkedin.com/in/eshginguluzade/

My Quora: https://www.quora.com/profile/Eshgin-Guluzade

My Youtube Channel: https://www.youtube.com/channel/UCr6yufueEVaXBHgM8x1YlTw

'''


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
    # output list which will show all permutaions of given input (sequence)
    created_list = []
    
    # base case
    if len(sequence) == 1:
        return sequence
    
    # recursive case
    else:
        # reduce problem and get all permutations of length of { len(sequence) - 1 }
        # means that first character is not included
        get_perms = get_permutations(sequence[1:]) 
        # get the first character of sequence
        first_char = sequence[0]
        
        # get the permutations of get_perms one by one
        for i in get_perms:
        # range will be just length of given input(sequence)
            for j in range(len(i) + 1):
        # increase list by adding permutations one by one
                created_list.append(i[:j] + first_char + i[j:])
        # return the output list
        return created_list
                
            
    

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
     sequence = input('Enter the sequence to be permuated: ')
#    print('Input:', example_input)
     print('Input: ', sequence)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

#    print('Actual Output:', get_permutations(example_input))
     print('Actual Output: ', get_permutations(sequence))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
