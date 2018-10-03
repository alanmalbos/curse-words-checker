# defining a function to read the text to be check
def read_file():
	file = open("/home/alanmalbos/version-control/curse-words-checker/movie_quotes.txt")
	content_of_file = file.read()
	print(content_of_file)
	file.close()

read_file()