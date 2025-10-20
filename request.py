import requests

"""
Takes a url and determines whether path exists or does not exist
  returns 0 = nothing // 404
          1 = for directory // 301
          2 = for valid endpoint // 200
"""

def checkPath(endpoint: str) -> int:
  """converts endpoint to an int based on its status code"""
  
  httpGet = requests.get(f'{endpoint}') # gets the URL from the endpoint string

  match httpGet.status_code: # gets status code
    case (404 | 400): # if not present
      return 0
    case 301: # if directory
      return 1
    case 200: # if found
      return 2

