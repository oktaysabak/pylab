import re

sentence = 'My numbers are 415-555-4242 and 987-542-1234.'

pattern = r'([\d]{3}-[\d]{3}-[\d]{4})'
search_sentence = re.search(pattern, sentence) # for find first pattern
findall_sentence = re.findall(pattern, sentence) # find all pattern
sub_sentence = re.sub(pattern, '', sentence) # change pattern with ''
start, stop = search_sentence.span()
print(sentence)
print('--------------------------------')
for found in findall_sentence:
    print(found)
print('--------------------------------')
print(search_sentence)
print('--------------------------------')
print(search_sentence.group())
print('--------------------------------')
print(sub_sentence)
print('--------------------------------')