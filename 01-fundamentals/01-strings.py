message1 = 'Hello World'

#one of the way to handle single quotes in the string OR you can also use double quotes
message2 = 'Ashish\'s world'

#multi-line string can be created using triple quotes
message3 = '''
Hello
how
are
you?
'''

#getting length of the string
print(len(message1))

#getting charters of the string using index
print(message3[11])

#getting range of characters
print(message1[0:5])
#works in similar manner
print(message1[:5])

#this is called slicing, we will practice slicing exercises in a separate file

#convert the string to lower and upper case
print(message1.lower())
print(message1.upper())

#counts the occurance of characters in the message
print(message1.count('l'))

#return the index of word/ character within the string
print(message1.find('World'))

#returns -1 if it doesnot find the occurance
print(message1.find('z'))

#replaces with new word withing the string
message1 = message1.replace('World', 'Universe')
print(message1)

#concatenation

#fstrings

# returns help doc for str class
print(help(str))
print(help(str.lower))