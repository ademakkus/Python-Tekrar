sentence = input("Enter a sentence :")

numberOfWovels = 0
numberOfConsonants = 0
for i in range(len(sentence)):
	if sentence[i] == "a" or sentence[i] == "e" or sentence[i] == "i" or sentence[i]=="ı" or sentence[i]=="u" or sentence[i]=="ü" or sentence[i] == "o" or sentence[i]=="ö":
		numberOfWovels = numberOfWovels + 1
	else:
		numberOfConsonants = numberOfConsonants + 1
print(sentence, "number of vowels in a sentence =", numberOfWovels)
print(sentence, "number of consonants in a sentence =", numberOfConsonants)