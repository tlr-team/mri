import spacy
import math
from stopWords import stop_words
from document import Document


class Indexer:
    def __init__(self):
        self.terms = set()

    def contains(self, elem):
        return elem in self.terms

    def add(self, term):
        self.terms.add(term)

    def __getitem__(self, key):
        for i, term in enumerate(self.terms):
            if term == key:
                return i
        return -1


class MIR:
    def __init__(self):
        self.reset()

    def reset(self):
        self.nlp = spacy.load("en_core_web_lg")
        self.index = Indexer()
        self.freqij = []
        self.idfi = []
        self.documents = []
        self.N = 0

    def tfij(self, index, doc, freq=None):
        return (
            self.freqij[index][doc]
            / max([self.freqij[i][doc] for i in range(len(self.index.terms))])
            if freq == None
            else freq
        )

    def idfi(self, term):
        return math.log(self.N / self.idfi[term])

    def text_words(self, source):
        words = []

        _doc = self.nlp(source)

        # get keywords
        for np in _doc.noun_chunks:
            for word in np.split(' '):
                if word != None and word != '' and word not in stop_words:
                    words.append(word)

        return words

    def add(self, doc):

        self.documents.append(doc)
        self.N += 1

        text = doc.Title + doc.Desc

        words = self.text_words(text)

        n = len(self.index.terms)

        # add new document row
        for i in range(n):
            self.freqij[i].append(0)

        for word in words:
            if self.index.contains(word):
                i = self.index[word]

                self.idfi[i] += 1
                self.freqij[i][N - 1] += 1

            else:
                self.index.append(word)
                self.idfi.append(1)
                self.freqij.append([0] * N)
                self.freqij[len(self.index.terms) - 1] = 1

    def run_query(self, query, top=10):
        ranking = []

        q = self.build_query_vector(query)

        n = len(self.index.terms)

        for i in range(self.N):
            w = self.build_document_vector(i)

            term1 = sum([w[k] * q[k] for k in range(n)])
            term2 = math.sqrt(sum([w[k] ** 2 for k in range(n)]))
            temr3 = math.sqrt(sum([q[k] ** 2 for k in range(n)]))

            ranking.append((i, term1 / (term2 * temr3)))

        ranking.sort(lambda x: -1 * x[1])

        return ranking

    def build_query_vector(self, query):
        words = self.text_words(query)

        wdict = {}

        for word in words:
            if word in self.index.terms:
                if word in wdict:
                    wdict[word] += 1
                else:
                    wdict[0] = 1

        values = []

        for (_, value) in wdict.items():
            values.append(value)

        _max = max(values)

        vector = [0] * len(self.index.terms)

        for word in wdict.keys():
            i = self.index[word]

            vector[i] = (0, 4 + 0.6 * wdict[word] / _max) * self.idfi(word)

        return vector

    def build_document_vector(self, doc_indx):
        n = len(self.index.terms)
        max_freq = max([self.freqij[i][doc_indx] for i in range(n)])

        vector = [self.idfi(i) * self.tfij(i, doc_indx, max_freq) for i in range(n)]

        return vector

