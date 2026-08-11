import tkinter as tk
from tkinter import messagebox
import random
import time

class SnakeWaterGunPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Water Gun - Professional Edition")
        self.root.geometry("600x700")
        self.root.configure(bg="#0f111a")
        self.root.resizable(False, False)

        self.user_score = 0
        self.comp_score = 0
        self.choices = ["Snake", "Water", "Gun"]
        self.emoji_map = {"Snake": "🐍", "Water": "💧", "Gun": "🔫"}

        self.setup_ui()

    def setup_ui(self):
        # Header Section
        self.header = tk.Label(
            self.root, text="SNAKE WATER GUN",
            font=("Inter", 28, "bold"), fg="#61afef", bg="#0f111a", pady=30
        )
        self.header.pack()

        # Score Board
        self.score_frame = tk.Frame(self.root, bg="#1a1b26", bd=0)
        self.score_frame.pack(pady=10, fill="x", padx=50)

        self.user_score_label = tk.Label(
            self.score_frame, text=f"PLAYER: {self.user_score}",
            font=("Inter", 14, "bold"), fg="#ffffff", bg="#1a1b26", padx=20, pady=20
        )
        self.user_score_label.pack(side="left")

        self.comp_score_label = tk.Label(
            self.score_frame, text=f"COMPUTER: {self.comp_score}",
            font=("Inter", 14, "bold"), fg="#ffffff", bg="#1a1b26", padx=20, pady=20
        )
        self.comp_score_label.pack(side="right")

        # Visual Display Area
        self.display_canvas = tk.Frame(self.root, bg="#0f111a", pady=40)
        self.display_canvas.pack()

        self.result_main = tk.Label(
            self.display_canvas, text="VS",
            font=("Inter", 60), fg="#333", bg="#0f111a"
        )
        self.result_main.pack()

        self.status_msg = tk.Label(
            self.root, text="Select your weapon to begin",
            font=("Inter", 12), fg="#9aa0a6", bg="#0f111a"
        )
        self.status_msg.pack(pady=10)

        # Controls Section
        self.controls = tk.Frame(self.root, bg="#0f111a")
        self.controls.pack(side="bottom", pady=50)

        self.create_button("Snake", "#e06c75", self.controls)
        self.create_button("Water", "#61afef", self.controls)
        self.create_button("Gun", "#98c379", self.controls)

    def create_button(self, name, color, parent):
        btn = tk.Button(
            parent, text=f"{self.emoji_map[name]} {name}",
            font=("Inter", 12, "bold"), fg="#ffffff", bg=color,
            activebackground="#ffffff", activeforeground=color,
            width=12, height=2, bd=0, cursor="hand2",
            command=lambda: self.play(name)
        )
        btn.pack(side="left", padx=10)
        btn.bind("<Enter>", lambda e: btn.config(bg="#ffffff", fg=color))
        btn.bind("<Leave>", lambda e: btn.config(bg=color, fg="#ffffff"))

    def play(self, user_choice):
        comp_choice = random.choice(self.choices)
        
        # UI "Thinking" effect
        self.result_main.config(text="...", fg="#61afef")
        self.root.update()
        time.sleep(0.4)

        result_text = ""
        result_color = "#ffffff"

        if user_choice == comp_choice:
            result_text = "IT'S A DRAW"
            result_color = "#9aa0a6"
        else:
            if (user_choice == "Snake" and comp_choice == "Water") or \
               (user_choice == "Water" and comp_choice == "Gun") or \
               (user_choice == "Gun" and comp_choice == "Snake"):
                result_text = "YOU WIN!"
                result_color = "#98c379"
                self.user_score += 1
            else:
                result_text = "COMPUTER WINS"
                result_color = "#e06c75"
                self.comp_score += 1

        self.update_ui(user_choice, comp_choice, result_text, result_color)

    def update_ui(self, u_choice, c_choice, res, color):
        # Update Big Display
        display_str = f"{self.emoji_map[u_choice]}  VS  {self.emoji_map[c_choice]}"
        self.result_main.config(text=display_str, fg="#ffffff")
        
        # Update Message and Scores
        self.status_msg.config(text=res, fg=color, font=("Inter", 16, "bold"))
        self.user_score_label.config(text=f"PLAYER: {self.user_score}")
        self.comp_score_label.config(text=f"COMPUTER: {self.comp_score}")

        # Check for Match Win (First to 5)
        if self.user_score == 5 or self.comp_score == 5:
            winner = "Player" if self.user_score == 5 else "Computer"
            messagebox.showinfo("Game Over", f"{winner} has won the match!")
            self.reset_game()

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.user_score_label.config(text="PLAYER: 0")
        self.comp_score_label.config(text="COMPUTER: 0")
        self.result_main.config(text="VS", fg="#333")
        self.status_msg.config(text="Select your weapon to begin", fg="#9aa0a6")

if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeWaterGunPro(root)
    root.mainloop()