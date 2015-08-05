imports urllib

def read_text():
        file_path = "/home/eric/Documents/Workspaces/Studio3/ProfanityChecker/movie_quotes.txt"
        quotes = open(file_path)
        contents_of_file = quotes.read()
        print(contents_of_file)
        quotes.close()
        check_profanity(contents_of_file)
        
def check_profanity(text_to_check):
        connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
        output = connection.read()
        print(output)
        connection.close()
        
read_text()
