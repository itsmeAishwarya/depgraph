def build_graph(project):
    """Build adjacency list from parsed project."""
    # project = {module: [dep1, dep2, ...]}
    return project


def find_circular(graph):
    """Detect circular dependencies using DFS."""
    visited = set()
    rec_stack = set()
    cycles = []

    def dfs(node, path):
        visited.add(node)
        rec_stack.add(node)
        path.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, path)
            elif neighbor in rec_stack:
                # Found a cycle — extract it
                cycle_start = path.index(neighbor)
                cycle = path[cycle_start:] + [neighbor]
                cycles.append(cycle)

        path.pop()
        rec_stack.discard(node)

    for node in graph:
        if node not in visited:
            dfs(node, [])

    return cycles


def get_dependents(graph, target):
    """Find all modules that depend on a given module."""
    dependents = []
    for module, deps in graph.items():
        if target in deps:
            dependents.append(module)
    return dependents


def topological_sort(graph):
    """Return modules in build order (dependencies first)."""
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        for dep in graph.get(node, []):
            if dep not in visited:
                dfs(dep)
        order.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return order