# app.py - Main Application Controller Module
# This module contains the App class and quiz data (works with login_app.py)

import tkinter as tk
from quiz_components import MainMenu, QuizPage


class App(tk.Tk):
    """
    Main application controller class.
    This class manages the quiz data and handles navigation between different pages.
    """

    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.title("Greenwich University Project - Quiz")

        # Student data storage (will be set by login app)
        self.student_data = {}

        # ===== QUIZ DATA (3 categories) =====
        # Category 0 -> Software Quiz
        # Category 1 -> System/Patterns Quiz
        # Category 2 -> Algorithm/Data Structures Quiz
        self.quiz_data = [
            [
                {
                    "question": "What are the characteristics of software?",
                    "choices": [
                        "Software is developed or engineered; it is not manufactured in the classical sense.",
                        "Software doesn't wear out.",
                        "Software can be custom built or custom build.",
                        "All mentioned above",
                    ],
                    "answer": "All mentioned above",
                },
                {
                    "question": "Compilers, Editors software come under which type of software?",
                    "choices": [
                        "System software",
                        "Application software",
                        "Scientific software",
                        "None of the above",
                    ],
                    "answer": "System software",
                },
                {
                    "question": "Software Engineering is defined as a systematic, disciplined and quantifiable approach for the development, operation and maintenance of software.",
                    "choices": [
                        "True",
                        "False",
                    ],
                    "answer": "True",
                },
                {
                    "question": "Software consists of ______ .",
                    "choices": [
                        "Set of instructions + operating procedures",
                        "Programs + hardware manuals",
                        "Programs + documentation + operating procedures",
                        "Set of programs",
                    ],
                    "answer": "Programs + documentation + operating procedures",
                },
                {
                    "question": "RAD Software process model stands for _____",
                    "choices": [
                        "Rapid Application Development.",
                        "Relative Application Development.",
                        "Rapid Application Design.",
                        "Recent Application Development.",
                    ],
                    "answer": "Rapid Application Development.",
                },
                {
                    "question": "Software project management comprises of a number of activities, which contains_________.",
                    "choices": [
                        "Project planning",
                        "Scope management",
                        "Project estimation",
                        "All mentioned above",
                    ],
                    "answer": "All mentioned above",
                },
                {
                    "question": "COCOMO stands for ______ .",
                    "choices": [
                        "Consumed Cost Model",
                        "Constructive Cost Model",
                        "Common Control Model",
                        "Composition Cost Model",
                    ],
                    "answer": "Constructive Cost Model",
                },
                {
                    "question": "Which of the following is not defined in a good Software Requirement Specification(SRS) document?",
                    "choices": [
                        "Functional Requirement.",
                        "Nonfunctional Requirement.",
                        "Goals of implementation.",
                        "Algorithm for software implementation.",
                    ],
                    "answer": "Algorithm for software implementation.",
                },
                {
                    "question": "What is the simplest model of software development paradigm?",
                    "choices": [
                        "Spiral model",
                        "Big Bang model",
                        "V-model",
                        "Waterfall model",
                    ],
                    "answer": "Waterfall model",
                },
                {
                    "question": "Which design identifies the software as a system with many components interacting with each other?",
                    "choices": [
                        "High-level design",
                        "Architectural design",
                        "Detailed design",
                        "Efficiently design",
                    ],
                    "answer": "Architectural design",
                },
            ],
            [
                {
                    "question": "The extent to which one component depends on other components?",
                    "choices": [
                        "Cohesion",
                        "Concern",
                        "Coupling",
                        "Crossover",
                    ],
                    "answer": "Coupling",
                },
                {
                    "question": "Given classes A and B, which of the following is not a common type of coupling in object-oriented software?",
                    "choices": [
                        "A is a direct or an indirect subclass of B",
                        "A method parameter or local variable in A references B",
                        "A has an instance variable that refers to B",
                        "None of the above",
                    ],
                    "answer": "None of the above",
                },
                {
                    "question": "All else being equal, which is more desirable?",
                    "choices": [
                        "Higher/tighter coupling",
                        "Lower/looser coupling",
                        "None of the above is more desirable than the others",
                    ],
                    "answer": "Lower/looser coupling",
                },
                {
                    "question": "Which of the following is true about design patterns?",
                    "choices": [
                        "Represent the best practices used by experienced object-oriented software developers",
                        "Solutions to general problems that developers commonly face during software development",
                        "Obtained by trial and error of numerous software developers over a substantial period of time",
                        "All of the above",
                    ],
                    "answer": "All of the above",
                },
                {
                    "question": "Which pattern automatically notifies dependent objects when a subject object is modified?",
                    "choices": [
                        "Adapter",
                        "Observer",
                        "Mediator",
                        "Memento",
                    ],
                    "answer": "Observer",
                },
                {
                    "question": "Which pattern encapsulates how a set of objects interact?",
                    "choices": [
                        "Adapter",
                        "Observer",
                        "Mediator",
                        "Memento",
                    ],
                    "answer": "Mediator",
                },
                {
                    "question": "Which of the following are true about the Mediator Pattern?",
                    "choices": [
                        "Promotes loose coupling by keeping objects from referring to each other explicitly.",
                        "Allows you to vary the interaction between objects independently.",
                        "Uses indirection to keep objects from directly referring to each other.",
                        "All of the above.",
                    ],
                    "answer": "All of the above.",
                },
            ],
            [
                {
                    "question": "Process of inserting an element in stack is called ____________",
                    "choices": ["Create", "Push", "Evaluation", "Pop"],
                    "answer": "Push",
                },
                {
                    "question": "Process of removing an element from stack is called ____________",
                    "choices": ["Create", "Push", "Evaluation", "Pop"],
                    "answer": "Pop",
                },
                {
                    "question": "In a stack, if a user tries to remove an element from an empty stack it is called _________",
                    "choices": [
                        "Underflow",
                        "Empty collection",
                        "Overflow",
                        "Garbage Collection",
                    ],
                    "answer": "Underflow",
                },
                {
                    "question": "Pushing an element into stack already having five elements and stack size of 5, then stack becomes ___________",
                    "choices": [
                        "Underflow",
                        "Empty collection",
                        "Overflow",
                        "Garbage Collection",
                    ],
                    "answer": "Overflow",
                },
                {
                    "question": "RAD Software process model stands for _____",
                    "choices": [
                        "Rapid Application Development.",
                        "Relative Application Development.",
                        "Rapid Application Design.",
                        "Recent Application Development.",
                    ],
                    "answer": "Rapid Application Development.",
                },
                {
                    "question": "Entries in a stack are 'ordered'. What is the meaning of this statement?",
                    "choices": [
                        "A collection of stacks is sortable",
                        "Stack entries may be compared with the '<' operation",
                        "The entries are stored in a linked list",
                        "There is a Sequential entry that is one by one",
                    ],
                    "answer": "There is a Sequential entry that is one by one",
                },
                {
                    "question": "The data structure required to check whether an expression contains a balanced parenthesis is?.",
                    "choices": ["Stack", "Queue", "Array", "Tree"],
                    "answer": "Stack",
                },
                {
                    "question": "The postfix form of A*B+C/D is?",
                    "choices": ["*AB/CD+", "AB*CD/+", "A*BC+/D", "ABCD+/*"],
                    "answer": "AB*CD/+",
                },
                {
                    "question": "A linear list of elements in which deletion can be done from one end (front) and insertion can take place only at the other end (rear) is known as _____________",
                    "choices": ["Queue", "Stack", "Tree", "Linked list"],
                    "answer": "Queue",
                },
                {
                    "question": "Circular Queue is also known as ________",
                    "choices": ["Ring Buffer", "Square Buffer", "Rectangle Buffer", "Curve Buffer"],
                    "answer": "Ring Buffer",
                },
            ],
        ]

        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface with container and frames"""
        # ====== Container for pages ======
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Create Main Menu
        main = MainMenu(parent=container, controller=self)
        self.frames["MainMenu"] = main
        main.grid(row=0, column=0, sticky="nsew")

        # Create three quiz pages, each bound to its category index
        pages = [
            ("SoftwareQuiz", "Software Quiz", 0),
            ("LogicDesignQuiz", "Logic and Design Quiz", 1),
            ("AlgorithmQuiz", "Algorithm Quiz", 2),
        ]
        for key, title, idx in pages:
            frame = QuizPage(parent=container, controller=self, category_index=idx, title=title)
            self.frames[key] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name: str):
        """Show the specified frame/page"""
        frame = self.frames[page_name]
        frame.tkraise()


def create_app():
    """
    Factory function to create and return an App instance.
    This can be called from other modules to create the application.
    """
    return App()


# If this module is run directly, create and run the app
if __name__ == "__main__":
    app = create_app()
    app.mainloop()
