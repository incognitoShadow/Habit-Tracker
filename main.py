import tkinter as tk
from tkinter import messagebox
def Start():
    user_name = question_entry.get()
    if user_name.strip():
        frame2.pack_forget()
        messagebox.showinfo("Welcome", f"Welcome, {user_name}! Let's start tracking your habits.")
    else:
        messagebox.showerror("Error", "Please enter your name!")

def yes():
    global frame2, question_entry
    frame1.pack_forget()
    frame2 = tk.Frame(window, bg="#FFFEFA")
    frame2.pack(pady=20)

    question_label = tk.Label(frame2, text="What should we call you ?", bg="#FFFEFA", fg="#5A5B34", font=("Outfit", 14))
    question_entry = tk.Entry(frame2, bg = "#F6FFD7")
    question_entry.grid(row=1, column=0, columnspan=2, pady=10)
    question_label.grid(row=0, column=0, columnspan=2, pady=10)

    Start_btn = tk.Button(frame2, text="Let's Get Started", bg="#5A5B34", fg="#FFFEFA", font=("Outfit", 8), command=Start)
    Start_btn.grid(row=2, column=0, columnspan=2, pady=10)

window = tk.Tk()
window.title("Habit Tracker Application")
window.geometry("400x300")
window.config(bg="#FFFEFA")

frame1 = tk.Frame(window, bg="#FFFEFA")
frame1.pack(pady=20)

welcome_Text = tk.Label(frame1, text="Want to gain a new HABIT!?", bg="#FFFEFA", fg="#5A5B34", font=("Outfit", 16))
intrested = tk.Button(frame1, text="Yes", command=yes, bg="#5A5B34", fg="#FFFEFA", font=("Outfit", 8))

welcome_Text.grid(row=0, column=0, columnspan=2, pady=10)
intrested.grid(row=1, column=0, columnspan=2, pady=10)

window.mainloop()
