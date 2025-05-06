import tkinter as tk
from tkinter import messagebox, ttk

questions = [
    ("Do you feel very happy today?", "Happy"),
    ("Are you feeling emotionally low?", "Sad"),
    ("Do you feel stressed or anxious?", "Stressed"),
    ("Do you want to go on an adventure?", "Adventurous"),
    ("Are you feeling romantic?", "Romantic"),
    ("Do you feel highly motivated?", "Motivated"),
    ("Are you in a calm or peaceful state of mind?", "Calm"),
    ("Do you want to read something inspiring?", "Motivated"),
    ("Do you feel like escaping reality through imagination?", "Adventurous"),
    ("Are you in the mood for something emotional?", "Sad"),
    ("Do you want to laugh and stay cheerful?", "Happy"),
    ("Do you want to relax with a light read?", "Calm")
]

mood_books = {
    "Happy": [
        "The Alchemist", "Eleanor Oliphant is Completely Fine", "Wonder",
        "The Rosie Project", "You Are a Badass"
    ],
    "Sad": [
        "The Fault in Our Stars", "A Man Called Ove", "It’s Kind of a Funny Story",
        "Norwegian Wood", "The Perks of Being a Wallflower"
    ],
    "Stressed": [
        "Ikigai", "The Power of Now", "Atomic Habits",
        "Meditations", "The Art of Happiness"
    ],
    "Adventurous": [
        "Into the Wild", "Life of Pi", "The Hobbit",
        "Around the World in 80 Days", "Wild"
    ],
    "Romantic": [
        "Pride and Prejudice", "Me Before You", "The Notebook",
        "Outlander", "Love in the Time of Cholera"
    ],
    "Motivated": [
        "Can't Hurt Me", "Grit", "Start with Why",
        "Deep Work", "Drive"
    ],
    "Calm": [
        "The Little Prince", "Tuesdays with Morrie", "The Secret Garden",
        "Big Magic", "The Wind in the Willows"
    ]
}

class ScrollableFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        canvas = tk.Canvas(self, bg="#ffffff", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class MoodBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Mood Book Generator")
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f0f0")

        title = tk.Label(root, text="📚 Mood Book Generator", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        # Create scrollable area
        container = ScrollableFrame(root)
        container.pack(fill="both", expand=True, padx=20, pady=10)

        self.vars = []
        for idx, (q, _) in enumerate(questions):
            q_frame = ttk.LabelFrame(container.scrollable_frame, text=f"Question {idx+1}", padding=(10,5))
            q_frame.pack(fill="x", padx=5, pady=5)

            q_label = tk.Label(q_frame, text=q, font=("Helvetica", 12), bg="white", anchor="w", justify="left", wraplength=550)
            q_label.pack(fill="x", padx=5, pady=2)

            var = tk.StringVar(value="None")
            yes_btn = tk.Radiobutton(q_frame, text="Yes", variable=var, value="Yes", bg="white")
            no_btn = tk.Radiobutton(q_frame, text="No", variable=var, value="No", bg="white")
            yes_btn.pack(anchor="w", padx=20)
            no_btn.pack(anchor="w", padx=20)

            self.vars.append(var)

        submit_btn = tk.Button(root, text="Get Recommendations", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=self.recommend_books)
        submit_btn.pack(pady=15)

    def recommend_books(self):
        mood_score = {}
        for (question, mood), var in zip(questions, self.vars):
            answer = var.get()
            if answer == "Yes":
                mood_score[mood] = mood_score.get(mood, 0) + 1

        if any(v.get() == "None" for v in self.vars):
            messagebox.showwarning("Incomplete", "Please answer all questions.")
            return

        if not mood_score:
            messagebox.showinfo("No Mood", "Could not detect your mood.")
            return

        top_mood = max(mood_score, key=mood_score.get)
        books = mood_books[top_mood][:5 + mood_score[top_mood] % 6]
        book_list = "\n".join(f"• {book}" for book in books)

        messagebox.showinfo("Recommended Books", f"🧠 Detected Mood: {top_mood}\n\n📘 Your Book Recommendations:\n\n{book_list}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MoodBookApp(root)
    root.mainloop()
