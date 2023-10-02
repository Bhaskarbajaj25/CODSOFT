
import random

def generate_password(length):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
    
    characters = digits + lower + upper + symbols
    passwd = ''
    
    if length <= 0:
        print("Invalid input. Password length should be a positive number.")
        return None
    
    for i in range(length):
        passwd += str(random.choice(characters))
    
    return passwd

length = int(input("Please enter the length of your password: "))

generated_password = generate_password(length)

if generated_password:
    print("Generated Password:", generated_password)
