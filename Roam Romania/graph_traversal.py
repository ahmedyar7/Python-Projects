import queue
import networkx as nx
import matplotlib.pyplot as plt


class GraphTraversal:
    def __init__(self) -> None:

        self.graph = nx.Graph()
        self.graph.add_edges_from(
            [
                ("Oradea", "Zerind"),
                ("Oradea", "Sibiu"),
                ("Zerind", "Arad"),
                ("Arad", "Sibiu"),
                ("Timisoara", "Lugoj"),
                ("Lugoj", "Mehadia"),
                ("Mehadia", "Drobeta"),
                ("Drobeta", "Craiova"),
                ("Craiova", "Pitesti"),
                ("Craiova", "Rimnicu Vilcea"),
                ("Rimnicu Vilcea", "Sibiu"),
                ("Sibiu", "Fagaras"),
                ("Fagaras", "Bucharest"),
                ("Bucharest", "Giurgiu"),
                ("Bucharest", "Pitesti"),
                ("Bucharest", "Urziceni"),
                ("Urziceni", "Vaslui"),
                ("Vaslui", "Iasi"),
                ("Iasi", "Neamt"),
                ("Urziceni", "Hirsova"),
                ("Hirsova", "Eforie"),
            ]
        )

        self.pos = nx.spring_layout(self.graph, seed=42)

    def order_bfs(self, start_node):
        """
        Perform a Breadth-First Search (BFS) traversal starting from the specified node.

        This method explores the graph in a BFS manner, starting from the `start_node` and
        visiting each connected node level by level. It returns the order in which the
        nodes are visited.

        Args:
            start_node (str): The starting node for the BFS traversal.

        Returns:
            list: A list of nodes representing the order in which they are visited during BFS.
        """

        visited = set()
        q = queue.Queue()
        q.put(start_node)
        order_set = []

        while not q.empty():
            vertex = q.get()
            if vertex not in visited:
                visited.add(vertex)
                order_set.append(vertex)

                for node in self.graph[vertex]:
                    if node not in visited:
                        q.put(node)

        return order_set

    def find_shortest_path(self, start_node, target_node):
        """
        Find the shortest path between two nodes using an unweighted graph traversal algorithm.

        This method uses NetworkX's built-in `shortest_path` function to compute and return
        the shortest path between the `start_node` and the `end_node`. In this case, the
        shortest path is based on the number of edges, since the graph is unweighted.

         Args:
            >>> start_node (str): The starting node from which to calculate the shortest path.
            >>> end_node (str): The destination node to which the shortest path is calculated.

         Returns:
            - list: A list of nodes representing the shortest path from the `start_node`
            - to the `end_node`. If there is no path, an exception may be raised by NetworkX.
        """

        return nx.all_shortest_paths(self.graph, source=start_node, target=target_node)

    def order_dfs(self, start_node, visited):
        """
        Perform a Depth-First Search (DFS) traversal of the graph starting from the given node.

        Args:
            >>> start_node (hashable): The starting node for the DFS traversal.
            >>> visited (set): A set of nodes that have already been visited. If None, a new set will be created to track visited nodes.

        Returns:
            list: A list of nodes in the order they were visited during the DFS traversal.

        Notes:
            - This method uses recursion to explore all connected nodes from the `start_node`.
            - The graph is traversed in depth-first order, meaning that the method explores as far as possible along each branch before backtracking.
            - The `visited` set ensures that each node is visited only once to avoid cycles or redundant checks in the graph.

        Example:
            If the graph represents cities and the DFS starts from city 'A', the function will return a list of cities in the order they are visited.
        """

        if visited is None:
            visited = set()

        order_set = []

        if start_node not in visited:
            visited.add(start_node)
            order_set.append(start_node)

            for node in self.graph:
                if node not in visited:
                    order_set.extend(self.order_dfs(node, visited))
        return order_set

    def visualize_search(
        self, order_set, title, shortest_path=None, pause_duration=0.5
    ):
        plt.figure(figsize=(8, 8))
        plt.title(title, fontsize=16)

        for i, node in enumerate(order_set, start=1):
            plt.clf()
            plt.title(f"{title} Steps: {i}/{len(order_set)}", fontsize=16)

            node_color = [
                "lightgreen" if nodes in order_set[:i] else "lightblue"
                for nodes in self.graph.nodes
            ]
