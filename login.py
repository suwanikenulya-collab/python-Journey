from tkinter import *
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("800x600")
        self.root.config(bg="#1e1e2f")
        self.root.resizable(False, False)

        # Login Frame
        frame_login = Frame(self.root, bg="#25253a")
        frame_login.place(x=200, y=80, width=400, height=450)

        # Title
        Label(
            frame_login,
            text="Login System",
            font=("Impact", 35, "bold"),
            bg="#25253a",
            fg="white"
        ).place(x=70, y=30)

        # Subtitle
        Label(
            frame_login,
            text="Members Login Here!",
            font=("Segoe UI", 14),
            bg="#25253a",
            fg="#b0b0b0"
        ).place(x=110, y=100)

        # Username Label
        Label(
            frame_login,
            text="Username",
            font=("Segoe UI", 12, "bold"),
            bg="#25253a",
            fg="white"
        ).place(x=40, y=150)

        # Username Entry
        self.username = Entry(
            frame_login,
            font=("Segoe UI", 12),
            bg="white",
            fg="gray",
            relief=FLAT
        )

        self.username.place(x=40, y=180, width=320, height=35)
        self.username.insert(0, "Enter username")
        self.username.bind("<FocusIn>", self.clear_username)

        # Password Label
        Label(
            frame_login,
            text="Password",
            font=("Segoe UI", 12, "bold"),
            bg="#25253a",
            fg="white"
        ).place(x=40, y=240)

        # Password Entry
        self.password = Entry(
            frame_login,
            font=("Segoe UI", 12),
            bg="white",
            fg="gray",
            relief=FLAT
        )

        self.password.place(x=40, y=270, width=320, height=35)
        self.password.insert(0, "Enter password")
        self.password.bind("<FocusIn>", self.clear_password)

        # 🔥 Show Password Variable
        self.show_password_var = IntVar()

        # Show Password Checkbox
        Checkbutton(
            frame_login,
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password,
            bg="#25253a",
            fg="white",
            activebackground="#25253a",
            activeforeground="white",
            selectcolor="#25253a",
            font=("Segoe UI", 10)
        ).place(x=40, y=310)

        # Login Button
        Button(
            frame_login,
            text="LOGIN",
            font=("Segoe UI", 12, "bold"),
            bg="#4a90e2",
            fg="white",
            relief=FLAT,
            cursor="hand2",
            command=self.check_function
        ).place(x=40, y=340, width=320, height=40)

        # Forgot Password
        Label(
            frame_login,
            text="Forgot Password?",
            font=("Segoe UI", 10, "underline"),
            bg="#25253a",
            fg="#4a90e2",
            cursor="hand2"
        ).place(x=135, y=400)

    # Username Placeholder
    def clear_username(self, event):
        if self.username.get() == "Enter username":
            self.username.delete(0, END)
            self.username.config(fg="black")

    # Password Placeholder
    def clear_password(self, event):
        if self.password.get() == "Enter password":
            self.password.delete(0, END)
            self.password.config(fg="black", show="*")

    # 🔥 Toggle Password Visibility
    def toggle_password(self):
        if self.show_password_var.get() == 1:
            self.password.config(show="")
        else:
            self.password.config(show="*")

    # Login Validation
    def check_function(self):

        username = self.username.get()
        password = self.password.get()

        if username in ("", "Enter username") or password in ("", "Enter password"):
            messagebox.showerror(
                "Error",
                "All fields are required!",
                parent=self.root
            )

        elif username == "tech2etc" and password == "123456":
            messagebox.showinfo(
                "Success",
                "Login Successful!",
                parent=self.root
            )

        else:
            messagebox.showerror(
                "Error",
                "Invalid username or password!",
                parent=self.root
            )


root = Tk()
obj = Login(root)
root.mainloop()