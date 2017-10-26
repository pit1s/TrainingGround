# Simple print statement to console:
print('Hello World!')
# There are other ways output data with Python, but
# we'll focus on print() for now.


# Same concept, but letting the user choose what to say 'Hello' to:
thing = input('What should we say Hello to: ')
print('Hello ' + thing)
# Notice the space after 'Hello'. This is called concatenation, 
# we're adding one string 'Hello ' with whatever 'thing' is, 
# which is defined by whatever the user inputs


# We can also put the two together, without assigning a variable
print('My favorite food is ' + input('What is your favorite food? '))
# Notice that when this line is run, it will perform the input method first,
# then use the resulting string to finish the sentence.


# You can use concatenation to create more complex strings
name = input('What is your name? ')
quest = input('What is your quest? ')
color = input('What is your favorite color? ')
print('Your name is ' + name + '. Your quest is ' + quest + '. Your favorite color is ' + color +'.')


# You can use special characters to insert newlines (\n) or tabs (\t)
print('Your name is:\t' + name + '.\nYour quest is:\t' + quest + '.\nYour favorite color is:\t' + color +'.')


# You can also use \ to break up statements into multiple lines
print('Your name is:\t' + name \
    + '.\nYour quest is:\t' + quest \
    + '.\nYour favorite color is:\t' + color +'.')


# Note that using the backslash does not affect the strings themselves
print('This' + \
        'is' + \
        'one' + \
        'word')



