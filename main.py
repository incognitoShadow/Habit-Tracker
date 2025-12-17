import ttkbootstrap as ttk
from tkinter import messagebox
import json
from datetime import date

# ================= JSON STORAGE =================
DATA_FILE = "habits_data.json"

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# ================= HABIT ENTRY SCREEN =================
def enter_habits():
    global frame4, habit_entries

    try:
        habits_count = int(habits_num_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    if habits_count <= 0:
        messagebox.showerror("Error", "Number must be greater than 0!")
        return

    frame3.pack_forget()
    frame4 = ttk.Frame(window)
    frame4.pack(expand=True)

    habit_entries = []

    for i in range(habits_count):
        ttk.Label(
            frame4,
            text=f"Enter Habit {i + 1}:",
            font=("Outfit", 12)
        ).grid(row=i, column=0, pady=10, sticky="e")

        entry = ttk.Entry(frame4, width=30)
        entry.grid(row=i, column=1, pady=10, padx=10)
        habit_entries.append(entry)

    ttk.Button(
        frame4,
        text="Save Habits",
        command=save_habits,
        bootstyle="success-outline",
        padding=(20, 8)
    ).grid(row=habits_count, column=0, columnspan=2, pady=20)

# ================= SAVE HABITS =================
def save_habits():
    habits = {}

    for entry in habit_entries:
        habit = entry.get().strip()
        if habit:
            habits[habit] = {"completed_dates": []}

    if not habits:
        messagebox.showerror("Error", "Please enter at least one habit!")
        return

    data = {
        "username": user_name,
        "habits": habits
    }

    save_data(data)
    messagebox.showinfo("Saved", "Habits saved successfully!")
    show_tracker()

# ================= TRACKING SCREEN =================
def show_tracker():
    global frame5, habit_buttons

    frame4.pack_forget()
    frame5 = ttk.Frame(window)
    frame5.pack(expand=True)

    data = load_data()
    today = str(date.today())
    habit_buttons = {}

    ttk.Label(
        frame5,
        text=f"Hello {data['username']} 👋\nMark habits completed today",
        font=("Outfit", 14),
        justify="center"
    ).pack(pady=15)

    for habit, info in data["habits"].items():
        completed_today = today in info["completed_dates"]

        btn = ttk.Button(
            frame5,
            text=habit,
            padding=(40, 8),
            bootstyle="success" if completed_today else "info-outline",
            state="disabled" if completed_today else "normal",
            command=lambda h=habit: mark_done(h)
        )
        btn.pack(pady=6)
        habit_buttons[habit] = btn

# ================= MARK HABIT DONE =================
def mark_done(habit):
    data = load_data()
    today = str(date.today())

    if today not in data["habits"][habit]["completed_dates"]:
        data["habits"][habit]["completed_dates"].append(today)
        save_data(data)

        # Change button color + disable
        btn = habit_buttons[habit]
        btn.config(bootstyle="success", state="disabled")

        messagebox.showinfo("Done!", f"'{habit}' completed for today 🎉")
    else:
        messagebox.showwarning(
            "Already Done",
            f"You already completed '{habit}' today!"
        )

# ================= HABITS NUMBER SCREEN =================
def Enter_habitsNum():
    global frame3, habits_num_entry

    frame2.pack_forget()
    frame3 = ttk.Frame(window)
    frame3.pack(expand=True)

    ttk.Label(
        frame3,
        text="HOW MANY HABITS DO YOU WANT TO TRACK?",
        font=("Outfit", 14)
    ).grid(row=0, column=0, columnspan=2, pady=10)

    habits_num_entry = ttk.Entry(frame3, width=30)
    habits_num_entry.grid(row=1, column=0, columnspan=2, pady=20)

    ttk.Button(
        frame3,
        text="Track Habits",
        command=enter_habits,
        bootstyle="primary-outline",
        padding=(20, 8)
    ).grid(row=2, column=0, columnspan=2, pady=10)

# ================= START BUTTON =================
def start():
    global user_name
    user_name = question_entry.get()

    if not user_name.strip():
        messagebox.showerror("Error", "Please enter your name!")
        return

    messagebox.showinfo(
        "Consistency is key!",
        f"Welcome, {user_name}! Let's start tracking your habits."
    )
    Enter_habitsNum()

# ================= NAME SCREEN =================
def yes():
    global frame2, question_entry

    frame1.pack_forget()
    frame2 = ttk.Frame(window)
    frame2.pack(expand=True)

    ttk.Label(
        frame2,
        text="What should we call you?",
        font=("Outfit", 14)
    ).grid(row=0, column=0, columnspan=2, pady=10)

    question_entry = ttk.Entry(frame2, width=25)
    question_entry.grid(row=1, column=0, columnspan=2, pady=10)

    ttk.Button(
        frame2,
        text="Let's Get Started",
        command=start,
        bootstyle="primary-outline",
        padding=(20, 8)
    ).grid(row=2, column=0, columnspan=2, pady=10)

# ================= MAIN WINDOW =================
window = ttk.Window(
    title="Habit Tracker Application",
    themename="flatly",
    size=(850, 450)
)

frame1 = ttk.Frame(window)
frame1.pack(expand=True)

ttk.Label(
    frame1,
    text="Want to gain a new HABIT!?",
    font=("Outfit", 16)
).grid(row=0, column=0, columnspan=2, pady=10)

ttk.Button(
    frame1,
    text="Yes",
    command=yes,
    bootstyle="success-outline",
    padding=(80, 8)
).grid(row=1, column=0, columnspan=2, pady=10)

window.mainloop()
