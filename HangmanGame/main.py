import tkinter as tk
import random

# List of words for the game
words = ['python', 'hangman', 'programming', 'developer', 'challenge']

# Select a random word
word = random.choice(words)
guessed_word = ['_'] * len(word)
attempts = 6


# Function to display the hangman figure
def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    return stages[6 - attempts]


# Function to update the guessed word display
def update_display_word():
    word_label.config(text=" ".join(
        [f"{letter}" if letter == '_' else f"{letter}" for letter in guessed_word]
    ))


# Initialize the Tkinter GUI application
app = tk.Tk()
app.title('Hangman Game')
app.configure(bg='#1a1a1a')  # Background color

# GUI Elements
hangman_label = tk.Label(app, text=display_hangman(attempts), font=('Courier', 14), fg='#39FF14', bg='#1a1a1a',
                         justify=tk.LEFT, anchor='w')
hangman_label.pack(pady=10, padx=10, anchor='center')

word_label = tk.Label(app, text=" ".join(guessed_word), font=('Helvetica', 20, 'italic'), fg='#F0E68C', bg='#1a1a1a')
word_label.pack(pady=10, padx=10, anchor='center')

attempts_label = tk.Label(app, text=f'Attempts Remaining: {attempts}', font=('Helvetica', 16), fg='#F0E68C',
                          bg='#1a1a1a')
attempts_label.pack(pady=10, padx=10, anchor='center')

guess_entry = tk.Entry(app, font=('Helvetica', 20), width=2, justify='center')
guess_entry.pack(pady=5, padx=10, anchor='center')  # Reduced pady here

feedback_label = tk.Label(app, text="", font=('Helvetica', 16, 'italic'), fg='#FF6347', bg='#1a1a1a')
feedback_label.pack(pady=10, padx=10, anchor='center')


# Function to handle guesses
def make_guess():
    global attempts
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if guess in guessed_word:
        feedback_label.config(text="You already guessed that letter.")
    elif guess in word:
        feedback_label.config(text=f"Good guess! '{guess}' is in the word.")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
        update_display_word()  # Update the display of guessed letters
    else:
        feedback_label.config(text=f"Sorry, '{guess}' is not in the word.")
        attempts -= 1
        attempts_label.config(text=f'Attempts Remaining: {attempts}')

    hangman_label.config(text=display_hangman(attempts))

    if '_' not in guessed_word:
        feedback_label.config(text="Congratulations! You won!", fg='#00FF00')
        guess_entry.config(state=tk.DISABLED)
    elif attempts == 0:
        feedback_label.config(text=f"Game Over! The word was '{word}'.", fg='#FF4500')
        guess_entry.config(state=tk.DISABLED)


# Button to submit guess
guess_button = tk.Button(app, text="Guess", command=make_guess, font=('Helvetica', 16), bg='#F0E68C', fg='#1a1a1a',
                         relief='raised', borderwidth=3)
guess_button.pack(pady=10, padx=10, anchor='center')  # Increased pady here

# Start the GUI event loop
app.mainloop()
