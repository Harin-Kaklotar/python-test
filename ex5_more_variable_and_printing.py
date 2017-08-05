# more variable and printing
# here we use some int, string, char variable


print "hello welcome with more variable and printing excersice"

name = 'Harin'
middle_name = 'S'
surname = 'Kaklotar'
age = 25   # year
height = 74  # cm
weight = 52 # kg 
eyes_color = 'Black'
hair = 'Black and Silky'
teeth = 'White'

print name
print middle_name
print surname
print age

print "Hello", name
print "how are you",name, "?"
print "Let's talk about", name
print name, "Is %d inches tall." %height	# %d use for int type value
print "He's %d kg heavy." %weight
print "He's got %s eyes and %s hair." %(eyes_color, hair)   # %s use for string type value  and () use for using multiple value at same time
print "His teeth are usually %s" %teeth 

# tricky line
print "If I add %d, %d and %d I get %d" %(age, height, weight, age+height+weight)  # print line with using math operations


#note: we can use %r instedof %d and %s only while development time
