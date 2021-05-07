class Document:
    def __init__(self, doc):
        self.id = doc['id']
        self.Title = doc['title']
        self.Desc = doc['text']
        self.author = doc['author']

