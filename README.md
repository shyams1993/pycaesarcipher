# CaesarCipher
Python library to encipher &amp; decipher a string using one of the simplest Substitution ciphers - "Caesar's Cipher"

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence

This library contains an Encipher method and a Decipher method to encipher & decipher a string, respectively, using a shiftkey.


<b>INSTALLATION</b>: python -m pip install pycaesarcipher==1.3 (or) python -m pip install pycaesarcipher==1.4

<b>ALGORITHM :</b> 
Import the module<br>
Create an instance of the class<br>
call the function "encipher" or "decipher" as an object along with the instance of the class<br>

<b>USAGE :</b> 
variable_name = CaesarCipher() <br>
new_variable = variable_name.caesar_encipher("string",shiftkey) <br>
another_variable = variable_name.caesar_decipher(new_variable,shiftkey) <br>
print(new_variable) <br>

<b>EXAMPLE PROGRAM:</b><br>
<code>from pycaesarcipher import pycaesarcipher<br></code>
<code>word = pycaesarcipher()<br></code>
<code>new = word.caesar_encipher("i love python",12)<br></code>
<code>word2 = word.caesar_decipher("u xahq bkftaz",12)<br></code>
<code>print(new," is the enciphered text.\n")<br></code>
<code>print(word2," is the deciphered text.")<br></code>
