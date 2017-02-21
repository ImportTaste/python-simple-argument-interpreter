def option(argv, optiontoparsefor):
	found = False
	for i in range(1, len(argv)):
		if argv[i] == optiontoparsefor:
			return argv[i + 1]
def flag(argv, optiontoparsefor):
	found = False
	for i in range(1, len(argv)):
		if argv[i] == optiontoparsefor:
			found = True
		return found
