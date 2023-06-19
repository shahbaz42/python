import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# raw string in python is a string prefixed with r
# raw string tells python interpreter not to handle backslashes in any special way

# search for a literal string (case senstive)
pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print(text_to_search[1:4]) # Output: abc
print()

# escape characters
pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print()

# search for any digit (0-9) using \d
pattern = re.compile(r'\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print()

# search for any non-digit (0-9) using \D
pattern = re.compile(r'\D')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print()

# search for any word character (a-z, A-Z, 0-9, _) using \w
pattern = re.compile(r'\w')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print()

# search for any non-word character (a-z, A-Z, 0-9, _) using \W
pattern = re.compile(r'\W')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print()

# search for any whitespace character (space, tab, newline) using \s
pattern = re.compile(r'\s')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print()

# search for any non-whitespace character (space, tab, newline) using \S
pattern = re.compile(r'\S')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print()

# search for word boundary using \b
pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print()

# search for non-word boundary using \B
pattern = re.compile(r'\BHa')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print()

# search for start of string using ^
pattern = re.compile(r'^Start') # searches for the literal string Start at the start of the string
matches = pattern.finditer(sentence)
for match in matches:
    print(match)
print()

# search for end of string using $
pattern = re.compile(r'end$') # searches for the literal string "end" at the end of the line.
matches = pattern.finditer(sentence)
for match in matches:
    print(match)
print()

# search for a phone number
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

#Opening data.txt
with open('data.txt', 'r', encoding='UTF-8') as f :
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches: 
        print(match)
print()

# Matching phone numbers with only . or - as separators
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')  # [] it is a character set
# Note : In character sets we don't need to escape special characters. Althoug they can be done
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print()

# matching 800 and 900 number
pattern = re.compile(r'[89]00[-.]\d\d\d[.-]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print()

# match digits of character range
pattern = re.compile(r'[1-5]') # it is equivalent to [12345]
matches = pattern.finditer(text_to_search)
for match in matches :
    print(match)
print()

# match uppercase or lowercase letters
pattern = re.compile(r'[a-zA-Z]')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
print()

# negation of a character set [^] Matches the characters not in the bracker
pattern = re.compile(r'[^a-z]') # matches every character except lowercase character
matches = pattern.finditer(text_to_search)
for match in matches :
    print(match)
print()

#Quantifiers

# match a character 0 or more times to find phone number
pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
matches = pattern.finditer(text_to_search)
for match in matches :
    print(match)
print()

# Match Mr. or Ms. or Mrs. or Mr
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') # | (r|s|rs) matches r or s or rs
matches = pattern.finditer(text_to_search)
for match in matches :
    print(match)
print()