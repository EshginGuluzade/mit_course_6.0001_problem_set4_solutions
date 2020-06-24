# Problem Set 4B
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



import string
file_name = "words.txt"
### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(file_name)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # for now, it is empty dictionary but it will be result dictionary in the end
        my_dict = {}
        # upper letters
        uletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # lower letters
        lletters = 'abcdefghijklmnopqrstuvwxyz'
        # it shows the position of i in letters
        n=0
        
        # this 'for' loop maps upper letters
        for i in uletters:
           if (n+shift)>25:
              my_dict[i] = uletters[(n+shift)-25-1]
           else:
              my_dict[i] = uletters[n + shift]
           n+=1
        m=0
        
        # this 'for' loop maps lower letters
        for j in lletters:
           if (m+shift)>25:
              my_dict[j] = lletters[(m+shift)-25-1]
           else:
              my_dict[j] = lletters[m + shift]
           m+=1
           
        return my_dict
         
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift    s    
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # paste our text to this variable
        our_text = self.get_message_text()
        
        our_text_list = []
        
        new_text_list = []
        
        new_text_list_to_string = ''
        
        shifted_letters = self.build_shift_dict(shift)
        
        n=0
        # creating the list from given text
        for i in our_text:
            our_text_list.append(i)
            n+=1
           
        m=0   
        # creating new shifted letter list from given text list (our_text_list)
        for j in our_text_list:
            if (j in shifted_letters):
              new_text_list.append(shifted_letters[j])
            
            else:
                new_text_list.append(j)
            m+=1
        
        # Pasting new shifted letter list(new_text_list) to a string
        for i in new_text_list:
            new_text_list_to_string += i
            
        return new_text_list_to_string

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        new_dict = {}
        new_string =''
        new_list = []
        word_list = self.get_valid_words()
        
        for shift in range(26):
            # decrypted message text
            d_m_t = self.apply_shift((26-shift))
            # decrypted message text list
            d_m_t_list = d_m_t.split()
            
            n=0
            # checking how many times words shown in the wordlist
            # this for loop gets the 'n' = number of valid words
            # we will use the biggest 'n' to find best shift value
            for i in d_m_t_list:
                if is_word(word_list, i):
                    n+=1
                else:
                    continue
            # storing shift value to the corresponding 'n' by creating a dictionary
            # shift = key, 'n' = value
            new_dict[shift] = n
            
            # creating a list that is related to current shift value and 'n'
            new_list.append(d_m_t)
            
            # increasing shift value one by one (0-26)
            shift+=1
        
        ##################################################################
        # the next 3 lines of code just determines the key which corresponding to the 
        # maximum o 'n' in the new_dict(dictionary)
        key_list = list(new_dict.keys()) 
        val_list = list(new_dict.values()) 
        best_shift = key_list[val_list.index(max(new_dict.values()))]
        ##################################################################
        
        # creting a tuple that stores best decrypted shift value and decrypted text whixh is
        # related to that shift value
        my_tuple = ((26 - best_shift ), new_list[best_shift])
        
        return my_tuple
            
if __name__ == '__main__':
    
#    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    print('-----------------------------------------------------------')
    
#    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
    print('-----------------------------------------------------------')
  
    #TODO: WRITE YOUR TEST CASES HERE
    plaintext = PlaintextMessage('apple', 15)
    print('Expected Output: peeat')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    print('-----------------------------------------------------------')
    
    ciphertext = CiphertextMessage('PeEat')
    print('Expected Output:', (11, 'ApPle'))
    print('Actual Output:', ciphertext.decrypt_message())
    print('-----------------------------------------------------------')
    
    #TODO: best shift value and unencrypted story 
    ciphertext = CiphertextMessage(get_story_string())
    print('Actual story:', ciphertext.decrypt_message())
    print('-----------------------------------------------------------')
    
   # pass #delete this line and replace with your code here
