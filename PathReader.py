import subprocess
import json
import os

def load_applications_from_file(file_name="vell_mapping.json"):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return {}

def open_app(app_name):
    app_mapping = load_applications_from_file()
    app_path = app_mapping.get(app_name.lower())
    if app_path:
        try:
            subprocess.Popen(app_path, shell=True)
            print(f"Opening {app_name}...")
        except Exception as e:
            print(f"Failed to open {app_name}: {e}")
    else:
        print(f"{app_name} is not on the list.")
