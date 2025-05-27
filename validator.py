import subprocess
from pathlib import Path

from .utils import load_config, ensure_directory

def run_reference_solution(ref_path: str, input_path: Path, output_path: Path):
    """
    Run the reference solution script with the given input file,
    capturing its output into the output file.
    """
    ref_path = Path(ref_path)
    if not ref_path.exists():
        raise FileNotFoundError(f"Reference solution not found: {ref_path}")

    # Ensure output directory exists
    ensure_directory(output_path.parent)

    # Run reference solution (assuming a Python script)
    # Redirect input and output
    with open(input_path, 'r') as inp, open(output_path, 'w') as outp:
        subprocess.run(["python3", str(ref_path)], stdin=inp, stdout=outp, check=True)

def validate_test_cases(config: dict):
    """
    Validate each test case by running the reference solution and checking outputs.
    """
    ref_sol = config.get("reference_solution")
    test_dir = Path(config.get("output_dir", "testcases"))
    if not ref_sol:
        raise ValueError("No reference_solution specified in config.")

    for input_file in sorted(test_dir.glob("*_input.txt")):
        case_id = input_file.stem.split("_input")[0]
        output_file = test_dir / f"{case_id}_output.txt"
        # Regenerate output from reference solution
        run_reference_solution(ref_sol, input_file, output_file)
