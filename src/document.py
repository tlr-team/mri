class Document:
    def __init__(self, doc, cisi=True):
        self.id = doc['id']
        self.Title = doc['title'] if 'title' in doc.keys() else ""
        source = 'text' if cisi else 'abstract'
        self.Desc = doc[source] if source in doc.keys() else ""
        self.author = doc['author'] if 'author' in doc.keys() else ""

    def __str__(self):
        return f'''
        Id: {self.id}
        Title: {self.Title}
        Author: {self.author}

        Desc: {self.Desc}
        '''
    
    def __repr__(self):
        return self.__str__()

