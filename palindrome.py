your_sentence = input("What do you want to test as a palindrome?").lower()

import re
cleared_sentence = re.sub (r'[^A-Za-z]', "", your_sentence)
print(cleared_sentence)

if len(cleared_sentence) <= 1:
            print("Is palindrome")




def match_alpha(cleared_sentence):
    """Each alphabet of the input is matched with the corresponding one in the input from the end in the reverse to find out if they are the same."""
    index = 0
    for index in range(int(len(cleared_sentence)/2)):  
        if cleared_sentence[index] != cleared_sentence [-(index + 1)]:
            return False
    return True
    
def print_sentence (cleared_sentence):
        if match_alpha(cleared_sentence):
            print("is a palindrome!!!") 
        else:
              print("is not a palindrome.") 
    
    
print_sentence(cleared_sentence)  