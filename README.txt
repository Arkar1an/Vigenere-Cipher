Russell Richardson
Homework 2

Problem one can be called by running main() in "vigenerecipher.py" and problem two can be called by running main() in "vigeneredecipher.py" 

The relevant text files are included in the zipped folder. "message.txt" can be edited with a text editor and when the .py files are run, the other text files will be changed.

I decided to use the stratedgy on vigenere ciphers wikipedia page under the algebraic decription heading:

https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

Basically I made a string of the alphabet called "alphabet", and at each index of the message I used .find() to get an index of the alphabet and an index of the letter in the key phrase at key_index which is initially zero (first index of the key phrase). This effectively turned the letters into numbers which I then used the modulus operator on to get an encrypted index within the string "alphabet" for the new encrypted message. This process is skipped if the index of the message is a space or a symbol like a period or comma. Key_index is incremented for each consecutive valid letter. Once the key_index equaled the keys length, it would be reset back to zero.

This same process is used for decrypting the message except subtraction of
the indices is used to get the clear text.
