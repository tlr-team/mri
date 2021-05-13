from json import dumps


class Document:
    def __init__(self, doc, text=True):
        self.id = doc.get('id', '')
        self.title = doc.get('title', '')
        source = 'text' if text else 'abstract'
        self.content = doc.get(source, '')
        self.author = doc.get('author', '')

    def toJson(self):
        dic = {}
        dic['id'] = self.id
        dic['title'] = self.title
        dic['author'] = self.author
        dic['content'] = self.content
        return dumps(dic, indent=True)

    def __str__(self):
        return f'''
        Id: {self.id}
        Title: {self.title}
        Author: {self.author}

        Content: {self.content}
        '''

    def __repr__(self):
        return f'''
        Id: {self.id}
        Title: {self.title}
        Author: {self.author}
        '''

