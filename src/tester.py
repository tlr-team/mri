from .iomethods import load_queries, load_documents
from .metrics import *
from time import clock
from mri import IRM

class Tester:

    def __init__(self, dataset = 'CRAN', top=10, irm = IRM()):
        self.presicion = 0
        self.recall = 0
        self.f1 = 0
        self.r_presicion = 0
        self.fallout = 0
        self.timing = 0
        self.dataset = dataset
        self.irm = irm
        self.top = 10

    def test_dataset(self):
        t = load_documents(dataset=self.dataset)

        qs = load_queries(dataset=self.dataset)

        n = len(t)

        self.irm.reset()

        for d in t:
            self.irm.add(d)

        for q in qs:
            start = clock()
            relevants = q.relevant_documents

            qvector = self.irm.build_query_vector(q.query)

            rank = self.irm.get_query_ranking(qvector)
            end = clock()

            self.timing += end - start

            all = [i for (i,_) in rank]
            rall = [i for (i,_) in rank[0:self.top]]
            RRR = len([i for i in rall if i in relevants])
            #RR = len([i for i in all if i in relevants])
            RI = len([i for i in all if i not in relevants])
            NR = len(relevants) - RRR
            RRI = len([i for i in all if i not in relevants])
            RNI = n - len(relevants)

            self.presicion += precision(RRR, RI)
            self.recall += recall(RRR, NR)
            self.f1 += F1(RRR, RI, NR)
            self.r_presicion += r_precision(RRR, RRI)
            self.fallout += fallout(RRI, RNI)

        self.presicion /= len(qs)
        self.recall /= len(qs)
        self.f1 /= len(qs)
        self.r_presicion /= len(qs)
        self.fallout /= len(qs)
        self.timing /= len(qs)


    def __str__(self) -> str:
        return f'''
        Presición: {self.presicion}
        Recobrado: {self.recall}
        F1: {self.f1}
        R-Presición: {self.r_presicion}
        Fallout: {self.fallout}
        Tiempo promedio por consulta: {self.timing}
        '''

    def __repr__(self) -> str:
        return self.__str__()

        


