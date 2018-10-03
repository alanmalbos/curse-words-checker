from urllib import urlopen
# defining a function to read the text to be check
def read_file():
	file = open("/home/alanmalbos/version-control/curse-words-checker/movie_quotes.txt")
	content_of_file = file.read()
	file.close()
	print(content_of_file)
	check_text(content_of_file)

# defining a function to check for profanity
def check_text(text_to_check):
	# connect to a site to check, it is response True or False
	connection = urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	connection.close()
	if output == "true":
		print("This text contains curse words!")
	else:
		print("Everything is OK!")

# call the firt function to test a text
read_file()