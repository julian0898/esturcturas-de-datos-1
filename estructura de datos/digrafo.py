import networkx as nx
import matplotlib.pyplot as plt

# Definir el conjunto A
A = [(x, y) for x in range(1, 4) for y in range(1, 4)]

# Crear el grafo dirigido
G = nx.DiGraph()

# Agregar nodos
G.add_nodes_from(A)

# Agregar aristas según la relación (x, y) ⪯ (u, v)
for (x, y) in A:
    for (u, v) in A:
        if x <= u and y <= v:
            G.add_edge((x, y), (u, v))

# Dibujar el grafo
pos = {node: (node[0], -node[1]) for node in G.nodes()}  # Posiciones para una visualización ordenada
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", arrows=True)
plt.title("Dígrafo de la relación ⪯ sobre A")
plt.show()
