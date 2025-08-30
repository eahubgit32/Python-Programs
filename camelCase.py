import re

def to_camel_case(s):

    if not s:
        return ""
    words = re.split(r'[-_ ]+', s)

    camel_case_words = [words[0].lower()]
    for word in words[1:]:
        if word:  
            camel_case_words.append(word.capitalize())
    return "".join(camel_case_words)

s = 'hello world'
print(to_camel_case(s))

** end of main.py **

