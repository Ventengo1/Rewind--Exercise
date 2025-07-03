import tkinter as tk
import json
import os

def save():
    n = name_entry.get()
    d = duration_entry.get()
    note = note_box.get("1.0", tk.END).strip()

    if not n or not d.isdigit():
        return

    new_data = {"name": n, "duration": d, "note": note}

    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            old = json.load(f)
    else:
        old = []

    old.append(new_data)

    with open("data.json", "w") as f:
        json.dump(old, f)

    name_entry.delete(0, tk.END)
    duration_entry.delete(0, tk.END)
    note_box.delete("1.0", tk.END)

def edit_entry(index):
    with open("data.json", "r") as f:
        all_data = json.load(f)

    e = all_data[index]

    win = tk.Toplevel()
    win.title("Edit Exercise")
    win.geometry("300x300")

    tk.Label(win, text="Name").pack()
    en = tk.Entry(win, width=30)
    en.insert(0, e["name"])
    en.pack()

    tk.Label(win, text="Duration").pack()
    ed = tk.Entry(win, width=30)
    ed.insert(0, e["duration"])
    ed.pack()

    tk.Label(win, text="Note").pack()
    et = tk.Text(win, width=30, height=4)
    et.insert("1.0", e["note"])
    et.pack()

    def save_change():
        new_name = en.get()
        new_dur = ed.get()
        new_note = et.get("1.0", tk.END).strip()

        if not new_name or not new_dur.isdigit():
            return

        all_data[index] = {
            "name": new_name,
            "duration": new_dur,
            "note": new_note
        }

        with open("data.json", "w") as f:
            json.dump(all_data, f)

        win.destroy()

    tk.Button(win, text="Save", command=save_change).pack(pady=10)

def open_log():
    if not os.path.exists("data.json"):
        return

    with open("data.json", "r") as f:
        all_data = json.load(f)

    log = tk.Toplevel()
    log.title("My Exercises")
    log.geometry("400x500")
    log.configure(bg="#f4f4f4")

    tk.Label(log, text="Exercise Log", font=("Arial", 16), bg="#f4f4f4").pack(pady=10)

    for i, e in enumerate(all_data):
        s = e["name"] + " - " + e["duration"] + " min\n" + e["note"]
        frame = tk.Frame(log, bg="#e6f7ff", padx=5, pady=5)
        tk.Label(frame, text=s, bg="#e6f7ff", justify="left", anchor="w", width=40).pack(side="left")
        tk.Button(frame, text="Edit", command=lambda idx=i: edit_entry(idx), bg="#ffc107").pack(side="right")
        frame.pack(pady=5, fill="x", padx=10)

app = tk.Tk()
app.title("Exercise App")
app.geometry("350x450")
app.configure(bg="#e8f0fe")

tk.Label(app, text="Exercise Tracker", font=("Arial", 18), bg="#e8f0fe", fg="#2e64fe").pack(pady=10)

tk.Label(app, text="Name", bg="#e8f0fe").pack()
name_entry = tk.Entry(app, width=30)
name_entry.pack()

tk.Label(app, text="Duration", bg="#e8f0fe").pack()
duration_entry = tk.Entry(app, width=30)
duration_entry.pack()

tk.Label(app, text="Notes", bg="#e8f0fe").pack()
note_box = tk.Text(app, width=30, height=4)
note_box.pack()

tk.Button(app, text="Save", command=save, bg="#4caf50", fg="white", padx=10).pack(pady=10)
tk.Button(app, text="View Log", command=open_log, bg="#2196f3", fg="white", padx=10).pack()

app.bind('<Control-Return>', lambda event: save())

app.mainloop()
