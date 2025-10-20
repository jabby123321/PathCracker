import cmd
import pathEnnumeration

"""
- Take user input from command line
    - Input is single URL and a .txt word list (user defined)
- Validate the word list is real and isn't empty
- Validate that the URL is in the correct format (.com, .net, ect.)

pathCracker test_words.txt https://www.website.com/foo -> call ennumerateURL("test_words.txt", "website.com")

- Display list of strings from ennumerateURL
"""

def check_word_list(file: str):
    lines = open(file, "r").readlines()

    if not lines:
        return False
    else:
        return True
    
    lines.close()

def sanitise_url(url: str):
    # remove http(s)
    # remove ://
    # remove foo.
    # remove /foo
    return url

class PathCracker(cmd.Cmd):
    def do_pathCracker(self, line):
        words, url = line.split()
        if words and url:
            if check_word_list(words):
                sanitised_url = sanitise_url(url)
                cmd.Cmd.columnize(pathEnnumeration.ennumerateURL(words, sanitised_url))
        else:
            print("No URL and/or word list")
    
    def do_EOF(self, line):
        return True
    
    def postloop(self):
        print

if __name__ == '__main__':
    PathCracker().cmdloop()


