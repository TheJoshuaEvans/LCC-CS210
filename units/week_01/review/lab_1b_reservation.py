# =========================================================
# Program: Lab 1
# Author: Trevor Leadon
# Date: October 2025
# Version: 1.0
# IDE: VS Code / IDLE
# =========================================================

# Meeting Room Reservation System

attendees = int(input("Enter number of attendees: "))
projector_needed = input("Is a projector needed? (yes/no): ").strip().lower() == "yes"

if 1 <= attendees <= 5:
    print("Recommended Room: Room Alpha (No Projector)")
elif 6 <= attendees <= 15 and projector_needed:
    print("Recommended Room: Room Beta (Has Projector)")
elif 6 <= attendees <= 15 and not projector_needed:
    print("Recommended Room: Room Gamma (No Projector)")
elif attendees >= 16:
    print("Reservation Denied (No large rooms available)")
else:
    print("Invalid input. Please try again.")
