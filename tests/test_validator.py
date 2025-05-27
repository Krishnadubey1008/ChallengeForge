import subprocess
import sys
import pytest
from pathlib import Path

from challengeforge.validator import run_reference_solution

def create_dummy_solution(tmp_path):
    # Write a simple Python script that echoes its input
    script = tmp_path / "echo_solution.py"
    script.write_text("import sys\nfor line in sys.stdin: print(line.strip())")
    return script

def test_run_reference_solution(tmp_path):
    script = create_dummy_solution(tmp_path)
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"
    input_file.write_text("hello\nworld\n")
    run_reference_solution(str(script), input_file, output_file)
    output = output_file.read_text().strip().splitlines()
    assert output == ["hello", "world"]
