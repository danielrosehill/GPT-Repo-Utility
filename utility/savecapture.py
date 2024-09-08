import os
import time
import tkinter as tk
from tkinter import messagebox

def save_file():
    choice = var.get()
    
    # Get the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Determine the save path based on the user's choice
    if choice == 1:
        save_path = os.path.join(script_dir, "../Module/Outputs/thismonth")
    elif choice == 2:
        save_path = os.path.join(script_dir, "../Module/Prompts/thismonth")
    elif choice == 3:
        save_path = os.path.join(script_dir, "../Module/Configs/thismonth")
    else:
        messagebox.showerror("Error", "Invalid choice. Please select an option.")
        return
    
    # Get the text to save
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Text input cannot be empty.")
        return
    
    # Get the file name
    file_name = file_name_entry.get().strip()
    if not file_name:
        messagebox.showerror("Error", "File name cannot be empty.")
        return
    
    file_name = file_name.replace(" ", "_")  # Replace spaces with underscores
    
    # Generate the final file name with a timestamp
    timestamp = time.strftime("%Y%m%d%H%M%S")
    final_file_name = f"{file_name}{timestamp}.md"
    
    try:
        # Ensure the save directory exists
        os.makedirs(save_path, exist_ok=True)
        
        # Save the text to the file
        file_path = os.path.join(save_path, final_file_name)
        with open(file_path, "w") as file:
            file.write(text)
        
        messagebox.showinfo("Success", f"File saved successfully as {final_file_name} in {save_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the file: {e}")
    
    ask_to_continue()

def ask_to_continue():
    # Ask the user if they want to save something else
    answer = messagebox.askyesno("Continue", "Would you like to save something else?")
    
    if not answer:
        root.destroy()  # Close the GUI if the user says no
    else:
        reset_form()  # Reset the form if the user says yes

def reset_form():
    # Reset the form fields for the next input
    var.set(0)
    file_name_entry.delete(0, tk.END)
    text_input.delete("1.0", tk.END)

# Create the main application window
root = tk.Tk()
root.title("Save File GUI")

# Create and place widgets
tk.Label(root, text="What do you want to save?").pack(anchor=tk.W)

var = tk.IntVar()
tk.Radiobutton(root, text="1. Output", variable=var, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="2. Prompt", variable=var, value=2).pack(anchor=tk.W)
tk.Radiobutton(root, text="3. Custom GPT Configuration", variable=var, value=3).pack(anchor=tk.W)

tk.Label(root, text="Enter a name for the file:").pack(anchor=tk.W)
file_name_entry = tk.Entry(root, width=50)
file_name_entry.pack(anchor=tk.W)

tk.Label(root, text="Paste the text you want to save:").pack(anchor=tk.W)
text_input = tk.Text(root, height=10, width=50)
text_input.pack(anchor=tk.W)

save_button = tk.Button(root, text="Save File", command=save_file)
save_button.pack(anchor=tk.W)

# Run the application
root.mainloop()
