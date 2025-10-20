"""
Pathcracker - webserver resource search tool

usage:
pathcracker [URL] [Wordlist]
  \\->pathcracker will find all resources on given URL where their path is a permitation of words found in the wordlist

additional options
-e --extensions-list -> specify a wordlist of extensions which will be added to the end of words from the wordlist 
"""

import sys
from typing import List

from pathEnnumeration import ennumerateURL

def main(args: List[str]):
  ennumerateURL(args[1], args[2])

if __name__ == "__main__":
  main(sys.argv)

