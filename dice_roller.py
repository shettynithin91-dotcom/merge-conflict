import random
import tkinter as tk

DICE_UNICODE = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]


def roll_dice():
    return random.randint(1, 6)


def update_dice():
    value = roll_dice()
    dice_label.config(text=DICE_UNICODE[value - 1])
    result_label.config(text=f"You rolled: {value}")


root = tk.Tk()
root.title("Dice Roller")
root.resizable(False, False)
root.geometry("220x180")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True, fill="both")

dice_label = tk.Label(frame, text=DICE_UNICODE[0], font=("Arial", 60), pady=10, cursor="hand2")
dice_label.pack()
dice_label.bind("<Button-1>", lambda event: update_dice())

result_label = tk.Label(frame, text="Click the dice or button to roll!", font=("Arial", 12))
result_label.pack(pady=(0, 10))

roll_button = tk.Button(frame, text="Roll Dice", command=update_dice, font=("Arial", 12), width=12)
roll_button.pack()

root.mainloop()
