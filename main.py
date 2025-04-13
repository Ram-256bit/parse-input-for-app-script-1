import tkinter as tk
from tkinter import scrolledtext, messagebox


def process_text(input_text):
    lines = input_text.splitlines()
    processed = ",".join(f'"{line.strip()}"' for line in lines) + ","
    return processed


def paste_from_clipboard():
    try:
        clipboard_text = window.clipboard_get()
        input_box.delete("1.0", tk.END)
        input_box.insert(tk.END, clipboard_text)

        # Automatically process and copy the output to clipboard
        processed_text = process_text(clipboard_text)
        window.clipboard_clear()
        window.clipboard_append(processed_text)

        # Update the formatted output text box with the processed text
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, processed_text)

        # Update success message
        success_label.config(text="Successfully copied output to clipboard", fg="green")
        # Hide the success message after 2 seconds
        window.after(2000, hide_success_message)

    except tk.TclError:
        messagebox.showwarning("Clipboard Error", "No text found in clipboard.")


def process_button_action():
    input_text = input_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("No Input", "Please enter some text.")
        return
    processed_text = process_text(input_text)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, processed_text)


def copy_to_clipboard():
    output_text = output_box.get("1.0", tk.END).strip()
    if not output_text:
        messagebox.showwarning("No Output", "Nothing to copy.")
        return
    window.clipboard_clear()
    window.clipboard_append(output_text)

    # Update success message
    success_label.config(text="Successfully copied output to clipboard", fg="green")
    # Hide the success message after 2 seconds
    window.after(2000, hide_success_message)


def hide_success_message():
    success_label.config(text="")


def clear_input():
    input_box.delete("1.0", tk.END)


# GUI Setup
window = tk.Tk()
window.title("Text Formatter")
window.geometry("600x450")
window.resizable(False, False)

# Input Label and Box
tk.Label(window, text="Enter your text (one per line):").pack(pady=5)
input_box = scrolledtext.ScrolledText(window, width=70, height=10)
input_box.pack(padx=10)

# Buttons under input
button_frame = tk.Frame(window)
button_frame.pack(pady=5)
tk.Button(
    button_frame, text="Paste from Clipboard and Process", command=paste_from_clipboard
).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Process", command=process_button_action).pack(
    side=tk.LEFT, padx=5
)
tk.Button(button_frame, text="Clear Input", command=clear_input).pack(
    side=tk.LEFT, padx=5
)

# Output Label and Box
tk.Label(window, text="Formatted Output:").pack(pady=5)
output_box = scrolledtext.ScrolledText(window, width=70, height=5)
output_box.pack(padx=10)

# Copy output button
tk.Button(window, text="Copy Output to Clipboard", command=copy_to_clipboard).pack(
    pady=10
)

# Success Label
success_label = tk.Label(window, text="", fg="green")
success_label.pack(pady=5)

# Run the App
window.mainloop()
