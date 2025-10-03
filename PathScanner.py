import os
import json

def scan_applications(directories, file_extension=".exe"):
    apps = {}
    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(file_extension):
                    app_name = os.path.splitext(file)[0].lower()
                    apps[app_name] = os.path.join(root, file)
    return apps

def save_applications_to_file(apps, file_name="vell_mapping.json"):
    with open(file_name, "w") as file:
        json.dump(apps, file, indent=4)
    print(f"Application mapping saved to {file_name}")

def load_applications_from_file(file_name="vell_mapping.json"):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return {}

if __name__ == "__main__":
    directories_to_scan = [
        "C:\\Program Files",
        "C:\\Program Files (x86)",
        "C:\\Users\\YourName\\AppData\\Local",
        "D:\\"
    ]
    print("Scanning for applications...")
    applications = scan_applications(directories_to_scan)
    save_applications_to_file(applications)
    print("Scan complete. Applications found:")
    for app_name, app_path in applications.items():
        print(f"{app_name}: {app_path}")
