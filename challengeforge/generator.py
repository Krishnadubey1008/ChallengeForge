import os
import json
import random
from pathlib import Path
import networkx as nx

from .utils import ensure_directory

def generate_test_cases(config: dict):
    """
    Generate test cases based on the provided configuration dictionary.
    For each test case, create an input file (and optionally an output file by running reference solution).
    """
    challenge_name = config.get("name", "challenge")
    output_dir = Path(config.get("output_dir", "testcases"))
    ensure_directory(output_dir)

    num_cases = config.get("test_cases", 1)
    gen_cfg = config.get("generator", {})

    for i in range(1, num_cases + 1):
        case_id = f"case_{i}"
        input_path = output_dir / f"{case_id}_input.txt"
        output_path = output_dir / f"{case_id}_output.txt"

        # Example: generate a random graph input if type is 'random_graph'
        gen_type = gen_cfg.get("type", "")
        if gen_type == "random_graph":
            graph = _generate_random_graph(gen_cfg)
            # Save graph to input file
            _save_graph_input(graph, input_path, gen_cfg)
        else:
            # Placeholder for other generator types
            with open(input_path, "w") as f:
                f.write(str(config))

        # Optionally, run reference solution to generate the correct output
        ref_sol = config.get("reference_solution")
        if ref_sol:
            # Use validator to run solution and create output file
            from .validator import run_reference_solution
            run_reference_solution(ref_sol, input_path, output_path)

def _generate_random_graph(gen_cfg: dict) -> nx.Graph:
    """
    Generate a random graph based on configuration.
    """
    num_nodes = gen_cfg.get("num_nodes", 10)
    num_edges = gen_cfg.get("num_edges", 15)
    directed = gen_cfg.get("directed", False)
    # Choose generation method; here we do simple random graph
    if directed:
        G = nx.gnm_random_graph(n=num_nodes, m=num_edges, directed=True)
    else:
        G = nx.gnm_random_graph(n=num_nodes, m=num_edges)
    return G

def _save_graph_input(graph: nx.Graph, filepath: Path, gen_cfg: dict):
    """
    Save a graph to a text file. Format:
    First line: num_nodes num_edges
    Next lines: edge pairs (u v) one per line.
    """
    with open(filepath, "w") as f:
        num_nodes = graph.number_of_nodes()
        num_edges = graph.number_of_edges()
        f.write(f"{num_nodes} {num_edges}\n")
        for u, v in graph.edges():
            f.write(f"{u} {v}\n")