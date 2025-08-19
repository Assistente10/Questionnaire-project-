# login_app.py - Login Application Module
# This module contains the user's exact login code with logo integration

from tkinter import *
from tkinter import messagebox


class App(Tk):
    def __init__(self):
        super().__init__()

        # Title, icon, size
        self.title("Greenwich University Project")
        self.iconbitmap("/Users/diegofoggi/Desktop/Projects/Questionaire/Quiz_Couersework/greenwich_logo.ico")
        self.geometry("800x600")

        # Add logo image (smaller and centered)
        try:
            # Load the logo image
            original_logo = PhotoImage(
                file="/Users/diegofoggi/Desktop/Projects/Questionaire/Quiz_Couersework/greenwich_logo.png"
            )
            # Make it smaller (subsample by 3)
            self.logo_image = original_logo.subsample(3, 3)

            # Create logo label and center it
            self.logo_label = Label(self, image=self.logo_image)
            self.logo_label.pack(pady=(20, 10))

        except Exception:
            # Fallback to text if image not found
            self.logo_label = Label(self, text="Greenwich University",
                                    font=("Arial", 16, "bold"))
            self.logo_label.pack(pady=(20, 10))

        # Create widgets:
        # Create a Label for the widget.
        self.title_label = Label(self, text="Exam Quiz", font=("Arial", 24, "bold"), padx=5, pady=5)
        self.title_label.pack()

        # Ask the user to enter data.
        self.info_label = Label(self, text="Enter your student data below.", font=("Arial", 18), padx=5, pady=5)
        self.info_label.pack()

        # Display the prompts:
        self.prompt_name = Label(self, text="Enter your full name: ", font=("Arial", 14), padx=5, pady=5)
        self.name_entry = Entry(self)
        self.prompt_name.pack()
        self.name_entry.pack()

        self.prompt_email = Label(self, text="Enter your email: ", font=("Arial", 14), padx=5, pady=5)
        self.email_entry = Entry(self)
        self.prompt_email.pack()
        self.email_entry.pack()

        self.prompt_id = Label(self, text="Enter your ID: ", font=("Arial", 14), padx=5, pady=5)
        self.id_entry = Entry(self)
        self.prompt_id.pack()
        self.id_entry.pack()

        # Add login button
        self.login_button = Button(self, text="Login to Quiz", font=("Arial", 12, "bold"),
                                   command=self.handle_login, padx=10, pady=5)
        self.login_button.pack(pady=20)

        # Store student data
        self.student_data = {}

    def handle_login(self):
        """Handle the login process"""
        # Get the entered data
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        student_id = self.id_entry.get().strip()

        # Basic validation
        if not name or not email or not student_id:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Store student data
        self.student_data = {
            "name": name,
            "email": email,
            "id": student_id
        }

        # Show success message
        messagebox.showinfo("Login Successful", f"Welcome {name}!\nStarting quiz application...")

        # Close login window and start main quiz app
        self.destroy()
        self.start_quiz_app()

    def start_quiz_app(self):
        """Start the main quiz application"""
        try:
            # Import and start the main quiz application
            from app import create_app
            quiz_app = create_app()

            # Pass student data to the quiz app
            quiz_app.student_data = self.student_data

            # Start the quiz app
            quiz_app.mainloop()

        except ImportError:
            messagebox.showerror("Error", "Could not load quiz application. Please ensure app.py is available.")


def create_login_app():
    """Create and return a login app instance"""
    return App()


def run_login_app():
    """Run the login application"""
    app = create_login_app()
    app.mainloop()


# If this module is run directly, start the login app
if __name__ == "__main__":
    run_login_app()