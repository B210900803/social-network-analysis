import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Load the data
data = pd.read_csv("data/edges.csv")
G = nx.from_pandas_edgelist(data, source='Source', target='Target')

# Draw the network
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
plt.savefig("results/network_visualization.png")
plt.show()
