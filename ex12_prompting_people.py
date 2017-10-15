# prompting people
# actually we complete this part in ex11.py

# so here we lear that we can user character in raw_input() while taking some input form user

# means when your interprinter come to raw_input() code it inderstand that now we want some
# use input for programm, so it stop it's exicution and wait for your enter it's text and
# when your press enter then interpriter resume it's work take that input which is user added

# we can store that user responce in the variable and use it leter


print "ok now start the exercise"

y = raw_input("name ?")

print y

print "lets play a game"

print "are you ready?"

isReady = raw_input()

print isReady

print "ok tell me which programming language you love most?"

progAns = raw_input()

print "I am agree with you that %s is good programming language" %progAns

tellMe = raw_input("ok tell me about that...  ")

print "your point is : ", tellMe

likeEmma = raw_input("Do you like emma watson?")

print "Because I like her soooo much. and you %s like her" %likeEmma

if likeEmma == "yes":
 print "you are good"  # because i love her she is so beautifule. awwwwwww.....
else :
 print "then you are dumb :("

# have we notice we use if else statement and compare users response
# please try to use previouse exercise points in present exercise because using that
# we can lear more. 
# have you remember old age people said PRACTICE MAN MAKE PERFECT
# you here we are doing same thing ;)

# now lets check can we sore raw_input data as integer or only string

numb = input("lucky number :")
print "your lucky number %d store as int" %numb

# have you notice we use input() for store value as int
# but if you try below line code then you will get type error
# because it stored as string and we want pass value as int :(

# well I found this in below url
# https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-integers

#luckyNumber = raw_input("print your magical number:")
#print "so here we prove that we can store your magic number %d as integer" %luckyNumber








'''
# exercis of learn python hard way
name = raw_input("what is your name?")
age = raw_input("what is your age?")
height = raw_input("How tall are you?")
weight = raw_input("how much do you weight?")

print "so your name is %s, you are %s year old. you are %s tall and %s heavy" %(name, age, height, weight)
'''








