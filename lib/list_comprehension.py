#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = []
    for num in num_list:
        #Check if the number is even
       if num % 2 == 0:
           #To append to the list a number is even
        even_numbers.append(num)
    return even_numbers

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(return_evens(sequence))        
pass

def make_exclamation(sentence_list):
    #To add an exclamation mark to each sentence in the list
    return [sentence + '!' for sentence in sentence_list]

sentences = ["Hello", "I'm doing great", "Python is fun"]
print(make_exclamation(sentences))
pass