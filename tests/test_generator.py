import pytest
import tempfile
import shutil
from pathlib import Path
import networkx as nx

from challengeforge.generator import _generate_random_graph, _save_graph_input

def test_generate_random_graph():
    config = {"num_nodes": 5, "num_edges": 4, "directed": False}
    G = _generate_random_graph(config)
    # Check number of nodes and edges
    assert G.number_of_nodes() == 5
    assert G.number_of_edges() == 4

def test_save_graph_input(tmp_path):
    # Create a simple graph
    G = nx.Graph()
    G.add_nodes_from([0, 1, 2])
    G.add_edges_from([(0,1), (1,2)])
    filepath = tmp_path / "graph_input.txt"
    _save_graph_input(G, filepath, {})
    # Read file and check contents
    text = filepath.read_text().strip().splitlines()
    assert text[0] == "3 2"
    edges = {tuple(map(int, line.split())) for line in text[1:]}
    assert edges == {(0,1), (1,2)}
