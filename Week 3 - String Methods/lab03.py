# Develop a Python program which will convert 
# English words into their Pig Latin form

VOWELS = "aeiou"
word = input("Enter a word ('quit' to quit): \n")
word.lower()
while (word.lower() != 'quit' ):
    if word == " ":
        print("Can't convert empty string.  Try again.")
    else:
        if word[0] in VOWELS:
            word += "way"
            print(word.lower())
        else:
            index = 0
            for i in (word):
                if i not in VOWELS:
                    index += 1
                else:
                    break
            newword = word[index:] + word[:index] + "ay"
            print(newword.lower())
    word = input ("Enter a word ('quit' to quit): \n")