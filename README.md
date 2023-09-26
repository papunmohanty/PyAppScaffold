# Folder Structure for a Sample Command-line based application

## Sample Reference Project Structure for a commandline application

```sh
project_name/
│
├── app/
│   ├── __init__.py
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── base.py  # Base command class
│   │   ├── command1.py  # Command 1 implementation
│   │   ├── command2.py  # Command 2 implementation
│   │   └── ...  # Additional command files
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py  # Configuration handling
│   │   ├── logging.py  # Logging configuration
│   │   └── utils.py  # Utility functions
│   │
│   ├── __init__.py
│   ├── main.py  # Entry point for the command-line application
│   └── settings.py  # Application settings and constants
│
├── tests/
│   ├── __init__.py
│   ├── test_command1.py
│   ├── test_command2.py
│   ├── test_config.py
│   └── ...  # Additional test files
│
├── .gitignore
├── pyproject.toml  # Project metadata and dependencies
├── README.md
├── requirements.txt  # Development dependencies
└── setup.py  # Project setup script
```

## Bootstrapping the Project from an existing template

The Python script `script.py` allows to scaffold project from a given structure/template specified in the distionary
