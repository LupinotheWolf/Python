# This is a small programme I'm writing to test out basic strings, integers, and functions.
# The purpose of this is to check how many letters a word has that a user puts in.
# Written by Mattia 'Lupino' Ruta


# lets user input their name
name = raw_input("Okay, let's start! What is your name?")
exit == False

# asks how the user is doing today
print ("Oh, hello %s! How are you doing today?") % name
how_do = raw_input("Enter good or not good here!")
if how_do == 'good':
    print "That's great to hear!"
elif how_do == 'not good':
    print "oh no, i'm sorry to hear that!"
else:
    print "that's not a correct response!"

# First Segment
print "Anyway, let's get on with the programme! Type in a word and I'm going to tell you how many letters are in it!"
word = raw_input("Enter your word here:")
print "Great! Your word is", word, "and the number of letters it has is", len(word)
print "You used the programme! would you like to exit?"
exit_answer = raw_input("Enter y or n:")

if exit_answer == 'y':
    quit()
elif exit_answer == 'n':
    print "oh.. okay then."
