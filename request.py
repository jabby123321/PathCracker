import requests
import sys

"""
Takes a url and determines whether path exists or does not exist
  returns 0 = nothing // 404
          1 = for subdirectory // 301
          2 = for valid endpoint // 200
"""

def checkPath(endpoint: str) -> int:
  """converts endpoint to an int based on its status code"""
  
  httpGet = requests.get(f'http://{endpoint}') 

  match httpGet.status_code: 
    # Nothing
    case (404 | 400):
      return 0
    # subdirectory
    case 301:
      return 1
    # valid endpoint
    case 200:
      return 2
    # code not implemented
    case _:
      sys.stderr.write(f"{endpoint} responded with code {httpGet.status_code} - ignored")
      return 0