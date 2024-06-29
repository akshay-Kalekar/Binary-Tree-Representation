import streamlit as st
import graphviz

def createBinaryTree(s):
    graph = graphviz.Digraph()
    l = s.split()
    if not l:
        return
    root = l[0]
    
    queue = [(root, 0)]  
    i = 1
    index = 1  
    while i < len(l):
        if(len(queue)==0):
            st.write("invalide Tree")
            break
        root, root_index = queue.pop(0)
        for j in range(2):
            if i >= len(l):
                break
            if l[i] == 'N':
                pass
            else:
                node_id = f"{l[i]} #{index}"  
                graph.edge(f"{root} #{root_index}", node_id)
                queue.append((l[i], index))
                index += 1
            i += 1
    
    st.graphviz_chart(graph.source)

if __name__ == "__main__":
    title = st.text_input("Enter space-separated node values (use 'N' for null nodes):")
    if title:
        createBinaryTree(title)
