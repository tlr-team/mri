class Document:
    def __init__(self, doc):
        self.id = doc['id']
        self.Title = doc['title']
        self.Desc = doc['text']
        self.author = doc['author']

    def __str__(self):
        return f'''
        Id: {self.id}
        Title: {self.Title}
        Author: {self.author}

        Desc: {self.Desc}
        '''
    
    def __repr__(self):
        return self.__str__()

