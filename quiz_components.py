# quiz_components.py - Quiz UI Components Module
# This module contains the MainMenu and QuizPage classes

import tkinter as tk
from tkinter import ttk


class MainMenu(tk.Frame):
    """
    Main menu class that displays the quiz selection interface.
    Shows the logo, title, and buttons for different quiz categories.
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Create a main container frame for centering content
        main_container = tk.Frame(self)
        main_container.pack(expand=True, fill="both")

        # Create content frame that will be centered
        content_frame = tk.Frame(main_container)
        content_frame.pack(expand=True)

        # Try to show logo; if not found, show text fallback
        # Make the logo smaller and centered
        try:
            # Load the original image
            original_logo = tk.PhotoImage(
                file="/Users/diegofoggi/Desktop/Projects/Questionaire/Quiz_Couersework/greenwich_logo.png"
            )
            # Subsample to make it smaller (every 3rd pixel)
            self.img_logo = original_logo.subsample(3, 3)

            # Create logo label and center it
            logo_label = tk.Label(content_frame, image=self.img_logo)
            logo_label.pack(pady=(20, 10))

        except Exception:
            # Fallback to text if image not found
            logo_label = tk.Label(content_frame, text="Greenwich University",
                                  font=("Arial", 16, "bold"), fg="navy")
            logo_label.pack(pady=(20, 10))

        # Main title - centered
        title_label = tk.Label(content_frame, text="Exam Quiz",
                               font=("Arial", 22, "bold"), fg="darkblue")
        title_label.pack(pady=(5, 10))

        # Student info section (if logged in)
        self.create_student_info_section(content_frame)

        # Buttons container - centered
        buttons_frame = tk.Frame(content_frame)
        buttons_frame.pack(pady=10)

        # Create quiz selection buttons
        button_configs = [
            ("Software Engineering", "SoftwareQuiz"),
            ("Logic and Design", "LogicDesignQuiz"),
            ("Algorithm and Data Structure", "AlgorithmQuiz")
        ]

        for button_text, frame_name in button_configs:
            btn = tk.Button(
                buttons_frame,
                text=button_text,
                width=25,
                height=2,
                font=("Arial", 11),
                bg="lightblue",
                fg="darkblue",
                relief="raised",
                bd=2,
                command=lambda name=frame_name: controller.show_frame(name)
            )
            btn.pack(pady=8)

    def create_student_info_section(self, parent):
        """Create section to display logged-in student information"""
        if hasattr(self.controller, 'student_data') and self.controller.student_data:
            student_data = self.controller.student_data

            # Student info frame
            info_frame = tk.Frame(parent, bg="lightblue", relief="solid", bd=1)
            info_frame.pack(pady=(5, 15), padx=20, fill="x")

            # Welcome message
            welcome_text = f"Welcome, {student_data.get('name', 'Student')}!"
            welcome_label = tk.Label(info_frame, text=welcome_text,
                                     font=("Arial", 12, "bold"),
                                     bg="lightblue", fg="darkblue")
            welcome_label.pack(pady=5)

            # Student details
            details_text = f"ID: {student_data.get('id', 'N/A')} | Email: {student_data.get('email', 'N/A')}"
            details_label = tk.Label(info_frame, text=details_text,
                                     font=("Arial", 10),
                                     bg="lightblue", fg="darkblue")
            details_label.pack(pady=(0, 5))

            # Logout button
            logout_btn = tk.Button(info_frame, text="Logout",
                                   font=("Arial", 9),
                                   bg="lightcoral", fg="darkred",
                                   command=self.logout)
            logout_btn.pack(pady=5)

    def logout(self):
        """Handle logout functionality"""
        # Clear student data
        self.controller.student_data = {}

        # Return to login page
        self.controller.show_frame("LoginPage")


class QuizPage(tk.Frame):
    """
    Quiz page class that displays questions and handles user interactions.
    This class creates a quiz page that shows questions and lets users answer them.
    """

    def __init__(self, parent, controller, category_index, title):
        """
        Initialize the quiz page with all necessary components.

        Parameters:
        - parent: The window that will contain this quiz page
        - controller: The main app that controls navigation between pages
        - category_index: Which category of questions to show (like 0, 1, 2...)
        - title: The title to display at the top of the quiz
        """
        # Call the parent class constructor to set up the basic frame
        super().__init__(parent)

        # Store the parameters so we can use them later
        self.controller = controller
        self.category_index = category_index
        self.title_text = title

        # Get the questions for this specific category from the main app
        self.questions = controller.quiz_data[category_index]

        # Count how many questions we have total
        self.total_questions = len(self.questions)

        # Keep track of which question we're currently showing (starts at 0)
        self.current_question = 0

        # Create a list to store the user's answers for each question
        # We start with -1 for each question, which means "no answer selected yet"
        self.user_answers = []
        for i in range(self.total_questions):
            self.user_answers.append(-1)

        # Create the header section (title and progress)
        self.create_header_section()

        # Create the question display area
        self.create_question_section()

        # Create the answer choices area
        self.create_choices_section()

        # Create the feedback message area
        self.create_feedback_section()

        # Create the navigation buttons
        self.create_navigation_buttons()

        # Create the final results display area
        self.create_results_section()

        # Show the first question to start the quiz
        self.show_current_question()

    def create_header_section(self):
        """Create the top section with title and progress indicator"""
        # Create a frame to hold the header elements
        self.header_frame = tk.Frame(self)
        self.header_frame.pack(fill="x", pady=(10, 0))

        # Create the title label and put it on the left side
        self.title_label = tk.Label(self.header_frame, text=self.title_text,
                                    font=("Arial", 18, "bold"), fg="darkblue")
        self.title_label.pack(side="left", padx=12)

        # Create the progress label and put it on the right side
        self.progress_label = tk.Label(self.header_frame, text="",
                                       font=("Arial", 12), fg="gray")
        self.progress_label.pack(side="right", padx=12)

    def create_question_section(self):
        """Create the area where the question text is displayed"""
        self.question_text = tk.Label(self, text="", font=("Arial", 14),
                                      wraplength=520, justify="left", fg="black")
        self.question_text.pack(padx=16, pady=16, anchor="w")

    def create_choices_section(self):
        """Create the area where answer choices (radio buttons) are displayed"""
        # This variable keeps track of which radio button is selected
        self.selected_answer = tk.IntVar()
        self.selected_answer.set(-1)  # Start with no selection

        # Create a container frame for the radio buttons
        self.choices_container = tk.Frame(self)
        self.choices_container.pack(fill="x", padx=24)

        # This list will hold references to all the radio buttons
        self.radio_buttons = []

    def create_feedback_section(self):
        """Create the area where error messages are shown"""
        self.feedback_message = tk.Label(self, text="", fg="red", font=("Arial", 11))
        self.feedback_message.pack(pady=(8, 0))

    def create_navigation_buttons(self):
        """Create the buttons for navigation (Back, Restart, Next)"""
        # Create a frame to hold all the buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(fill="x", pady=20)

        # Back to menu button (left side)
        self.back_button = tk.Button(self.button_frame, text="Back to Menu",
                                     font=("Arial", 10), bg="lightgray",
                                     command=self.go_back_to_menu)
        self.back_button.pack(side="left", padx=10)

        # Restart button (left side, next to back button)
        self.restart_button = tk.Button(self.button_frame, text="Restart",
                                        font=("Arial", 10), bg="lightyellow",
                                        command=self.restart_quiz)
        self.restart_button.pack(side="left")

        # Next/Finish button (right side)
        self.next_button = tk.Button(self.button_frame, text="Next",
                                     font=("Arial", 10), bg="lightgreen",
                                     command=self.go_to_next_question)
        self.next_button.pack(side="right", padx=10)

    def create_results_section(self):
        """Create the area where final quiz results are displayed"""
        self.result_text = tk.Label(self, text="", font=("Arial", 14, "bold"),
                                    fg="darkgreen")
        self.result_text.pack(pady=(0, 6))

    def show_current_question(self):
        """
        This method displays the current question and its answer choices.
        It gets called whenever we need to show a new question.
        """
        # Get the data for the question we're currently showing
        current_q = self.questions[self.current_question]

        # Update the progress indicator (like "Q 1 / 5")
        question_number = self.current_question + 1  # Add 1 because we count from 1, not 0
        progress_text = "Q " + str(question_number) + " / " + str(self.total_questions)
        self.progress_label.config(text=progress_text)

        # Update the question text
        self.question_text.config(text=current_q["question"])

        # Remove any old radio buttons from previous questions
        for widget in self.choices_container.winfo_children():
            widget.destroy()
        self.radio_buttons = []  # Clear our list of radio button references

        # If the user already answered this question before, show their previous answer
        self.selected_answer.set(self.user_answers[self.current_question])

        # Create new radio buttons for each answer choice
        choice_index = 0
        for choice_text in current_q["choices"]:
            radio_button = tk.Radiobutton(
                self.choices_container,  # Put it in the choices container
                text=choice_text,  # The text to display
                variable=self.selected_answer,  # Which variable tracks the selection
                value=choice_index,  # The value this button represents
                anchor="w",  # Align text to the left
                justify="left",  # Justify text to the left
                wraplength=520,  # Wrap long text
                font=("Arial", 11),  # Font for choices
                fg="darkblue"  # Text color
            )
            radio_button.pack(fill="x", pady=4, anchor="w")  # Add it to the container
            self.radio_buttons.append(radio_button)  # Keep a reference to it
            choice_index = choice_index + 1  # Move to next choice

        # Clear any old feedback or result messages
        self.feedback_message.config(text="")
        self.result_text.config(text="")

        # Update the next button text depending on if this is the last question
        if self.current_question == self.total_questions - 1:
            self.next_button.config(text="Finish")  # Last question gets "Finish"
        else:
            self.next_button.config(text="Next")  # Other questions get "Next"

        # Make sure the next button is clickable
        self.next_button.config(state="normal")

        # Make sure all radio buttons are clickable
        self.enable_answer_choices()

    def enable_answer_choices(self):
        """Make all radio buttons clickable"""
        for radio_button in self.radio_buttons:
            radio_button.config(state="normal")

    def disable_answer_choices(self):
        """Make all radio buttons unclickable (used when quiz is finished)"""
        for radio_button in self.radio_buttons:
            radio_button.config(state="disabled")

    def calculate_final_score(self):
        """
        Calculate how many questions the user got right.
        Returns the number of correct answers.
        """
        correct_answers = 0

        # Go through each question and check if the user got it right
        question_index = 0
        for question in self.questions:
            # Get what the user selected for this question
            user_choice_index = self.user_answers[question_index]

            # Only check if the user actually selected something
            if user_choice_index != -1:
                # Get the text of what the user selected
                user_choice_text = question["choices"][user_choice_index]
                # Get the correct answer
                correct_answer = question["answer"]
                # Check if they match
                if user_choice_text == correct_answer:
                    correct_answers = correct_answers + 1

            question_index = question_index + 1

        return correct_answers

    def go_to_next_question(self):
        """
        This method runs when the user clicks the Next or Finish button.
        It either moves to the next question or finishes the quiz.
        """
        # Check if the user selected an answer
        selected_choice = self.selected_answer.get()
        if selected_choice == -1:
            # If no answer selected, show an error message and don't continue
            self.feedback_message.config(text="Please select an option before continuing.")
            return

        # Save the user's answer for this question
        self.user_answers[self.current_question] = selected_choice

        # Check if this is the last question
        if self.current_question == self.total_questions - 1:
            # Quiz is finished - calculate and show the final score
            final_score = self.calculate_final_score()
            score_text = "Your score: " + str(final_score) + " / " + str(self.total_questions)
            self.result_text.config(text=score_text)

            # Disable the next button and radio buttons since quiz is done
            self.next_button.config(state="disabled")
            self.disable_answer_choices()
        else:
            # Not the last question - move to the next one
            self.current_question = self.current_question + 1
            self.show_current_question()

    def restart_quiz(self):
        """
        Reset the quiz back to the beginning.
        This clears all answers and goes back to the first question.
        """
        # Go back to the first question
        self.current_question = 0

        # Clear all the user's answers
        for i in range(self.total_questions):
            self.user_answers[i] = -1

        # Show the first question again
        self.show_current_question()

    def go_back_to_menu(self):
        """
        Go back to the main menu.
        We restart the quiz first so it's fresh if the user comes back later.
        """
        # Reset the quiz so it's clean next time
        self.restart_quiz()
        # Tell the main app to show the main menu
        self.controller.show_frame("MainMenu")

