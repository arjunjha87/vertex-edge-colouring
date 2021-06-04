import networkx as nx
import matplotlib.pyplot as plt
from random import randint
g = nx.Graph()
edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2,
4)]
colors = ["BLUE", "GREEN", "RED", "YELLOW", "ORANGE", "PINK","BLACK",
"BROWN", "WHITE", "PURPLE"]
for edge in edges:
  g.add_edge(edge[0],edge[1])
color = nx.coloring.greedy_color(g, strategy = "largest_first")
v_color = [colors[color[edge]] for edge in sorted(color)]
e_color = [colors[randint(0,9)] for edge in sorted(color)]
f_color = [colors[color[edge]+4] for edge in sorted(color)]
[12:08, 6/4/2021] Shubham: nx.draw(g, node_color = v_color, edge_color=e_color ,with_labels =
True, width=3, node_size=400)
for index,color in enumerate(v_color):
  print("Color assigned to vertex", index, "is", color)
print("-------------------------------------")
for index,color in enumerate(e_color):
  print("Color assigned to Edge", index, "is", color)
print("-------------------------------------")
for index,color in enumerate(f_color):
  print("Color assigned to Face", index, "is", color)
  
