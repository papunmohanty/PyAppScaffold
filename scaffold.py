import os
import pathlib


def generate_folder_structure(root_path, tree_structure):
    for folder, subfolders in tree_structure.items():
        folder_path = pathlib.Path(root_path) / folder
        if isinstance(subfolders, dict):
            pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)
        else:
            folder_path.touch()
        if subfolders:
            generate_folder_structure(folder_path, subfolders)


if __name__ == "__main__":
    project_name = input("Enter your application name: ")
    app_root_directory = input("Specify loction of your app(or press Enter): ")
    if app_root_directory == "\n":
        app_root_directory = os.getcwd()
    root_path = os.path.join(app_root_directory, project_name)

    tree_structure = {
        "app": {
            "__init__.py": "",
            "commands": {
                "__init__.py": "",
                "base.py": "",
                "command1.py": "",
                "command2.py": "",
            },
            "core": {
                "__init__.py": "",
                "config.py": "",
                "logging.py": "",
                "utils.py": "",
            },
            "__init__.py": "",
            "main.py": "",
            "settings.py": "",
        },
        "tests": {
            "__init__.py": "",
            "test_command1.py": "",
            "test_command2.py": "",
            "test_config.py": "",
        },
        ".gitignore": "",
        "pyproject.toml": "",
        "README.md": "",
        "requirements.txt": "",
        "setup.py": "",
    }

    generate_folder_structure(root_path, tree_structure)
    print(f"Folder structure created at: {root_path}")
