# import heapq
# import networkx as nx
# import matplotlib.pyplot as plt
# import math
# def minimax(depth, node_index, is_maximizing, values, max_depth):
#     # When we reach leaves, compute which value index this heap index maps to
#     if depth == max_depth:
#         leaf_start = 2**max_depth - 1
#         leaf_index = node_index - leaf_start
#         return values[leaf_index]
#     le = minimax(depth + 1, node_index * 2 + 1, not is_maximizing, values, max_depth)
#     right = minimax(depth + 1, node_index * 2 + 2, not is_maximizing, values, max_depth)

#     return max(le , right) if is_maximizing else min(le , right)

# def build_tree_graph(depth, node_index, is_maximizing, values, max_depth, G, labels,
# parent=None):
#     if depth == max_depth:
#         leaf_start = 2**max_depth - 1
#         leaf_index = node_index - leaf_start
#         labels[node_index] = str(values[leaf_index])
#         G.add_node(node_index)
#         if parent is not None:
#             G.add_edge(parent, node_index)
#         return values[leaf_index]

#     le_val = build_tree_graph(depth + 1, node_index * 2 + 1, not is_maximizing, values,
# max_depth, G, labels, node_index)
#     right_val = build_tree_graph(depth + 1, node_index * 2 + 2, not is_maximizing, values,
# max_depth, G, labels, node_index)

#     node_value = max(le_val, right_val) if is_maximizing else min(le_val, right_val)
#     labels[node_index] = str(node_value)

#     G.add_node(node_index)
#     if parent is not None:
#         G.add_edge(parent, node_index)

#     return node_value

# def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
#     pos = _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
#     return pos

# def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None,
# parent=None):
#     if pos is None:
#         pos = {root: (xcenter, vert_loc)}
#     else:
#         pos[root] = (xcenter, vert_loc)

#     children = list(G.successors(root))
#     if len(children) != 0:
#         dx = width / len(children)
#         nextx = xcenter - width/2 - dx/2
#         for child in children:
#             nextx += dx
#             pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
#                                  vert_loc=vert_loc - vert_gap, xcenter=nextx, pos=pos, parent=root)
#     return pos
# if __name__ == "__main__":

#     n = int(input("Enter number of leaf nodes (must be power of 2): "))

#     if math.log2(n) % 1 != 0:
#         print("Error: Number of leaf nodes must be a power of 2 (e.g., 2, 4, 8, ...).")
#         raise SystemExit(1)

#     print("Enter values of leaf nodes one by one:")
#     values = []
#     for i in range(n):
#         v = int(input(f"Value of leaf node {i+1}: "))
#         values.append(v)

#     max_depth = int(math.log2(n))

#     opmal_value = minimax(0, 0, True, values, max_depth)

#     G = nx.DiGraph()
#     labels = {}
#     build_tree_graph(0, 0, True, values, max_depth, G, labels)

#     pos = hierarchy_pos(G, 0)
#     plt.figure(figsize=(12, 6))
#     nx.draw(G, pos, with_labels=True, labels=labels, node_size=1100,node_color="lightblue", font_size=9, font_weight="bold", arrows=False)
#     plt.title(f"Minimax Tree (Opmal Value = {opmal_value})")
#     plt.tight_layout()
#     plt.show()

#     print(f"\nNumber  of leaf nodes: {n}")
#     print(f"Leaf node values: {values}")
#     print(f"Opmal value (Minimax result): {opmal_value}")
    
    
    
    
# A simple Python3 program to find
# maximum score that
# maximizing player can get
import math

def minimax (curDepth, nodeIndex,
             maxTurn, scores, 
             targetDepth):

    # base case : targetDepth reached
    if (curDepth == targetDepth): 
        return scores[nodeIndex]
    
    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2, 
                    False, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, 
                    False, scores, targetDepth))
    
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, 
                     True, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, 
                     True, scores, targetDepth))
    
# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores,treeDepth))