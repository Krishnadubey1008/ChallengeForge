import pytest
import yaml
from pathlib import Path
from challengeforge.utils import create_challenge_scaffold, load_config

def test_create_challenge_scaffold(tmp_path):
    name = "TestChallenge"
    base = tmp_path
    challenge_dir = create_challenge_scaffold(name, base)
    # Check directories and files
    assert (challenge_dir / "config.yaml").exists()
    assert (challenge_dir / "testcases").exists()
    assert (challenge_dir / "reference_solution.py").exists()
    # Load config and verify contents
    config = load_config(challenge_dir / "config.yaml")
    assert config["name"] == name
    assert config["generator"]["type"] == "random_graph"
