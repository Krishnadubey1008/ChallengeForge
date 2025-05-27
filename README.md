# ChallengeForge

ChallengeForge is a command-line toolkit to automate the creation, validation, and packaging of coding challenges. It helps challenge authors generate test inputs and outputs, validate them with a reference solution, and export them for distribution.

## Features

- **Create** new challenge templates with a YAML configuration.
- **Define** problem parameters and constraints via `config.yaml`.
- **Generate** random test cases (e.g., graphs) using various algorithms.
- **Validate** test cases by running a reference solution.
- **Export** test cases as a ZIP archive or JSON bundle.

## Installation

Use `pip` to install the package dependencies:

```bash
pip install typer networkx pyyaml
