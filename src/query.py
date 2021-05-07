
class TestQuery:

    def __init__(self, text, relevant_documents):
        self.query = text
        self.relevant_documents = relevant_documents

    def __str__(self):
        return f'''
        Query: {self.query}
        Documents: {self.relevant_documents}
        '''

    def __repr__(self):
        return self.__str__()
