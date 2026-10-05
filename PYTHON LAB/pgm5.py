s=input("Enter a sentence:")
print(s)
WordsList=s.split()
print(WordsList)
uniqueWords=set(WordsList)
for word in uniqueWords:
    print(f"{word}occurs{WordsList.count(word)}times")
