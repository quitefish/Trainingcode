# how to find character in string and count it
my_string = "This is DYPIEMR ENTC"
print(my_string.count('E'))
count = 0
char_to_search = 'E'
for i in my_string:
    if i == char_to_search:
        count += 1

        ##### count char in string using counter
from collections import Counter
char_to_search = '1'
count = Counter(my_string)
print(count[char_to_search])