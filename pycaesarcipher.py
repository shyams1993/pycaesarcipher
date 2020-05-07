class pycaesarcipher():
    '''
    DOCSTRING: This class contains the encipher function & decipher function to one of the most simplest substitution Ciphers - "Caesar's Cipher"
    '''
    
    def __init__(self):
        return None

    def caesar_encipher(self,word,shiftkey):
        '''
        DOCSTRING: Function to encipher a given string using caesar cipher.
        \nINPUT: Any string and shiftkey.
        \nLOGIC: To encrypt, it uses the basic formula : (character + shiftkey)
        \nOUTPUT: The Enciphered string result.
        \nUSAGE: First import the CaesarCipher package; Then, create an instance of the class by using a variable to assign & call an instance of the class.
        \nSyntax: variable_name = CaesarCipher()
        \nThen create another variable to call either the caesar_encipher() method or caesae_decipher() method using two positional arguments : target word/variable, shiftkey
        \nSyntax: another_variable = variable_name.caesar_encipher("string",integer)
        \n\nThis logic uses ASCII code representation to convert the strings to integers. You can use any string, but this method will convert the string to lowercase and then encipher to maintain uniformity.
        '''
        word = word.lower()
        ciphertext = []
        for w in range(len(word)):
            x = (ord(word[w]) + shiftkey)
            if x > 122:
                y = (x-122)+96
                ciphertext.append(chr(y))
            elif ord(word[w]) == 32:
                y = 32
                ciphertext.append(chr(y))
            else:
                ciphertext.append(chr(x))
        word = ''.join([str(s) for s in ciphertext])
        return word

    def caesar_decipher(self,word,shiftkey):
        '''
        DOCSTRING: Function to decipher a given string using caesar cipher.
        \nINPUT: Any string and shiftkey.
        \nLOGIC: To decipher, it uses the basic formula : (character - shiftkey)
        \nOUTPUT: The deciphered string result.
        \nUSAGE: First import the CaesarCipher package; Then, create an instance of the class by using a variable to assign & call an instance of the class.
        \nSyntax: variable_name = CaesarCipher()
        \nThen create another variable to call either the caesar_encipher() method or caesae_decipher() method using two positional arguments : target word/variable, shiftkey
        \nSyntax: another_variable = variable_name.caesar_decipher("string",integer)
        \n\nThis logic uses ASCII code representation to convert the strings to integers. You can use any string, but this method will convert the string to lowercase and then decipher to maintain uniformity.
        '''
        word = word.lower()
        plaintext = []
        for w in range(len(word)):
            x = (ord(word[w]) - shiftkey)
            if x>=70 and x < 97:
                y = (x-96)+122
                plaintext.append(chr(y))
            elif ord(word[w]) == 32:
                plaintext.append(chr(32))
            else:
                plaintext.append(chr(x))
        word = ''.join([str(s) for s in plaintext])
        return word