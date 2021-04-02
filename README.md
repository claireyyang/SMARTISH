# SMARTISH
Social Minds and Agent Reasoning Testbed for Inverse Inference and Signaling with Humans

## Overview
This repository contains a testbed that contains a partially observable 3-player stag hunt simulation with signaling. We are investigating how we can model social preferences in these cooperative/competitive games through varying levels of agents in the cognitive hierarchy. See the README.md in the `/env` directory for a description of the simulation itself.

## Requirements
* Python 3.9.2
* Pip

## Getting Started
1) `pip3 install wheel`
2) `pip3 install mypy`
3) `python3 -m pip install .`

## Development
### Install Notes
 - python3 -m pip install .
 - python3 -m build --sdist --wheel .

### Before Pushing Do These Things 
  1. Lint the code: `pylint smartish`
  2. Type check the code `mypy smartish`
  3. Lint the tests: `pylint tests`
  4. Type check the tests `pylint tests`
  5. Run the unit tests `pytest tests`
  6. Generate new interface files (if appropriate) `stubgen smartish -o types`
