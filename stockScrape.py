import urllib
import re

symbolfile = open("Symbols.txt")

symbolslist = symbolfile.read().split()



newsymbolslist = symbolslist
print newsymbolslist


i = 0
while i < len(newsymbolslist):
	url = "http://finance.yahoo.com/q?s=" + newsymbolslist[i] + "&fr=uh3_finance_web&uhb=uhb2"
	htmlfile = urllib.urlopen(url) # Opens the url that's handed in
	htmltext = htmlfile.read() # Reads the file and converts to text
	regex = '<span id="yfs_l84_[^.]*">(.+?)</span>' # regex finds the part of the text we want via (.+?)
	pattern = re.compile(regex) # must compile regex before implementation
	price = re.findall(pattern,htmltext) # passes in compiled regex "pattern" and the text it comes from "htmltext"
	print "The price of ", newsymbolslist[i], " is ", price
	i += 1
