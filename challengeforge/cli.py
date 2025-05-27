import typer
from pathlib import Path
import sys

from . import generator, validator, exporter, utils

app = typer.Typer(help="ChallengeForge CLI - generate and manage coding challenges")

@app.command()
def create(name: str, path: Path = typer.Option(Path("."), "--path", "-p", help="Directory to create the challenge in")):
    """
    Create a new challenge directory with the given NAME.
    """
    try:
        challenge_path = utils.create_challenge_scaffold(name, path)
        typer.echo(f"Created challenge scaffold at {challenge_path}")
    except Exception as e:
        typer.echo(f"Error creating challenge: {e}", err=True)
        sys.exit(1)

@app.command()
def define(config: Path = typer.Option("config.yaml", "--config", "-c", help="Path to challenge config file")):
    """
    Define or update parameters in the challenge configuration (config.yaml).
    """
    try:
        utils.ensure_config_exists(config)
        utils.edit_config_interactive(config)
        typer.echo(f"Updated configuration at {config}")
    except Exception as e:
        typer.echo(f"Error defining parameters: {e}", err=True)
        sys.exit(1)

@app.command()
def generate(config: Path = typer.Option("config.yaml", "--config", "-c", help="Path to challenge config file")):
    """
    Generate test cases based on the challenge configuration.
    """
    try:
        cfg = utils.load_config(config)
        generator.generate_test_cases(cfg)
        typer.echo("Test case generation complete.")
    except Exception as e:
        typer.echo(f"Error generating test cases: {e}", err=True)
        sys.exit(1)

@app.command()
def validate(config: Path = typer.Option("config.yaml", "--config", "-c", help="Path to challenge config file")):
    """
    Validate test cases by running the reference solution on each input.
    """
    try:
        cfg = utils.load_config(config)
        validator.validate_test_cases(cfg)
        typer.echo("Validation complete. All test cases passed successfully.")
    except Exception as e:
        typer.echo(f"Validation error: {e}", err=True)
        sys.exit(1)

@app.command()
def export(
    config: Path = typer.Option("config.yaml", "--config", "-c", help="Path to challenge config file"),
    format: str = typer.Option("zip", "--format", "-f", help="Export format: 'zip' or 'json'")
):
    """
    Export test cases as a ZIP archive or JSON bundle.
    """
    try:
        cfg = utils.load_config(config)
        if format.lower() == "zip":
            exporter.export_zip(cfg)
            typer.echo("Exported test cases as ZIP archive.")
        elif format.lower() == "json":
            exporter.export_json(cfg)
            typer.echo("Exported test cases as JSON.")
        else:
            typer.echo("Unsupported format. Use 'zip' or 'json'.", err=True)
            sys.exit(1)
    except Exception as e:
        typer.echo(f"Error exporting test cases: {e}", err=True)
        sys.exit(1)

if __name__ == "__main__":
    app()