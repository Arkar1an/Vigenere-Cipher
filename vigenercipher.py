# Russell RIchardson
# Homework 2, problem 1

"""This reads from a text file and returns a string of the text"""
def read_from_a_file(the_file):
    file=open(the_file,'r')
    the_string=file.read()
    file.close()
    return the_string

"""This takes in a string and writes that string to a text file"""    
def write_to_a_file(message, the_file):
    file = open(the_file,"w")
    file.write(message)
    file.close()
    
"""Call main to run the main program"""
def main():
    
    the_file = r"message.txt"
    message = read_from_a_file(the_file)
    print(message)
    key = input("Enter a key for the cipher: ")
    
    encrypted_message = encrypt(key,message)
    print(encrypted_message)
    new_file = the_file[:-4]
    new_file = new_file + "-cipher.txt"
    
    write_to_a_file(encrypted_message,new_file)
   
"""This encrypts the message, given a key"""
def encrypt(key,message):
    encrypted_message = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_index = 0
    key = key.lower()
    
    for symbol in message:
        encrypted_index = alphabet.find(symbol)
        if encrypted_index != -1:
            encrypted_index += alphabet.find(key[key_index])
            
            encrypted_index %= len(alphabet)
        
            if symbol.islower():
                encrypted_message += alphabet[encrypted_index]
            elif symbol.isupper():
                encrypted_message += alphabet[encrypted_index].upper()
            
            key_index += 1
            if key_index == len(key):
                key_index = 0
        
        else:
            encrypted_message += symbol
            
    return encrypted_message
