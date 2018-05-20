# comments start with a hash and space
'''
multiline comment (technically a string)
'''
# whitespace matters for conditionals, loops, and nesting
# declare variables
age = 28

name = 'Ryan Tomlinson'

# print out static text and variables -- concatenation
print('My name is', name, 'and my age is:', age)
# also works as...
print('Hello my name is {} and I am {}'.format(name, age))
# or you could declare a variable with the sentence and just print it
# out with print(sentence)
# tab to indicate what is inside the conditional
if age > 18:
    print('You are older than 18')
else:
    print('You are not older than 18')

todayiscold = False

if todayiscold == True:
    print('Brr. It\'s cold today')
else:
    print('its not cold at all today')