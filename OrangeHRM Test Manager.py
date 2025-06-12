import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import ttk, filedialog
import json
import os

# Default config values
default_config = {
    "drivers_config": {
        "Test_URL": "",
        "Incognito_Mode": "No",
        "Drivers_Type": "Online",
        "Testing_Browser": "Chrome",
        "Headless_mode": False,
        "Show_Report": True,
        "Cross_Browser_Testing": False
    }
}

def select_config_path():
    default_dir = os.path.join(os.getcwd(), "Json_Files")
    os.makedirs(default_dir, exist_ok=True)
    file_path = filedialog.asksaveasfilename(
        initialdir=default_dir,
        initialfile="Config.json",
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")],
        title="Select Config File Location"
    )
    if file_path:
        config_path_var.set(file_path)
        load_or_create_config(file_path)

def load_or_create_config(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default_config, f, indent=4)
        config = default_config["drivers_config"]
    else:
        with open(path, "r") as f:
            data = json.load(f)
            config = data.get("drivers_config", default_config["drivers_config"])
    # Update GUI variables
    url_var.set(config.get("Test_URL", ""))
    incognito_var.set(config.get("Incognito_Mode", "No"))
    drivers_type_var.set(config.get("Drivers_Type", "Online"))
    browser_var.set(config.get("Testing_Browser", "Chrome"))
    headless_var.set(config.get("Headless_mode", False))
    show_report_var.set(config.get("Show_Report", True))
    cross_browser_var.set(config.get("Cross_Browser_Testing", False))
    status_var.set("Config loaded.")

def save_config():
    config = {
        "drivers_config": {
            "Test_URL": url_var.get(),
            "Incognito_Mode": incognito_var.get(),
            "Drivers_Type": drivers_type_var.get(),
            "Testing_Browser": browser_var.get(),
            "Headless_mode": headless_var.get(),
            "Show_Report": show_report_var.get(),
            "Cross_Browser_Testing": cross_browser_var.get()
        }
    }
    config_path = config_path_var.get()
    if not config_path:
        status_var.set("Please select a config file location.")
        return
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)
    status_var.set("Config file saved/updated successfully!")

root = tk.Tk()
root.title("OrangeHRM Test Manager")

# Center the window on the screen
window_width = 650
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Status bar variable and label (create these early)
status_var = tk.StringVar()
status_label = ttk.Label(root, textvariable=status_var, foreground="green")
status_label.pack(side="bottom", fill="x", pady=5)

# Variables
default_config_path = os.path.join(os.getcwd(), "Json_Files", "Config.json")
config_path_var = tk.StringVar(value=default_config_path)
url_var = tk.StringVar()
incognito_var = tk.StringVar(value="No")
drivers_type_var = tk.StringVar(value="Online")
browser_var = tk.StringVar(value="Chrome")
headless_var = tk.BooleanVar(value=False)
show_report_var = tk.BooleanVar(value=True)
cross_browser_var = tk.BooleanVar(value=False)

# Load config (create if not present)
load_or_create_config(config_path_var.get())

# --- Frames for better structure ---
main_frame = ttk.Frame(root, padding=15)
main_frame.pack(fill="both", expand=True)

config_frame = ttk.LabelFrame(main_frame, text="Configuration File", padding=10)
config_frame.pack(fill="x", pady=10)

settings_frame = ttk.LabelFrame(main_frame, text="Test Settings", padding=10)
settings_frame.pack(fill="x", pady=10)

options_frame = ttk.LabelFrame(main_frame, text="Options", padding=10)
options_frame.pack(fill="x", pady=10)

button_frame = ttk.Frame(main_frame)
button_frame.pack(fill="x", pady=10)

# --- Config File Location ---
ttk.Label(config_frame, text="Config File Location:").grid(row=0, column=0, sticky="w")
ttk.Entry(config_frame, textvariable=config_path_var, width=60, state="readonly").grid(row=0, column=1, padx=5)
ttk.Button(config_frame, text="Select Location", command=select_config_path).grid(row=0, column=2, padx=5)

# --- Test Settings ---
ttk.Label(settings_frame, text="Test URL:").grid(row=0, column=0, sticky="w", pady=2)
ttk.Entry(settings_frame, textvariable=url_var, width=80).grid(row=0, column=1, columnspan=2, pady=2)

ttk.Label(settings_frame, text="Incognito Mode:").grid(row=1, column=0, sticky="w", pady=2)
ttk.Combobox(settings_frame, textvariable=incognito_var, values=["Yes", "No"], state="readonly", width=10).grid(row=1, column=1, pady=2, sticky="w")

ttk.Label(settings_frame, text="Drivers Type:").grid(row=2, column=0, sticky="w", pady=2)
ttk.Combobox(settings_frame, textvariable=drivers_type_var, values=["Online", "Offline"], state="readonly", width=10).grid(row=2, column=1, pady=2, sticky="w")

ttk.Label(settings_frame, text="Testing Browser:").grid(row=3, column=0, sticky="w", pady=2)
ttk.Combobox(settings_frame, textvariable=browser_var, values=["Chrome", "Edge", "Firefox"], state="readonly", width=10).grid(row=3, column=1, pady=2, sticky="w")

# --- Options ---
ttk.Checkbutton(options_frame, text="Headless Mode", variable=headless_var).pack(anchor="w", pady=2)
ttk.Checkbutton(options_frame, text="Show Report", variable=show_report_var).pack(anchor="w", pady=2)
ttk.Checkbutton(options_frame, text="Cross Browser Testing", variable=cross_browser_var).pack(anchor="w", pady=2)

# --- Save Button ---
ttk.Button(
    button_frame,
    text="Save Config",
    command=save_config,
    width=30
).pack(fill="x", pady=20, ipady=10, ipadx=5)

root.mainloop()