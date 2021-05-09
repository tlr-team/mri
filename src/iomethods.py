from .document import Document
from .query import TestQuery
import json


def load_documents(path='../datasets/', dataset='CISI'):

    doc_path = path + dataset + '.ALL.json'

    with open(doc_path, 'r') as docs:
        docs = json.load(docs)

    return [Document(docs[i], text=(dataset == 'CISI')) for i in docs]


def load_queries(path='../datasets/', dataset='CISI'):

    qsp = path + dataset + '.QRY.json'

    rlp = path + dataset + '.REL.json'

    qs = []

    with open(qsp, 'r') as qsps:
        _qs = json.load(qsps)

        qs = [TestQuery(_qs[i]['text'], None) for i in _qs]

    with open(rlp, 'r') as rlps:
        rl = json.load(rlps)

        for key in rl:
            val = int(key)

            if val >= len(qs):
                continue

            qs[val].relevant_documents = []

            for doc in rl[key]:
                qs[val].relevant_documents.append(int(doc))

    return [q for q in qs if q.relevant_documents != None]

