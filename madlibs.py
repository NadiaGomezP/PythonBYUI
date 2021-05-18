# WEEK 2 Mad Libs
print('Please enter the following words: ')

print()

adj = input('Adjective: ')
animal = input ('Animal: ')
verb = input('Verb: ')
exc = input('Exclamation: ')
verb2 = input('Verb: ')
verb3 = input('Verb: ')
name = input('Insert your name: ')

print('\nYour story is: \n')

print('The other day, I was really in trouble. It all started when I saw a very\n' 
+f'{adj.lower()} {animal.lower()} {verb.lower()} ' 
+ 'down the hallway. ' +f'"{exc.capitalize()}!" ' + 'I yelled. But all\nI could think to do was to ' 
+ verb2.lower() + ' over and over. Miraculously, \nthat caused it to stop, but not before it tried to '
+ verb3.lower() + '\nright in front of my family.') 

print()

# This is to make the person writing part of the story.
print('Yay ' + name.capitalize() + '! That was a great story.' )