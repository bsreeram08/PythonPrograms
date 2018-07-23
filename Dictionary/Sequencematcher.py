from difflib import SequenceMatcher
print("\nEnter two words to Compare Similarity:-")
word1=input("Word 1:")
word1=word1.lower()
word2=input("Word 2:")
word2=word2.lower()
match=SequenceMatcher(None,word1,word2).ratio()
match=match*100
print("These Words Match "+ str(match)+"% irrespective of their CASE!")
