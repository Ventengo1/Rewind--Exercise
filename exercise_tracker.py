import tkinter as tk
from tkinter import messagebox, Toplevel
import json
import os

DATA_FILE = "exercise_data.json"

def save_exercise(name, duration, notes):
    entry = {"name": name, "duration": duration, "notes": notes}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append(entry)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def view_history():
    if not os.path.exists(DATA_FILE):
        messagebox.showinfo("No Data", "No exercise history yet.")
        return

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    history_window = Toplevel()
    history_window.title("Exercise History")
    history_window.geometry("400x400")

    tk.Label(history_window, text="Your Exercise Log", font=("Arial", 16)).pack(pady=10)

    for entry in data:
        info = f"{entry['name']} - {entry['duration']} min\nNotes: {entry['notes']}\n"
        tk.Label(history_window, text=info, anchor="w", justify="left").pack(pady=5)

def submit():
    name = entry_name.get()
    duration = entry_duration.get()
    notes = text_notes.get("1.0", tk.END).strip()

    if not name or not duration.isdigit():
        messagebox.showerror("Error", "Please enter a valid name and number for duration.")
        return

    save_exercise(name, int(duration), notes)
    messagebox.showinfo("Saved", "Exercise saved successfully!")
    entry_name.delete(0, tk.END)
    entry_duration.delete(0, tk.END)
    text_notes.delete("1.0", tk.END)

# UI Setup
root = tk.Tk()
root.title("Exercise Tracker")
root.geometry("400x400")

tk.Label(root, text="Exercise Tracker", font=("Arial", 18)).pack(pady=10)

tk.Label(root, text="Exercise Name").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Duration (minutes)").pack()
entry_duration = tk.Entry(root, width=40)
entry_duration.pack()

tk.Label(root, text="Notes").pack()
text_notes = tk.Text(root, width=40, height=5)
text_notes.pack()

tk.Button(root, text="Add Exercise", command=submit).pack(pady=10)
tk.Button(root, text="View History", command=view_history).pack()

root.mainloop()
