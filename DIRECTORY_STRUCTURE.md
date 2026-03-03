# Directory Structure

This document explains the purpose of each directory in this repository.

```
Vicliu1213/
├── .github/
│   └── workflows/          # GitHub Actions CI/CD workflow definitions
├── src/                    # Application source code
│   ├── main.py             # Main entry point
│   └── utils/              # Shared utility modules
├── tests/                  # Automated test suite
│   ├── __init__.py
│   └── test_main.py        # Tests for main module
├── docs/                   # Project documentation
│   ├── README.md           # Documentation index
│   ├── SETUP.md            # Setup and installation guide
│   ├── ARCHITECTURE.md     # Architecture overview
│   └── CONTRIBUTING.md     # Contribution guidelines
├── scripts/                # Helper and automation scripts
│   ├── setup.sh            # Project setup script
│   └── deploy.sh           # Deployment script
├── config/                 # Configuration files
│   ├── config.yml          # Application configuration
│   └── terraform.tf        # Infrastructure-as-Code (IaC)
├── README.md               # Project overview (shown on GitHub)
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
└── DIRECTORY_STRUCTURE.md  # This file
```

## Guidelines

| Directory   | What belongs here |
|-------------|-------------------|
| `src/`      | All Python source code and modules |
| `tests/`    | All test files (named `test_*.py`) |
| `docs/`     | Markdown documentation, guides, and references |
| `scripts/`  | Shell scripts for setup, CI, or automation tasks |
| `config/`   | YAML, JSON, TOML, or Terraform configuration files |
| `.github/workflows/` | GitHub Actions workflow YAML files |

## Adding New Files

- **New Python modules** → `src/` or a subdirectory of `src/`
- **New tests** → `tests/` following the `test_<module>.py` naming convention
- **New documentation** → `docs/`
- **New scripts** → `scripts/` with a `.sh` or `.py` extension
- **New configuration** → `config/`
- **New CI/CD workflows** → `.github/workflows/`
