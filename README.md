# CaesarCipher
Python library to encipher &amp; decipher a string using one of the simplest Substitution ciphers - "Caesar's Cipher"

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence

This library contains an Encipher method and a Decipher method to encipher & decipher a string, respectively, using a shiftkey.


INSTALLATION: python -m pip install pycaesarcipher==1.3 (or) python -m pip install pycaesarcipher==1.4

USAGE : 
variable_name = CaesarCipher()
new_variable = variable_name.caesar_encipher("string",shiftkey)
another_variable = variable_name.caesar_decipher(new_variable,shiftkey)
print(new_variable)

EXAMPLE:

from pycaesarcipher import pycaesarcipher

word = pycaesarcipher()
new = word.caesar_encipher("i love python",12)
word2 = word.caesar_decipher("u xahq bkftaz",12)
print(new," is the enciphered text.\n")
print(word2," is the deciphered text.")


