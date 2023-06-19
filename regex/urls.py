import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls) # this will remove the www. and the .com/.gov/.net

print(subbed_urls)

matches = pattern.finditer(urls)

for match in matches:
    print(match.group(0)) # group(0) is the entire match
    print(match.group(1)) # group(1) is the first group
    print(match.group(2)) # group(2) is the second group
    print(match.group(3)) # group(3) is the third group
    print()
