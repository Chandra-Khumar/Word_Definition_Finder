import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(w):
     w = w.lower()
     if w in data:
          return data[w]
     elif get_close_matches(w, data.keys()):
          return "Did you mean %s instead?"
     else:
          return "sorry doesnt match"

word = input('Enter word:')

print(translate(word))


























































