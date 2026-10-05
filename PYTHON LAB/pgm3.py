s=input("enter a sentence:")
print(s)
WordsList=s.split()
print(WordsList)
UniqueWords=set(WordsList)
for Word in UniqueWords:
    print(f"{Word} occurs {WordsList.count(Word)} times")
