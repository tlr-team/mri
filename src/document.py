class Document:
    def __init__(self, doc, text=True):
        self.id = doc['id']
        self.Title = doc.get('title', '')
        source = 'text' if text else 'abstract'
        self.Desc = doc.get(source, '')
        self.author = doc.get('author', '')

    def __str__(self):
        return f'''
        Id: {self.id}
        Title: {self.Title}
        Author: {self.author}

        Content: {self.Desc}
        '''

    def __repr__(self):
        return self.__str__()

