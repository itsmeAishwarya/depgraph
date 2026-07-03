def render_tree(graph):
    """Print dependency tree in terminal."""
    print("\n DEPENDENCY GRAPH")
    print("=" * 40)"""for clarity"""
    
    if not graph:
        print("No Python files found.")
        return
    
    for module, deps in sorted(graph.items()):
        if deps:
            print(f"\n  {module}")
            for i, dep in enumerate(deps):
                connector = "└──" if i == len(deps) - 1 else "├──"
                print(f"    {connector} {dep}")
        else:
            print(f"\n  {module} (no local deps)")


def render_stats(graph):
    """Print summary statistics."""
    total_modules = len(graph)
    total_deps = sum(len(d) for d in graph.values())
    most_deps = max(graph.items(), key=lambda x: len(x[1]), default=("none", []))
    
    print("\n STATS(imp ouput 1)")
    print("=" * 40)
    print(f"  Total modules:     {total_modules}")
    print(f"  Total dependencies:{total_deps}")
    print(f"  Most connected:    {most_deps[0]} ({len(most_deps[1])} deps)")


def render_cycles(cycles):
    """Print circular dependency warnings."""
    print("\n CIRCULAR DEPENDENCIES")
    print("=" * 40)
    if not cycles:
        print(" :)  None found!")
    else:
        for cycle in cycles:
            print(f"    {' → '.join(cycle)}")


def render_build_order(order):
    """Print topological build order."""
    print("\n  BUILD ORDER (dependencies first)")
    print("=" * 40)
    for i, module in enumerate(order, 1):
        print(f"  {i}. {module}")
