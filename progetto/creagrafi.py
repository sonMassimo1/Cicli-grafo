from progetto.graph.Graph_AdjacencyList import GraphAdjacencyList
from time import time

def timerDfs(func):
    """
    Decorator che calcola il tempo di esecuzione della funzione
    :param func:
    :return: funzione di wrap
    """
    def wrapping_function(*args, **kwargs):
        start = time()
        value = func(*args, **kwargs)  # chiamata alla funzione da decorare
        elapsed = time() - start
        file = open("risultatihascycleDfs.txt", "a")
        tempo="\tt:\t"+str(elapsed)
        input="\nn:\t"+str(n)
        file.write(input)
        file.write(tempo)
        file.close()
        print(f'Function {func.__name__} with args {args} took {elapsed} seconds')
        return value
    return wrapping_function


def grafociclo(n):
    graph = GraphAdjacencyList()

    graph.print()

    nodes = []
    for i in range(n):
        node = graph.addNode(i)
        print("Node inserted:", node)
        nodes.append(node)

    graph.print()

    for node_src in nodes:
        for node_dst in nodes:
            if node_src != node_dst:
                print("---")
                print("Adjacent nodes {},{}: {}"
                      .format(node_src.id, node_dst.id,
                              graph.isAdj(node_src.id, node_dst.id)))
                graph.insertEdge(node_src.id, node_dst.id,
                                 node_src.id + node_dst.id)
                print("Edge inserted: from {} to {}".format(node_src.id,
                                                            node_dst.id))
                print("Adjacent nodes {},{}: {}"
                      .format(node_src.id, node_dst.id,
                              graph.isAdj(node_src.id, node_dst.id)))
                graph.print()
                print("---")

    print("Num Nodes:", graph.numNodes())
    print("Num Edges:", graph.numEdges())
    return graph


def grafoaciclo(n):
    graph = GraphAdjacencyList()
    nodi=[]
    for i in range(0,n+1):
        nodo=graph.addNode(i)
        nodi.append(nodo)
    for j in range(1, n+1):
        graph.insertEdge(nodi[j-1].id, nodi[j].id)
        #graph.insertEdge(nodi[j].id,nodi[j-1].id)
    graph.print()
    return graph

@timerDfs
def hasCycleDFS(grafo, n):
    grafo.hasCycleDfs(0)  #nodo parte da 0


if __name__ == "__main__":
    n=70
    grafo=grafoaciclo(n)
    #grafo=grafociclo(n)

    print("Edges:", [str(i) for i in grafo.getEdges()])
    hasCycleDFS(grafo, n)
