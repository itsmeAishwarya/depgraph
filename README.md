# depgraph 🔍

A Python dependency graph analyzer that maps, visualizes, and queries 
module relationships in any Python codebase — built from scratch using 
Python's AST module, with zero external dependencies.

---

## What it does

Give it any Python project directory and it will:
- Parse every `.py` file and extract all import relationships using AST
- Build a directed dependency graph of your entire codebase
- Detect circular dependencies using DFS
- Generate a topological build order
- Answer queries like "what modules depend on X?"

---

## Usage

```bash
# Full dependency graph + stats + cycle detection
python3 main.py index <directory>

# What depends on a specific module?
python3 main.py query <directory> <module>

# Detect circular dependencies
python3 main.py cycles <directory>

# Show build order (dependencies first)
python3 main.py order <directory>
```

````md
## Sample output

```text
📦 DEPENDENCY GRAPH

════════════════════════════════════════

main
├── parser
├── graph
└── visualize

parser (no local deps)
graph (no local deps)
visualize (no local deps)

📊 STATS

════════════════════════════════════════

Total modules:      4
Total dependencies: 3
Most connected:     main (3 deps)

🔄 CIRCULAR DEPENDENCIES

════════════════════════════════════════

✅ None found!

🏗️ BUILD ORDER

════════════════════════════════════════

parser
graph
visualize
main
````

```
```
---

## How it works

**Parsing** — uses Python's built-in `ast` module to walk the syntax 
tree of each file and extract `import` and `from...import` statements. 
No regex, no string matching — proper AST traversal.

**Graph building** — constructs a directed adjacency list mapping each 
module to its local dependencies, filtering out stdlib and third-party 
imports to focus on the project's own structure.

**Cycle detection** — runs DFS with a recursion stack to identify 
circular dependencies, which would cause import errors at runtime.

**Topological sort** — orders modules so every dependency appears before 
the modules that need it — essentially the order a build system would 
compile them.

---


## Stack
- Language: Python 3
- Core: `ast` (syntax tree parsing), `os` (directory traversal)
- Zero external dependencies
