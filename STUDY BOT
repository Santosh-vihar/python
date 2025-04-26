import tkinter as tk

# Function to process user input and return a response
def get_response(user_input):
    user_input = user_input.lower()

    if "what should i study" in user_input:
        return "Focus on Python and revise your notes."
    elif "remind me to study at" in user_input:
        time = user_input.split("at")[-1].strip()
        return f"Reminder set for {time}!"
    elif "give me a tip" in user_input:
        return "Study in short focused bursts — try the Pomodoro technique!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Stay consistent and keep learning. 🚀"
    else:
        return "Sorry, I didn't understand that. Try asking about study topics or setting a reminder."

# Function to update chat window
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    response = get_response(user_input)
    chat_window.insert(tk.END, "Bot: " + response + "\n\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)
    entry.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("📚 Study Assistant Bot")

chat_window = tk.Text(root, bg="white", height=20, width=50, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5, side=tk.LEFT)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5, side=tk.LEFT)

# Start the GUI loop
root.mainloop()
