graph = {
    "A": ["D", "B"],
    "B": ["A", "E", "C", "F"],
    "C": ["B", "F"],
    "D": ["A", "E"],
    "E": ["D", "B"],
    "F": ["B", "C"],
}


# Breadth First Traversal
def breadth_first_traversal(node):
    stack = []
    stack.append(node)
    visited.append(node)
    while stack:
        node = stack.pop(0)
        print(node, end=" ")
        for i in graph[node]:
            if i not in visited:
                stack.append(i)
                visited.append(i)

print("Breadth First Traversal")
visited = []
breadth_first_traversal("A")

# Depth First Traversal

print("\nDepth First Traversal")


def depth_first_traversal(node):
    visited.append(node)
    print(node, end=" ")
    for i in graph[node]:
        if i not in visited:
            depth_first_traversal(i)
    return visited


visited = []
print(depth_first_traversal("A"))

# Depth first traversal iterative
# This returns a differnt path
# compared withe the recursive approach

print("\nDepth First Traversal - iterative")


def depth_first_traversal_iterative(node):
    # creating stack with node
    stack = [node]
    # create visited list
    visited = []
    # print node and stack and visited
    print(node, "".join(stack), "".join(visited))
    # while the stack is not empty
    while stack:
        # remove last item from stakc and assign it to node
        node = stack.pop()
        # print node, stack, visited
        print(node, "".join(stack), "".join(visited))
        # if the node isn't in the visited list
        if node not in visited:
            # add the node to the ivsited list
            visited.append(node)
            # print the stuff again
            print(node, "".join(stack), "".join(visited))
            # iterate through the node
            for i in graph[node]:
                # add the items to the stack
                stack.append(i)
                # print the stuff again again 
                print(node, "".join(stack), "".join(visited), i)
    # return the visited list
    return visited

print(depth_first_traversal_iterative("A"))
