# printing printing

# this all examples are base on book 'Learn python The Hard way'
# and I add some extra examples on my own
# here we are using python v 2.7

formator = "%r"

print formator

# it will print %r

#but if we vant pass some valuse so what should we do?? let's see

print formator %'Hello Harin'			# string value
print formator %"Hello everyone"		# string value
print formator %5						# int value
print formator %True					# 
# print formator %and                   # if we write this line it will give 'invalid syntax' error because and is reserve key word
# if we want to print and we have to use signle or double quote
print formator %'and'

# if we write code like below then we must pass only number value
int_formator = "%d"

print int_formator
#print int_formator %"Hello harin"     # this will give you erro, here you can pass only numbers not string
print int_formator %24                 # this is my age  ;)

# now we pass more than one value
more_value = "%r %r %r"
print more_value

print more_value %("Hii", 24, True)  # we can pass any type of value because we use %r
print "Hello harin",more_value %("How","are","you?")
print "Numbers", more_value % (1, 2, 3)
# here this will give you error : not enough arguments for format string
# that means we have to pass 3 argument as we defime
# no argument more, no argument less
#print "Numbers", more_value %(1,2)    # just uncommnet it any thy this :)
print "booleans", more_value %(True, False, True)
print more_value %(more_value, more_value, more_value)

print more_value %(
	"Hello basically I am Android developer",
	"and now I am learning python",
	"because I found it halasdf amazing"
	)

# try your self another arguments and another data types like %s %d etc..
# %r is use for getting debugging information about something. 
# %r print as you write
# practice paractice practice