#how to reverse a string 
#1. using indexing
#2. using for loop
#3. using reverse and join

my_string = "Hello Nobita this is DYPIEMR ENTC"

#1. using indexing
reversed_string = my_string[::-1]
print(reversed_string)
#2. using for loop
reversed_string = ""
for i in my_string:
    reversed_string = i + reversed_string
print(reversed_string)
#3. using reverse and join
reversed_string = ''.join(reversed(my_string))
print(reversed_string)