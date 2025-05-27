import json
import shutil
from pathlib import Path
import zipfile
import pytest

from challengeforge.exporter import export_zip, export_json

def setup_test_case_dir(tmp_path):
    # Setup a fake testcases directory with one input/output pair
    case_dir = tmp_path / "testcases"
    case_dir.mkdir()
    input_file = case_dir / "case_1_input.txt"
    output_file = case_dir / "case_1_output.txt"
    input_file.write_text("data\n")
    output_file.write_text("result\n")
    return case_dir

def test_export_zip(tmp_path, monkeypatch):
    # Create dummy config
    dummy_config = {"name": "Dummy", "output_dir": str(tmp_path / "testcases")}
    case_dir = setup_test_case_dir(tmp_path)
    # Call export_zip
    export_zip(dummy_config)
    zip_path = Path("Dummy_testcases.zip")
    assert zip_path.exists()
    # Cleanup
    zip_path.unlink()

def test_export_json(tmp_path):
    case_dir = setup_test_case_dir(tmp_path)
    dummy_config = {"name": "Dummy", "output_dir": str(case_dir)}
    export_json(dummy_config)
    json_path = Path("Dummy_testcases.json")
    assert json_path.exists()
    data = json.loads(json_path.read_text())
    assert data["inputs"] == ["data\n"]
    assert data["outputs"] == ["result\n"]
    # Cleanup
    json_path.unlink()
