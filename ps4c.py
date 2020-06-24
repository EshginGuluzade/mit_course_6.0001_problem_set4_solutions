# Problem Set 4C
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
from ps4a import get_permutations
file_name = 'words.txt'
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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
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
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # it is result dictinoary
        my_dict = {}
        # pasting lower consonants to my_dict
        for i in CONSONANTS_LOWER:
            my_dict[i] = i
        # pasting upper consonants to my_dict
        for j in CONSONANTS_UPPER:
            my_dict[j] = j
            
        # pasting lower wovels to my_dict by transposing them
        vowels_permutation = vowels_permutation.lower()
        count = 0
        for n in vowels_permutation:
            my_dict[n] = VOWELS_LOWER[count]
            count+=1
            
        # pasting upper wovels to my_dict by transposing them
        vowels_permutation = vowels_permutation.upper()
        count = 0
        for m in vowels_permutation:
            my_dict[m] = VOWELS_UPPER[count]
            count+=1
        
        return my_dict

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        text = self.get_message_text()
        # encrypted list
        encrypted_text = []
        # encrypted string
        encrypted_text_string = ''
        
        # take each character in given text
        for i in text:
          # if the character is a letter, convert that character to corresponding transposed letter  
          if i.isalpha():  
            encrypted_text.append(transpose_dict[i])
          # if the character is not a letter, remain that character as it is
          else:
            encrypted_text.append(i)
        
        # convert output encrypted text list to encrypted text string
        for j in encrypted_text:
            encrypted_text_string+=j
            
        return encrypted_text_string
        
          
        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)
        

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        perm_list = get_permutations('aeiou')
        tranpose_dict_list = []
        decrypted_message_list = []
        perm_list = get_permutations('aeiou')
        
        new_dict = {}
        word_list = self.get_valid_words()
        
        # storing each permutation to the transposed dictionary list
        for perm in perm_list:
            tranpose_dict_list.append(self.build_transpose_dict(perm))
            
        # storing each decrypted message to the decrypted message list
        for dic in tranpose_dict_list:
            decrypted_message = self.apply_transpose(dic)
            decrypted_message_list.append(decrypted_message)
        
        
        for each_mes in decrypted_message_list:
            
            decrypted_words = each_mes.split()
            n=0
            for word in decrypted_words:
                
                if is_word(word_list, word):
                    n+=1
                else:
                    continue
            
            new_dict[each_mes] = n
            
                
        # the next 3 lines of code just determines the key which corresponding to the 
        # maximum of 'n' in the new_dict(dictionary)
        key_list = list(new_dict.keys()) 
        val_list = list(new_dict.values()) 
        best_decrypted_message = key_list[val_list.index(max(new_dict.values()))]
        ##################################################################
                
        return best_decrypted_message
        #return new_dict
    
        

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    print('-------------------------------------------------')
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    message = SubMessage("Their WoRlD wilL LoVe RobotS")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Thair WuRlD wilL LuVa RubutS")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    print('-------------------------------------------------')
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())