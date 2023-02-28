import re
# Example

# string = 'The quick brown fox jumps over the lazy dog.'

# The search() method returns a match object if there is a match anywhere in the string. If there is more than one match, only the first occurrence of the match will be returned.
# search = re.search(r'fox', string)
# print(search)  # <re.Match object; span=(16, 19), match='fox'>

# (16, 19)    # returns a tuple containing the start-, and end positions of the match.
# print(search.span())
# print(search.start())  # 16   # returns the start position of the match.
# print(search.end())  # 19   # returns the end position of the match.
# fox   # returns the part of the string where there was a match. THis is more useful when there's a multiple search.
# print(search.group())
# print(re.search('Fox', string))  # None   # returns None if no match was found.


# The compile() method returns a regex pattern object, which can be used to match all occurences of a pattern.
# pattern = re.compile('fox')
# print(pattern.search(string))  # <re.Match object; span=(16, 19), match='fox'>


# The findall() method returns a list of strings containing all matches.
# print(pattern.findall(string))

#  The match() method returns a match object if the text matches the pattern. If there is more than one match, only the first occurrence of the match will be returned.
# print(pattern.match(string))  # None   # returns None if no match was found.


# Regular Expression Character

# pattern = re.compile(r"([a-zA-Z]).([a])")
# string = 'Hey how are you!'

# # r - raw string
# # . - any character except newline
# # () - capturing group
# # [a-zA-Z] - any lowercase letter
# # [a] - any vowel

# search_re = pattern.search(string)
# print(search_re.group())


# Example
#  Validate email address using regex
pattern = re.compile(
    r"([a-zA-Z0-9.-]+)@([a-zA-Z-]+)\.([a-zA-Z]{2,5})")  # r - raw string
email = 'thisisjustatestemail@gmail.com'
valid_email = pattern.search(email)
print(valid_email.group())


# Example
#  Validate phone number using regex
pattern = re.compile(r"([0-9]{3})-([0-9]{3})-([0-9]{4})")
phone_number = '234-814-529-0260'
valid_phone_number = pattern.search(phone_number)
print(valid_phone_number.group())


# Example
#  Validate password using regex (password must be at least 8 characters long)

# pattern = re.compile(r"([a-zA-Z0-9@#$%^&+=]{8,})")
# pattern = re.compile(r"[A-Za-z0-9@#$%&!]{8,}\d") # password must be at least 8 characters long and must end with a digit
password = 'Passw@#12'
pattern = re.compile(r"[A-Za-z0-9@#$%&!]{8,}")
# fullmatch() - returns a match object if the string matches the pattern
try:
    valid_password = pattern.fullmatch(password)
    print(valid_password.group())
except AttributeError:
    print('Invalid password. Password must be at least 8 characters long')


# 4. Validate URL using regex

url = 'https://dev.to'
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
valid_url = pattern.fullmatch(url)
valid_url2 = pattern.search(url)
print(valid_url.group())
print(valid_url2.group())
