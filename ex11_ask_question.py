# ask question to use and get input from them

print "Hi harin"

print "Hey tell me your name"

name = raw_input()

print "hello",name

print "what is your hobby?"

hobby = raw_input()

print "%s oh that's good" %hobby

print "tell me which os you like?"

os  = raw_input()

print "ohkay you like", os

age = raw_input("what is your age?")   # if your are girl then this question is not for you ;)
print "cool my age is also", age

# ok we can ase more questin in many ways like

prompt = ">"

print "do you like ice-cream?"

likeIceCreame = raw_input(prompt)

print "you %s ice-cream" %likeIceCreame

print "so your name is %s, and %s year old. you love %s, and you use %s operating system. which is cool. and you %s ice-cream" %(name, age, hobby, os, likeIceCreame)

print "we can take all type of value using raw_input()"

print "which movie do you like?"
print "1. Titanic"
print "2. The Dark Knight Rises"
print "3. Harry Potter"

movieNumber = raw_input("please enter your choice [1-3] : ")

print "ok now we check your knowladge ;)"

ansOne = raw_input("what is 2+2 = ")
print "you said %s" %ansOne



# big news in python 3.x raw_input() is change to input()
# but for now we use raw_input() >> python 2.7


