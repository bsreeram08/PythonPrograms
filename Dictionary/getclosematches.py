from difflib import get_close_matches
word=input("\nEnter a word to find it's close one in dictionary:")
import json
data=json.load(open("data.json"))
print(get_close_matches(word,data.keys()))
