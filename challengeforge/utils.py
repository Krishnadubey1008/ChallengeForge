import os
import yaml
import subprocess
from pathlib import Path
from typing import Any

def create_challenge_scaffold(name: str, base_path: Path) -> Path:
    """
    Create a directory structure for a new challenge.
    """
    challenge_dir = base_path / name
    config_path = challenge_dir / "config.yaml"
    # Create directories
    challenge_dir.mkdir(parents=True, exist_ok=False)
    (challenge_dir / "testcases").mkdir()
    # Default config.yaml
    default_config = {
        "name": name,
        "description": "",
        "generator": {
            "type": "random_graph",
            "num_nodes": 5,
            "num_edges": 4,
            "directed": False
        },
        "test_cases": 3,
        "reference_solution": "reference_solution.py",
        "output_dir": "testcases"
    }
    with open(config_path, "w") as f:
        yaml.dump(default_config, f)
    # Create a template reference solution if desired
    ref_path = challenge_dir / "reference_solution.py"
    with open(ref_path, "w") as f:
        f.write("# Reference solution logic goes here\n")
    return challenge_dir

def ensure_config_exists(config_path: Path):
    """
    Check that the config file exists and is writable.
    """
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found at {config_path}")

def edit_config_interactive(config_path: Path):
    """
    Open the config file in the default editor for manual editing.
    """
    editor = os.environ.get("EDITOR", "nano")
    subprocess.run([editor, str(config_path)])

def load_config(config_path: Path) -> dict:
    """
    Load and return the YAML configuration as a dictionary.
    """
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def ensure_directory(path: Path):
    """
    Create the directory if it does not exist.
    """
    path.mkdir(parents=True, exist_ok=True)
