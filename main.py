import sys
from parser import parse_project
from graph import build_graph, find_circular, get_dependents, topological_sort
from visualize import render_tree, render_stats, render_cycles, render_build_order

def usage():
    print("""
depgraph — Python Dependency Graph Analyzer

Usage:
  python main.py index <directory>         → full dependency graph
  python main.py query <directory> <module>→ what depends on <module>?
  python main.py cycles <directory>        → detect circular dependencies
  python main.py order <directory>         → show build order
""")

def main():
    if len(sys.argv) < 3:
        usage()
        return

    command = sys.argv[1]
    directory = sys.argv[2]

    # Parse and build graph
    project = parse_project(directory)
    graph = build_graph(project)

    if command == "index":
        render_tree(graph)
        render_stats(graph)
        cycles = find_circular(graph)
        render_cycles(cycles)

    elif command == "cycles":
        cycles = find_circular(graph)
        render_cycles(cycles)

    elif command == "order":
        order = topological_sort(graph)
        render_build_order(order)

    elif command == "query":
        if len(sys.argv) < 4:
            print("Usage: python main.py query <directory> <module>")
            return
        target = sys.argv[3]
        dependents = get_dependents(graph, target)
        print(f"\n🔍 Modules that depend on '{target}':")
        print("=" * 40)
        if dependents:
            for d in dependents:
                print(f"  → {d}")
        else:
            print(f"  Nothing depends on '{target}'")
        
        # Also show what target itself depends on
        own_deps = graph.get(target, [])
        print(f"\n📌 '{target}' depends on:")
        if own_deps:
            for d in own_deps:
                print(f"  → {d}")
        else:
            print("  Nothing (no local deps)")

    else:
        print(f"Unknown command: {command}")
        usage()

if __name__ == "__main__":
    main()