# python string literal and much more

"""

"""

#print "I am 6'2" tall"     # try this it will give you invalid syntax error :(
# well we want to print 6'2" 
# but it give error because interpreter find 'print' so it think ok find what ever in between ""
# but when it start "I am 6'2" there interpreter print and go ahed then it fount tall which is without 
# opening and closing double qutoe and then error error error hahahahahaha
# for that we use string literals

print "I am 6'2\" tall"

# and also for signle quote also
print 'I am 6\'2" tall'

# now we use some other string literals 
tabed_string = "\tHi we just use tab"
print tabed_string

new_line_string = "Long long time ago\nthere lived a beautiful girl named cinderella"
print new_line_string

print """
Long, long time ago, there lived a beautiful girl named Cinderella.\nBecause her parents passed away, she lived with her step mother and step sister.
Cinderella was very sad every day because she had to do the house work alone.\nOne day, the king wanted to find the wife for his son.
\t* He invited all the beautiful girls to come.
\t* Cinderella was very sad because her step sister did not let her go.
\t* Her sister went to the palace without Cinderella. Luckily, The Angel came and helped Cinderella to go to the palace.
\t* In the palace, Cinderella danced with the prince. 
He fell in love with her;\n\tthen he married her.
They lived happily ever after....
"""


print "Oh I just love happy ending :*"


print "use of back slash>>> C:\\Users\\Harin\\Desktop\\ex9_print_print_print.py "
print "use of single quote : She\'s so beautiful"
print "use double quote>> prince:\"I love you Cinderella\""
print "Well really I don\'t know use of this\aBELL, which you can hear" #\a use for ASCII bell(BEl)
print "" #\\ use for Backslash(\)
print "" #\' use for Single-quote(')
print "" #\" use for Double-quote(")
print "" #\b use for ASCII backspace (BS)
print "" #\f use for ASCII formfeed (FF)
print "" #\n use for ASCII linefeed(LF)
print "" #\N{name} use for character named name in Unicode database (Unicode only)
print "" #\r use for ASCII carriage return (CR)
print "" #\t use for ASCII horizontal tab (TAB)
print "" #\uxxxx use for Character with 16 bit gex valuse xxxx (Unicode only)
print "" #\Uxxxxxxxx use for Character with 32 bit hex valuse xxxxxxxxxx (Unicode only)
print "" #\v use for ASCII vertical tab (VT)
print "" #\ooo use for Character with ictal valuse oo
print "" #\xhh use for Character with hex value


#note : If you found anything wrong please refer 'Learn python the hard way' by zed show
