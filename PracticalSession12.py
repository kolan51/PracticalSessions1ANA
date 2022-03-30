MAX = 300
n = 0

# Stores the vertices
store = [0] * MAX

# Graph
graph = [[0 for i in range(MAX)] for j in range(MAX)]

# Degree of the vertices
d = [0] * MAX

# Function to check if the given set of vertices in store array is a clique or not
def is_clique(b):
    # Run a loop for all set of edges
    for i in range(1, b):
        for j in range(i + 1, b):

            # If any edge is missing
            if graph[store[i]][store[j]] == 0:
                return False

    return True

# Function to find all the sizes of maximal cliques
def maxCliques(i, l):
    # Maximal clique size
    max_ = 0

    # Check if any vertices from i+1 can be inserted
    for j in range(i + 1, n + 1):

        # Add the vertex to store
        store[l] = j

        # If the graph is not a clique of size k then it cannot be a clique by adding another edge
        if is_clique(l + 1):
            # Update max
            max_ = max(max_, l)

            # Check if another edge can be added
            max_ = max(max_, maxCliques(j, l + 1))

    return max_


if __name__ == '__main__':

    f = open("G1.txt", "r")
    count = 0
    all = []
    edges = []
    myline = f.readline()
    while myline:
        x = myline.strip("\n").split(" ")
        x = [int(x[0]), int(x[1])]
        if x[0] not in all:
            all.append(x[0])
        if x[1] not in all:
            all.append(x[1])
        edges.append(x)
        myline = f.readline()
        count += 1
    f.close()

    MAX = count

    size = len(edges)
    n = len(all)

    for i in range(size):
        graph[edges[i][0]][edges[i][1]] = 1
        graph[edges[i][1]][edges[i][0]] = 1
        d[edges[i][0]] += 1
        d[edges[i][1]] += 1

    print(f.name.strip(".txt") + ": " + str(maxCliques(0, 1)))
