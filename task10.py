def commonLetters(string1, string2):
	common = ""
	for letter in string1:
		if letter in string2 and not common:
			if common == "":
				common = letter
			else:
				common = common + ", " + letter
	return common

commonLetters("Greetings", "Hello")
