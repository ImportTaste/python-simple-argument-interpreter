def option(argv, optiontoparsefor):
	for i in range(1, len(argv)):
		if argv[i] == optiontoparsefor:
			return argv[i + 1]
def flag(argv, optiontoparsefor):
	for i in range(1, len(argv)):
		if argv[i] == optiontoparsefor:
			return True
	return False
def missingFlags(argv, optionstoparsefor):
	founds = 0
	for i in range(0, len(optionstoparsefor)):
		for o in range(1, len(argv)):
			if argv[o] == optionstoparsefor[i]:
				founds = founds + 1
	if founds == len(optionstoparsefor):
		return True
	return False

def missingOptions(argv, optionstoparsefor):
	founds = 0
	misc = "misc"
	for i in range(0, len(optionstoparsefor)):
		for o in range(1, len(argv)):
			if argv[o] == optionstoparsefor[i]:
				try:
					misc = argv[o + 1]
				except IndexError:
					return True
				founds = founds + 1
	if founds == len(optionstoparsefor):
		return False
	return True
