# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

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
    word = word.strip (" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read()) #The read() method returns the specified number of bytes from the file. 
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
        
        
        return dictionary_map
        
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # get text input
        message_text = self.get_message_text()
        # dictionary map for shift
        dic_map = self.build_shift_dict(shift)

        # print (dic_map)  # need to be deleted eventually
        
        # shift down alphabet
        # print (message_text)  # need to be deleted eventually
        shifted_message = []
        
        for letter in message_text:
          
          # Punctuation and spaces should be retained
          if letter in " !@#$%^&*()-_+={}[]|\:;'<>?,./\"":
            # print (letter, end="")
            shifted_message.append(letter)
          else:
            # location of letter before shift
            letter_num = dic_map [letter]
        
            # location of letter after shift
            aftershift = letter_num + shift
  
            # aftershif >26 exceed length of alphabet(upper/lower case divided)
            if letter_num <= 25:
              if aftershift <= 25:
                shifted_letter = string.ascii_lowercase [aftershift]
              else:
                aftershift -= 26
                shifted_letter = string.ascii_lowercase [aftershift]
  
            else:
              if aftershift <= 51:
                aftershift -= 26
                shifted_letter = string.ascii_uppercase [aftershift]
              else:
                aftershift -= 52
                shifted_letter = string.ascii_uppercase [aftershift]

            # print (shifted_letter, end='')
            shifted_message.append(shifted_letter)
        # return encrypted text
        return ''.join(shifted_message)

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
        super().__init__(text)
        self.shift = shift
        self.encryption_dict = super().build_shift_dict(shift)
        self.message_text_encrypted = super().apply_shift(shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        self.shift = int(self.shift)
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        copy_encryption_dict = self.encryption_dict.copy()
        return copy_encryption_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        self.message_text_encrypted = str(self.message_text_encrypted)
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        
        PlaintextMessage.shift = shift
        self.encryption_dict = super().build_shift_dict(shift)
        self.message_text_encrypted = super().apply_shift(shift)
        
        return


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)
        
        
       

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
        
        # use self.valid_words to create valid words list
        # apply shift using (shift = 26-s)
        shift_valid_words = {}
        s = 0
        while 0 <= s < 26:
          try_shift = self.apply_shift(26-s)
          # split message into seperate word
          split_message = try_shift.split(' ')
           # compare descypted text with valid words
          valid_words = []
          for word in split_message:
            validity = is_word(self.valid_words, word)
            if validity == True:
              valid_words.append(word)
          # to find the maximum number of valid words and its shift
          shift_valid_words[s] = len(valid_words)
          s += 1
        
        max_shift = 26-max(shift_valid_words, key=shift_valid_words.get)
        decrypted_message = self.apply_shift(max_shift)
        
        # print ("The best shift is:", max_shift)
        # print ("The decrypted messaged is:", decrypted_message)
        # return best shift and decrypted message
        return max_shift, decrypted_message

if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#     
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    # test 1
    print ('Testcase 1: PlaintextMessage')
    test1 = PlaintextMessage('Oh My Girl', 2)
    print('Expected Output: Qj Oa Iktn')
    print('Actual Output:', test1.get_message_text_encrypted())

    #test 2
    print ()
    print ('Testcase 2: CiphertextMessage')
    test2 = CiphertextMessage ('Qj Oa Iktn')
    print('Expected Output:', (24, 'Oh My Girl'))
    print('Actual Output:', test2.decrypt_message())
    
    
    #TODO: best shift value and unencrypted story 
    print ()
    print ('Story descryption')
    story = get_story_string()
    load3 = CiphertextMessage (story)
    print ("Decrypted text:", load3.decrypt_message())
    
  
    
    
   


    
    
   

 
    
  
    
   
   
    

   
      