from tkinter import END, Button, Canvas, Entry, Frame, Label, Tk

import requests


def shorten_url(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text
        return "Error: Unable to shorten URL."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()


# GUI setup
root = Tk()
root.title("URL Shortener")
root.geometry("450x300")
root.configure(bg="#ffffff")  # Changed to white for cleaner contrast

# Header
header_frame = Frame(root, bg="#0056b3")  # Darker blue for better visibility
header_frame.pack(fill="x", pady=10)

header_label = Label(
    header_frame,
    text="🔗 URL Shortener",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#0056b3",  # White text on dark blue
)
header_label.pack(pady=5)

# Main Frame
main_frame = Frame(root, bg="#f8f9fa", padx=20, pady=20, relief="raised", borderwidth=2)
main_frame.pack(pady=15, padx=20, fill="both", expand=True)

# Input field
Label(
    main_frame, text="Enter URL:", font=("Arial", 12), bg="#f8f9fa", fg="#343a40"
).grid(row=0, column=0, sticky="w")
url_entry = Entry(
    main_frame,
    width=35,
    font=("Arial", 12),
    relief="solid",
    borderwidth=1,
    fg="#212529",  # Dark text color
    bg="#ffffff",  # White background for high contrast
)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Result display with frame
result_frame = Frame(
    main_frame, bg="#ffffff", padx=5, pady=5, relief="groove", borderwidth=1
)
result_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")
result_label = Label(
    result_frame,
    text="",
    font=("Arial", 12),
    fg="#0056b3",
    bg="#ffffff",  # Dark blue text on white
    cursor="hand2",
)
result_label.pack(fill="both", expand=True, padx=5, pady=5)


# Function for shortening the URL and showing the copy button
def get_short_url():
    long_url = url_entry.get()
    if long_url:
        short_url = shorten_url(long_url)
        result_label.config(text=short_url)
        result_label.bind("<Button-1>", lambda e: copy_to_clipboard(short_url))
        copy_button.grid(
            row=2, column=1, pady=10, sticky="e"
        )  # Show the copy button after generating the short URL
    else:
        result_label.config(text="Please enter a valid URL.")


# Clear the entry and result
def clear_fields():
    url_entry.delete(0, END)
    result_label.config(text="")
    copy_button.grid_forget()  # Hide the copy button


# Buttons
button_frame = Frame(main_frame, bg="#f8f9fa")
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

shorten_button = Button(
    button_frame,
    text="Shorten URL",
    command=get_short_url,
    font=("Arial", 10, "bold"),
    bg="#28a745",  # Green for success
    fg="white",
    activebackground="#218838",
    relief="flat",
    padx=10,
    pady=5,
)
shorten_button.grid(row=0, column=0, padx=5)

clear_button = Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    font=("Arial", 10, "bold"),
    bg="#dc3545",  # Red for danger
    fg="white",
    activebackground="#c82333",
    relief="flat",
    padx=10,
    pady=5,
)
clear_button.grid(row=0, column=1, padx=5)

copy_button = Button(
    main_frame,
    text="📋 Copy",
    command=lambda: copy_to_clipboard(result_label.cget("text")),
    font=("Arial", 10, "bold"),
    bg="#0056b3",  # Dark blue for the copy button
    fg="white",
    activebackground="#004085",
    relief="flat",
    padx=10,
    pady=5,
)
copy_button.grid_forget()  # Hide the copy button initially

# Footer
footer_label = Label(
    root,
    text="Made with ❤️ by Janardan Pathak",
    font=("Arial", 10),
    bg="#ffffff",  # Footer on white background
    fg="#6c757d",  # Muted gray text
)
footer_label.pack(pady=5)

root.mainloop()
