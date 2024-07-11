import streamlit as st
import graphviz

def createBinaryTree(l):
    graph = graphviz.Digraph()
    if not l:
        return
    root = l[0]
    
    queue = [(root, 0)]  
    i = 1
    index = 1  
    while i < len(l):
        if len(queue) == 0:
            st.write("Invalid Tree")
            break
        root, root_index = queue.pop(0)
        for j in range(2):
            if i >= len(l):
                break
            if l[i] == 'N':
                pass
            else:
                node_id = f"{l[i]}_{index}"  # Unique identifier for each node
                graph.edge(f"{root}_{root_index}", node_id)
                queue.append((l[i], index))
                index += 1
            i += 1
    
    st.graphviz_chart(graph.source)

def sorted_array_to_bst(arr, index_tracker):
    if not arr:
        return None

    mid = len(arr) // 2
    node = arr[mid]
    node_id = index_tracker[0]
    index_tracker[0] += 1
    left_subtree = sorted_array_to_bst(arr[:mid], index_tracker)
    right_subtree = sorted_array_to_bst(arr[mid+1:], index_tracker)
    
    return (node, left_subtree, right_subtree, node_id)

def visualize_bst(node, graph=None, parent=None, parent_id=None):
    if not node:
        return
    
    if graph is None:
        graph = graphviz.Digraph()
    
    node_id = f"{node[0]}_{node[3]}"  # Unique identifier for each node
    if parent is not None:
        graph.edge(f"{parent}_{parent_id}", node_id)
    
    visualize_bst(node[1], graph, node[0], node[3])
    visualize_bst(node[2], graph, node[0], node[3])
    
    return graph

def binarySearchTree(l):
    # Remove 'N' (null) values and convert the list to integers
    l = [x for x in l if x != 'N']
    l.sort()
    index_tracker = [0]  # A tracker to maintain unique indices
    bst = sorted_array_to_bst(l, index_tracker)
    graph = visualize_bst(bst)
    st.graphviz_chart(graph.source)

if __name__ == "__main__":
    title = st.text_input("Enter space-separated node values (use 'N' for null nodes):")
    title = title.split()
    if title:
        BT = st.checkbox("Binary Tree")
        BST = st.checkbox("Binary Search Tree")
        if BT:
            st.write("Binary Tree")
            createBinaryTree(title)
        if BST:
            st.write("Binary Search Tree")
            binarySearchTree(title)
