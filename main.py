import ttkbootstrap as ttk
from tkinter import messagebox

def Enter_habits():
    global frame2, frame3
    frame2.pack_forget()
    frame3 = ttk.Frame(window)
    frame3.pack(expand=True)
    Enter_habitLabel = ttk.Label(
        frame3,
        text="HOW MANY HABITS DO YOU WANT TO TRACK?",
        font=("Outfit", 14)
    )
    Enter_habitLabel.grid(row=0, column=0, columnspan=2, pady=10)
    Enter_HabitsName=ttk.Entry(
        frame3,
        font=("Outfit", 12),
        width=30
    )
    Enter_HabitsName.grid(row=1, column=0,columnspan=2, pady=20)
def start():
    user_name = question_entry.get()
    if user_name.strip():
        messagebox.showinfo(
            "consistency is key!",
            f"Welcome, {user_name}! Let's start tracking your habits."
        )
    else:
        messagebox.showerror("Error", "Please enter your name!")
        return frame2.pack()
    return Enter_habits()    

def yes():
    global frame2, question_entry

    frame1.pack_forget()

    frame2 = ttk.Frame(window)
    frame2.pack(expand=True)

    question_label = ttk.Label(
        frame2,
        text="What should we call you?",
        font=("Outfit", 14)
    )
    question_label.grid(row=0, column=0, columnspan=2, pady=10)

    question_entry = ttk.Entry(
        frame2,
        font=("Outfit", 12),
        width=25
    )
    question_entry.grid(row=1, column=0, columnspan=2, pady=10)

    start_btn = ttk.Button(
        frame2,
        text="Let's Get Started",
        command=start,
        bootstyle="primary-outline",
        padding=(20, 8),
        
    )
    start_btn.grid(row=2, column=0, columnspan=2, pady=10)
#main window
window = ttk.Window(
    title="Habit Tracker Application",
    themename="flatly",
    size=(850, 450)
)

frame1 = ttk.Frame(window)
frame1.pack(expand=True)

welcome_text = ttk.Label(
    frame1,
    text="Want to gain a new HABIT!?",
    font=("Outfit", 16)
)
welcome_text.grid(row=0, column=0, columnspan=2, pady=10)

interested = ttk.Button(
    frame1,
    text="Yes",
    command=yes,
    bootstyle="success-outline",
    padding=(80, 8)
)
interested.grid(row=1, column=0, columnspan=2, pady=10)

window.mainloop()
