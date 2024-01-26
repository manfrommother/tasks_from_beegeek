class TextHandler():

    def __init__(self):
        self.words_list = []

    def add_words(self, string):
        string = string.split()
        self.words_list += string

    def get_shortest_words(self):
        shorted = min(self.words_list, key=len)
        return [i for i in self.words_list if len(i) == len(shorted)]
    
    def get_longest_words(self):
        longest = max(self.words_list, key=len)
        return [i for i in self.words_list if len(i) == len(longest)]
    

texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())