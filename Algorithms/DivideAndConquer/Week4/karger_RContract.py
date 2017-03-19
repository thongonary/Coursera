# === Random Contraction Algorith ===
# While there are more than 2 vertices:
# - Pick a remaining edge (u,v) uniformly at random
# - Merge (or "contract") u and v into a single vertex
# - Remove self-loops
# Return cut represented by final 2 vertices


import argparse
import copy
from random import randint as ri

parser = argparse.ArgumentParser(description='Karger Random Contraction.')
parser.add_argument('-i', required=True, help = 'Input graph')
args = parser.parse_args()

min_cut = 1000;

original_nodes = []
original_edges = []

# Extract data from file:
with open(args.i) as infile:
    for row in infile.read().splitlines(): # file.read() returns the string as content of the file. string.splitlines() return the strings in the files separated by '\n'
        row_list = row.strip().split('\t')  # string.strip() return the string with whitespace character removed. string.split('\t') returns a list from the string separated by ('\t')
        original_nodes.append(int(row_list[0]))
        for i in range (1, len(row_list)):
            temp_edge = [int(row_list[0]), int(row_list[i])]
            temp_edge_reverse = [int(row_list[i]), int(row_list[0])]
            if not (temp_edge in original_edges or temp_edge_reverse in original_edges):
                original_edges.append(temp_edge)

for trial in range(0, 100):
    edges = copy.deepcopy(original_edges) # if just a = b, then pointer of a assign to b's and we still have only 1 list.
    nodes = copy.deepcopy(original_nodes) # copy.deepcopy() copies objects in the list 

    while len(nodes) > 2:
        # Pick a remaining edge (u,v) uniformly at random
        chosen_edge = edges[ri(0, len(edges)-1)]
        u = chosen_edge[0]
        v = chosen_edge[1]

        # Merge u and v into a single vertex, i.e, turn v into u
        for edge in edges:
            if edge[0] == v: edge[0] = u
            if edge[1] == v: edge[1] = u
        nodes.remove(v)

        # Remove self-loop
        edges = [x for x in edges if x[0] != x[1]]

        if len(edges) < min_cut: min_cut = len(edges)
    del edges
    del nodes
print min_cut
