# -*- coding: utf-8 -*-
### Scratch work for learning purposes

# ##------------------------
# ## Learning how to save objects
# ##-------------------------
# fh = open("junk.txt", "w")
# fh.close()

# content = fh.read()
# content = fh.readlines() ## returns list each line
# print content.rstrip()

# fh = open("hello.txt","w")

# write("Hello World")

# fh = open("hello.txt", "w")

# lines_of_text = ["a line of text", "another line of text", "a third line"]

# fh.writelines(lines_of_text)


# ##------------------
# ## Saving Lists to CSV
# ##----------------------

# from numpy import arange

# list1 = arange(1,50,2)
# list2 = arange(0,250,10)
# list3 = arange(150, 0, -6)


# replicate = 1

# with open('output_data' + str(replicate) + '.csv', 'w') as out_file:
# 	for i in range(len(list1)):
# 		out_string = ''
# 		out_string += str(list1[i])
# 		out_string += ',' + str(list2[i])
# 		out_string += ',' + str(list2[i])
# 		out_string += '\n'
# 		out_file.write(out_string)


# ##------------------
# ## Unicode
# ##-----------------

# uni_greeting = u'Hi, my name is %s.'
# utf8_greeting = uni_greeting.encode('utf-8')

# uni_name = u'José'
# utf8_name = uni_name.encode('utf-8')

# 	## Pluggine Uni to Uni is fine
# uni_greeting % uni_name

# 	## Plugging utf-8 to utf-8 is fine
# utf8_greeting % utf8_name

# 	## Pluggig Uni into a utf-8 is fine
# utf8_greeting % uni_name ## utf-8 invisibly decoded into Unicode
# print(type(utf8_greeting % uni_name))


# 	## BUT plugging utf-8 into Uni doesn't work
# uni_greeting % utf8_name ## no invisible decoding

# 	## Fix
# uni_greeting % u'Bob'.encode('utf-8')
# print(type(uni_greeting % u'Bob'.encode('utf-8')))


# # Well, you can interpolate utf-16 into utf-8 because these are just byte sequences
# utf8_greeting % uni_name.encode('utf-16')  # But this is a useless mess




##--------------------------
## Open files
##-------------------------
import csv

add = 'P:\QAC\Projects\datadive17\NotAnAccident\Fred_files\ManualGeoLoc1228_clean.csv'
# file = r'P:/QAC/Projects/datadive17/NotAnAccident/Fred_files/MaryHadALittleLamb.txt'
# print file
# f = open(file, 'r')
# print f.read()		

# f.close()

# with open(file) as f:
# 	att = csv.DictReader(f)
# 	for row in att:
# 		print row['USPS'], row['County'], row['Places']

att = open(add, 'r').read()
print att
