import json
import zipfile
from pathlib import Path

from .utils import ensure_directory

def export_zip(config: dict):
    """
    Package the test cases directory into a zip archive.
    """
    challenge_name = config.get("name", "challenge")
    output_dir = Path(config.get("output_dir", "testcases"))
    zip_path = Path(f"{challenge_name}_testcases.zip")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in output_dir.rglob("*"):
            zf.write(file_path, arcname=file_path.relative_to(output_dir.parent))

def export_json(config: dict):
    """
    Export test cases as a single JSON file containing inputs and outputs.
    """
    output_dir = Path(config.get("output_dir", "testcases"))
    bundle = {"inputs": [], "outputs": []}
    for input_file in sorted(output_dir.glob("*_input.txt")):
        case_id = input_file.stem.split("_input")[0]
        output_file = output_dir / f"{case_id}_output.txt"
        with open(input_file, 'r') as f:
            bundle["inputs"].append(f.read())
        if output_file.exists():
            with open(output_file, 'r') as f:
                bundle["outputs"].append(f.read())
        else:
            bundle["outputs"].append(None)
    json_path = Path(f"{config.get('name', 'challenge')}_testcases.json")
    with open(json_path, 'w') as jf:
        json.dump(bundle, jf, indent=2)
