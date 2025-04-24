import tkinter as tk
from tkinter import ttk
import sqlite3

class DashboardApp:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f0f0f0")

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#ffffff")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create sidebar
        self.create_sidebar()

        # Create content area
        self.create_content_area()

        # Set default view to dashboard
        self.show_dashboard()

    def create_sidebar(self):
        # Sidebar frame
        sidebar_frame = tk.Frame(self.main_frame, width=200, bg="#2c3e50")
        sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
        sidebar_frame.pack_propagate(False)

        # Sidebar title
        title_label = tk.Label(sidebar_frame, text="Dashboard", 
                               font=("Arial", 16, "bold"), 
                               bg="#2c3e50", 
                               fg="white")
        title_label.pack(pady=(20, 30))

        # Sidebar buttons
        sidebar_buttons = [
            ("Dashboard", self.show_dashboard),
            ("Profile", self.show_profile),
            ("Settings", self.show_settings),
            ("Analytics", self.show_analytics),
            ("Logout", self.logout)
        ]

        for text, command in sidebar_buttons:
            btn = tk.Button(
                sidebar_frame, 
                text=text, 
                command=command,
                bg="#34495e", 
                fg="white", 
                font=("Arial", 12),
                bd=0,
                activebackground="#2c3e50",
                activeforeground="white",
                width=20,
                anchor="w",
                padx=10
            )
            btn.pack(pady=5)

    def create_content_area(self):
        # Content frame
        self.content_frame = tk.Frame(self.main_frame, bg="white")
        self.content_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

    def clear_content(self):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_content()
        
        # Dashboard title
        title = tk.Label(self.content_frame, 
                         text="Dashboard Overview", 
                         font=("Arial", 20, "bold"), 
                         bg="white")
        title.pack(pady=20)

        # Dashboard cards
        dashboard_cards = [
            ("Total Users", "50"),
            ("Active Sessions", "23"),
            ("Revenue", "$5,420"),
            ("Pending Tasks", "7")
        ]

        # Create a frame to hold cards
        cards_frame = tk.Frame(self.content_frame, bg="white")
        cards_frame.pack(expand=True, fill=tk.BOTH, padx=20)

        # Configure grid for cards
        cards_frame.grid_columnconfigure(0, weight=1)
        cards_frame.grid_columnconfigure(1, weight=1)

        # Create and place cards
        for i, (title, value) in enumerate(dashboard_cards):
            card_frame = tk.Frame(cards_frame, 
                                  bg="#ecf0f1", 
                                  borderwidth=1, 
                                  relief=tk.RAISED)
            card_frame.grid(row=i//2, column=i%2, 
                            padx=10, pady=10, 
                            sticky="nsew")

            title_label = tk.Label(card_frame, 
                                   text=title, 
                                   font=("Arial", 12), 
                                   bg="#ecf0f1")
            title_label.pack(pady=(10,5))

            value_label = tk.Label(card_frame, 
                                   text=value, 
                                   font=("Arial", 16, "bold"), 
                                   bg="#ecf0f1")
            value_label.pack(pady=(0,10))

    def show_profile(self):
        self.clear_content()
        
        title = tk.Label(self.content_frame, 
                         text="User Profile", 
                         font=("Arial", 20, "bold"), 
                         bg="white")
        title.pack(pady=20)

        # Profile details
        profile_details = [
            ("Name", "John Doe"),
            ("Email", "johndoe@example.com"),
            ("Role", "Administrator"),
            ("Join Date", "January 15, 2024")
        ]

        for label, value in profile_details:
            frame = tk.Frame(self.content_frame, bg="white")
            frame.pack(fill=tk.X, padx=50, pady=5)

            label_widget = tk.Label(frame, 
                                    text=label, 
                                    font=("Arial", 12, "bold"), 
                                    bg="white", 
                                    width=15, 
                                    anchor="w")
            label_widget.pack(side=tk.LEFT)

            value_widget = tk.Label(frame, 
                                    text=value, 
                                    font=("Arial", 12), 
                                    bg="white")
            value_widget.pack(side=tk.LEFT)

    def show_settings(self):
        self.clear_content()
        
        title = tk.Label(self.content_frame, 
                         text="Application Settings", 
                         font=("Arial", 20, "bold"), 
                         bg="white")
        title.pack(pady=20)

        # Settings options
        settings_options = [
            "Notification Preferences",
            "Privacy Settings",
            "Account Security",
            "Theme Selection"
        ]

        for option in settings_options:
            btn = tk.Button(self.content_frame, 
                            text=option, 
                            font=("Arial", 12), 
                            bg="#3498db", 
                            fg="white", 
                            width=30)
            btn.pack(pady=10)

    def show_analytics(self):
        self.clear_content()
        
        title = tk.Label(self.content_frame, 
                         text="Analytics", 
                         font=("Arial", 20, "bold"), 
                         bg="white")
        title.pack(pady=20)

        # Placeholder for analytics content
        analytics_text = tk.Label(self.content_frame, 
                                  text="Analytics data will be displayed here", 
                                  font=("Arial", 12), 
                                  bg="white")
        analytics_text.pack(expand=True)

    def logout(self):
        # Close current window and potentially show login window
        self.root.destroy()

def main():
    root = tk.Tk()
    app = DashboardApp(root, "John Doe")  # Fixed: changed from keyword argument to positional argument
    root.mainloop()

if __name__ == "__main__":
    main()