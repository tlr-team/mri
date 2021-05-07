from document import Document
from query import TestQuery
import json

def load_documents(self, path = '../datasets/', cisi = True):

    doc_path = path + if cisi "CISI" else "CRAN" + 'ALL.json'

    with open(doc_path, 'r') as docs:
        docs = json.load(docs)

    return [Document(docs[i]) for i in docs.keys()]

def load_queries(self, path = '../datasets/', cisi = True):

    qsp = path + if cisi "CISI" else "CRAN" + 'QRY.json'

    rlp = path + if cisi "CISI" else "CRAN" + 'REL.json'

    qs = []
    rl = []

    with open(qsp, 'r') as qsps:
        _qs = json.load(qsps)

        qs = [TestQuery(_qs[i]['text'], None) for i in _qs.keys()]

    with open(rlp, 'r') as rlps:
        rl = json.load(rlps)

        for key in rl.keys():
            val = int(key)

            qs[val].relevant_documents = []

            for doc in rl[key].keys():
                qs[val].relevant_documents.append(int(doc))

    return [q for q in qs if q.relevant_documents != None]

    


    