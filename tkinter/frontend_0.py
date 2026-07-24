import tkinter as tk 

# Create the main application window

root= tk.Tk()

root.title("Simple Tkinter App")


root.geometry("200x100")


# Function to print "Hello, World! in the console
def say_hello():
    print("Hello, World!")
    

# Create a buttion that triggers the say_say hello function
hello_button = tk.Button(root, text="Click Me", command=say_hello)
hello_button.pack(pady=20)  # Pack the button into the windo


# Start the Tkinter event loop
root.mainloop()



