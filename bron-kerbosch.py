class Vertice:
    def __init__(self, id, adj):
        self.id = id
        self.adj = adj

def bron_kerbosch(r, p, x, triang):
    if (len(p) == 0 and len(x) == 0):
        print("%d vertices:" % len(r), [max.id for max in r])
        triang += ((len(r)- 1) * (len(r) - 2)) / 2
        return triang
    for v in p:
        r_new = r + [v]
        p_new = [a for a in p if a.id in v.adj]
        x_new = [a for a in x if a.id in v.adj]
        triang = bron_kerbosch(r_new, p_new, x_new, triang)
        p.remove(v)
        x.append(v)
    return triang

def bron_kerbosch_pivot(r, p, x):
    if (len(p) == 0 and len(x) == 0):
        print("%d vertices:" % len(r), [max.id for max in r])
        return
    for v in p:
        r_new = r + [v]
        p_new = [a for a in p if a.id in v.adj]
        x_new = [a for a in x if a.id in v.adj]
        bron_kerbosch_pivot(r_new, p_new, x_new)
        p.remove(v)
        x.append(v)


def read_graph(filename):

    file = open(filename, "r")
    linhas = file.readlines()

    total = []
    for line in linhas:
        if (line[0] != '%' and len(line.split(" ")) == 2):
            total.append(line.split(" "))
    for a in total:
        a[1] = a[1].strip()

    for a in total:
        a[0] = int(a[0])
        a[1] = int(a[1])

    grafo = []
    for i in range(1, 63):
        v = Vertice(i, [])
        grafo.append(v)
        for a in total:
            if a[0] == i:
                grafo[-1].adj.append(a[1])
            elif a[1] == i:
                grafo[-1].adj.append(a[0])

    return grafo


grafo = read_graph("soc-dolphins.mtx")
print("Lista de adjacencia:")
for v in grafo:
    print(v.id, v.adj)
print("\n")

print("Sem pivotamento:")
triang = bron_kerbosch([], grafo, [], 0)
print("\n")

print("Com pivotamento:")
bron_kerbosch_pivot([], grafo, [])
print("\n")

poss_triangulo = 0
for v in grafo:
    poss_triangulo += (len(v.adj) * (len(v.adj) - 1)) / 2
print("Coeficiente de aglomeracao = %f" % ( 1 / (triang/poss_triangulo)))
