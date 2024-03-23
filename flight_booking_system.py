import tkinter as tk
from tkinter import messagebox

class FlightBookingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Flight Booking System")
        

        # Initialize variables
        self.passenger_name_var = tk.StringVar()
        self.passenger_age_var = tk.StringVar()
        self.num_seats_var = tk.StringVar()
        self.selected_flight_var = tk.StringVar()

        # Create labels
        tk.Label(master, text="Passenger Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(master, text="Passenger Age:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(master, text="Number of Seats:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(master, text="Select Flight:").grid(row=3, column=0, padx=10, pady=10, sticky="e")

        # Create entry widgets
        tk.Entry(master, textvariable=self.passenger_name_var).grid(row=0, column=1, padx=10, pady=10)
        tk.Entry(master, textvariable=self.passenger_age_var).grid(row=1, column=1, padx=10, pady=10)
        tk.Entry(master, textvariable=self.num_seats_var).grid(row=2, column=1, padx=10, pady=10)

        # Create a dropdown menu for flight selection
        flights = ["Flight1 Mumbai to Delhi", "Flight2 Pune to Banglore", "Flight3 Noida to Delhi"]
        self.flight_dropdown = tk.OptionMenu(master, self.selected_flight_var, *flights)
        self.flight_dropdown.grid(row=3, column=1, padx=10, pady=10)

        # Create buttons
        tk.Button(master, text="Display Available Seats", command=self.display_available_seats).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(master, text="Book Flight", command=self.book_flight).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(master, text="Cancel Booking", command=self.cancel_booking).grid(row=6, column=0, columnspan=2, pady=10)

        # Display information
        self.info_text = tk.Text(master, height=10, width=50)
        self.info_text.grid(row=7, column=0, columnspan=2, pady=10)

        # Initialize available seats
        self.available_seats = {"Flight1 Mumbai to Delhi": 100, "Flight2 Pune to Banglore": 89, "Flight3 Noida to Delhi": 110}

    def display_available_seats(self):
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, "Available Seats:\n")
        for flight, seats in self.available_seats.items():
            self.info_text.insert(tk.END, f"{flight}: {seats} seats\n")

    def book_flight(self):
        passenger_name = self.passenger_name_var.get()
        passenger_age = self.passenger_age_var.get()
        num_seats = self.num_seats_var.get()
        selected_flight = self.selected_flight_var.get()

        if not passenger_name or not passenger_age or not num_seats:
            messagebox.showwarning("Incomplete Information", "Please enter Passenger Name, Age, and Number of Seats.")
            return

        try:
            num_seats = int(num_seats)
        except ValueError:
            messagebox.showwarning("Invalid Number of Seats", "Please enter a valid number for the seats.")
            return

        if selected_flight not in self.available_seats:
            messagebox.showwarning("Invalid Flight", "Please select a valid flight.")
            return

        if self.available_seats[selected_flight] < num_seats:
            messagebox.showwarning("Insufficient Seats", "Sorry, there are not enough available seats for this booking.")
            return

        self.available_seats[selected_flight] -= num_seats
        self.display_available_seats()
        messagebox.showinfo("Booking Successful", f"Booking for {num_seats} seat(s) for {passenger_name} on {selected_flight} successful!")

    def cancel_booking(self):
        passenger_name = self.passenger_name_var.get()
        passenger_age = self.passenger_age_var.get()
        num_seats = self.num_seats_var.get()
        selected_flight = self.selected_flight_var.get()

        if not passenger_name or not passenger_age or not num_seats:
            messagebox.showwarning("Incomplete Information", "Please enter Passenger Name, Age, and Number of Seats.")
            return

        try:
            num_seats = int(num_seats)
        except ValueError:
            messagebox.showwarning("Invalid Number of Seats", "Please enter a valid number for the seats.")
            return

        if selected_flight not in self.available_seats:
            messagebox.showwarning("Invalid Flight", "Please select a valid flight.")
            return

        self.available_seats[selected_flight] += num_seats
        self.display_available_seats()
        messagebox.showinfo("Booking Canceled", f"Booking for {num_seats} seat(s) for {passenger_name} on {selected_flight} canceled.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightBookingSystem(root)
    root.mainloop()
