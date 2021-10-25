import string
import random

def textstrip(filename):
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letters!
    '''
    # 
    final = ""
    # opening and reading file
    f = open(filename)
    s = f.read()

    s = s.lower() 

    allowed = "abcdefghijklmnopqrstuvwxyz"

    # we compare if a character in s string is in allowed string or not
    for character in s:
        if character in allowed:
            final += character
    

    return final

def generate_caesar_substituion_dictionary(key):
    """
    This function generates a substitution dictionary for caesar cypher
    by shifting letters by key position.
    """
    d = {}
    alpha = string.ascii_lowercase
    for ch in alpha :
        d[ch] = alpha[(alpha.index(ch)+key+26)%26]
    return(d)


def letter_distribution(s):
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''
    letter_dist = {}

    for c in s :
        if c in letter_dist :
            letter_dist[c] += 1

        else:
            letter_dist[c] = 1

    return letter_dist



def substitution_encrypt(s,d):
    '''encrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''

    final = ""

    for c in s:
        final += d[c]
    
    return final



def substitution_decrypt(s,d):
    '''decrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''

    final = ""
    dec = {}

    for key in d :
        dec[d[key]] = key

    for c in s:
        final += dec[c]
    
    return final



def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution (Caesar) cipher, predict the d'''

    alpha = string.ascii_lowercase
    d = {}

    # First we find the most frequent letter
    distribution = letter_distribution(s)
    max_freq = 0
    max_freq_letter = ""
    for i in distribution :
        if distribution[i] > max_freq :
            max_freq = distribution[i]
            max_freq_letter = i
    
    # This data comes from Wikipedia
    max_freq_letter_english = 'e'

    # print(max_freq_letter, max_freq_letter_english)
    # This is the difference between the max_freq_letter_english 
    index_diff = alpha.index(max_freq_letter_english) - alpha.index(max_freq_letter)

    for ch in alpha :
        d[ch] = alpha[((alpha.index(ch)-index_diff)+26)%26]

    return d
