# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

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
        self.valid_words = load_words(WORDLIST_FILENAME)
        
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        self.message_text = str(self.message_text)
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy_valid_words = self.valid_words.copy()
        return copy_valid_words
                
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
        # vowels_permutation is a user giving string containing vowels, example1: eioua, example2: ioaeu and so on
        
        dictionary_map = {}
        # give each letter (lower/upper) a number
        n = 0
        import string
        for letter in string.ascii_lowercase: #lowercase letter
          dictionary_map[letter] = n
          n += 1
        
        n = 26
        for letter in string.ascii_uppercase:  #uppercase letter
          dictionary_map [letter] = n
          n += 1
        dictionary1 = dictionary_map.copy()
        # replace vowel letter with given vowels_permutation
        
        # lowercase letter
        dictionary_map['a'] = dictionary1 [vowels_permutation.lower()[0]]
        dictionary_map['e'] = dictionary1 [vowels_permutation.lower()[1]]
        dictionary_map['i'] = dictionary1 [vowels_permutation.lower()[2]]
        dictionary_map['o'] = dictionary1 [vowels_permutation.lower()[3]]
        dictionary_map['u'] = dictionary1 [vowels_permutation.lower()[4]]
        # uppercase letter
        dictionary_map['A'] = dictionary1 [vowels_permutation.upper()[0]]
        dictionary_map['E'] = dictionary1 [vowels_permutation.upper()[1]]
        dictionary_map['I'] = dictionary1 [vowels_permutation.upper()[2]]
        dictionary_map['O'] = dictionary1 [vowels_permutation.upper()[3]]
        dictionary_map['U'] = dictionary1 [vowels_permutation.upper()[4]]
        
        return dictionary_map
        

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        # get text input
        message_text = self.get_message_text()
        # build up an origianl letter map
        original_map = {}
        # give each letter (lower/upper) a number
        n = 0
        import string
        for letter in string.ascii_lowercase: #lowercase letter
          original_map[n] = letter
          n += 1
        
        n = 26
        for letter in string.ascii_uppercase:  #uppercase letter
          original_map [n] = letter
          n += 1
        
        # encrypt message using transpose dictionary
        encrypted_message = []
        
        for letter in message_text:
          
          # Punctuation and spaces should be retained
          if letter in " !@#$%^&*()-_+={}[]|\:;'<>?,./\"":
            # print (letter, end="")
            encrypted_message.append(letter)
          else:
            if letter in CONSONANTS_LOWER or letter in CONSONANTS_UPPER:
              encrypted_message.append(letter)
            else:
              map_num = transpose_dict[letter]
              letter = original_map[map_num]
              encrypted_message.append(letter)
        
        return ''.join(encrypted_message)
          
              

        
        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

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
        # create list of vowels permutations
        try_permutation = get_permutations("aeiou")

        # compare descypted text with valid words
        try_valid_word = {}
        # apply each permutation to the encrypted message
        for perm_list in try_permutation:
          dec_dict = self.build_transpose_dict(perm_list)
          try_decrpt = self.apply_transpose(dec_dict)
          # split message into seperate word
          split_message = try_decrpt.split(' ')
           # compare descypted text with valid words
          valid_words = []
          for word in split_message:
            validity = is_word(self.valid_words, word)
            if validity == True:
              valid_words.append(word)
          try_valid_word[perm_list] = len(valid_words)
        
        # find the permutation having the most valid English words
        best_perm = max(try_valid_word, key=try_valid_word.get)
        if try_valid_word[best_perm] == 0:
          decrypted_message = self.message_text
        else:
          dec_dict = self.build_transpose_dict(best_perm)
          decrypted_message = self.apply_transpose(dec_dict)

        # return best decrypted message
        return decrypted_message

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     


    #TODO: WRITE YOUR TEST CASES HERE
    print()
    permutation = str(input('Choose any vowel permutation: '))
    transpose_dict = SubMessage.build_transpose_dict(SubMessage, permutation)
    
    testcase = SubMessage('Girls Generation fourth full length album "I GOT A BOY" has been released.')
    print ("Original message:", testcase.get_message_text())
    print ("Encryption:", testcase.apply_transpose(transpose_dict))
    
    enc_word= str(input('Please copy the result from last operation: '))
    dec_test = EncryptedSubMessage(enc_word)
    print ("Decrypted message:",dec_test.decrypt_message())
   
    
    
    
          