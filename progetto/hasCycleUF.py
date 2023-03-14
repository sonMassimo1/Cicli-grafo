from progetto.unionfind.quickUnion import QuickUnion as UnionFind
from progetto.creagrafi import grafociclo, grafoaciclo
from time import time
"""
def hasCycleUF(graph):  #senza iteratore
    uf = UnionFind()
    for i in range(len(graph.nodes)):
        uf.makeSet(graph.nodes[i])
    uf.print()
    edges=graph.getEdges()
    for edge in edges:
        r1 = uf.findRoot(uf.nodes[edge.head])
        r2 = uf.findRoot(uf.nodes[edge.tail])
        if r1 == r2:
            print("C'è il ciclo")
            return True
        else:
            uf.union(r1, r2)
    print("Non c'è il ciclo")
    return False
"""

def timerUF(func):
    """
    Decorator che calcola il tempo di esecuzione della funzione
    :param func:
    :return: funzione di wrap
    """
    def wrapping_function(*args, **kwargs):
        start = time()
        value = func(*args, **kwargs)  # chiamata alla funzione da decorare
        elapsed = time() - start
        file = open("risultatiHasCycleUF.txt", "a")
        tempo="\tt:\t"+str(elapsed)
        input="\nn:\t"+str(n)
        file.write(input)
        file.write(tempo)
        file.close()
        print(f'Function {func.__name__} with args {args} took {elapsed} seconds')
        return value
    return wrapping_function

@timerUF
def hasCycleUF(graph, n):  #con iterator
    uf = UnionFind()
    for i in range(len(graph.nodes)):
        uf.makeSet(graph.nodes[i])
    uf.print()
    edges=graph.getEdges()
    i=0
    j=1
    it = Iterator()
    for i in range(0,len(edges)):
        a = next(it)
        r1 = uf.findRoot(uf.nodes[edges[a].head])
        r2 = uf.findRoot(uf.nodes[edges[a].tail])
        if r1 == r2:
            print("C'è il ciclo")
            return True
        else:
            uf.union(r1, r2)


    print("Non c'è il ciclo")
    return False

class Iterator():
    """
    Iterator dei numeri di Fibonacci
    """
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        v = self.prev
        self.prev=self.curr
        self.curr+=1

        return v


if __name__=="__main__":
    n=150
    #grafo=grafociclo(n)
    grafo=grafoaciclo(n)

    hasCycleUF(grafo, n)
