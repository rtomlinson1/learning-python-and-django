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

year = 2101

# When you check your solution, don't change this number
# if year >= 2000 and year <= 2100:
# simplified to:
if 2000 <= year <= 2100:
    print('Welcome to the 21st Century!')
else:
    print('You are before or after the 21st century')

# functions:
# two blank lines before and after function declaration or use
# dont name your functions function!


def function(inputstring):
    print('Testing a function -' + inputstring)


function('success')


def getdeets(name1='Sir', age='1', job='engineer'):
    print('Hello, {}. You are a great {}, for a {} year old anyway...'.format(name1, job, age))


getdeets('Ryan', 28, 'Web Developer')


def trippleprint(input):
    print(input)
    print(input)
    print(input)


trippleprint('cheese')


# lists(arrays) listname = [item, item, item]

names = ['Ryan', 'Amy', 'Rosi', 'Mickey']

names.insert(1, 'Moosey')

print(names)
print(len(names))

names[4] = 'Mick'

print(names)


# loops
# with a list and for --- for name in names GOLD!!! so easy

for name in names:
    print(name)


# range of list


for x in range(1, 3):
    print(x)


# age = 28
# while loop while age < 40

num = 1
while num <= 10:
    print(num)
    num += 1


# dictionaries key : value

bikes = {'Release 1': 'Mountain', 'Century': 'Road', 'Century': 'Road2'}

print(bikes['Century'])
del(bikes['Century'])

print(bikes)

# newline at end of file
