from typing import List

import request

"""takes a file object for wordlist and a url"""
def ennumerateURL(wordlist: str, url: str) -> List[str]:
  wordlistFile = open(wordlist)

  foundWords = []

  for word in wordlistFile:
    word = word.strip()
    print(f"{url}/{word} -> {request.checkPath(f"{url}/{word}")}")
    match (request.checkPath(f"{url}/{word}")):
      case 0:
        continue
      case 1:
        foundWords.extend(ennumerateURL(wordlist, f"{url}/{word}"))
      case 2:
        foundWords.append(f"{url}/{word}")
  
  return foundWords