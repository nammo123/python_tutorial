para = input("Enter a Paragraph: ")
word = input("Enter word which you want to search in paragraph: ")

word_stripped_lower = word.strip().lower()   #convert word into lower and also did stripped
para_lower = para.lower()                    #convert para into lower

if(word_stripped_lower in para_lower):
    print("your word is in the paragaraph")
else:
    print("sorry your word is not in paragraph")
