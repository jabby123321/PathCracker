from typing import List

import request

"""takes a file object for wordlist and a url"""
def ennumerateURL(wordlist, url: str) -> List[str]:
  foundWords = []

  for word in wordlist.readline():
    match (request.checkPath(f"{url}/{word}")):
      case 0:
        continue
      case 1:
        foundWords.extend(ennumerateURL({url}/{word}))
      case 2:
        foundWords.append(f"{url}/{word}")


