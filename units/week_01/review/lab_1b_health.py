# =========================================================
# Program: Lab 1
# Author: Trevor Leadon
# Date: October 2025
# Version: 1.0
# IDE: VS Code / IDLE
# =========================================================

# Server Status and Priority Alert

health_code = int(input("Enter Health Code (1=Critical, 2=Warning, 3=Optimal): "))
hours_since_check = float(input("Enter time since last check (in hours): "))

if health_code == 1:
    priority = "HIGH"
elif health_code == 2:
    if hours_since_check > 4:
        priority = "HIGH"
    else:
        priority = "MEDIUM"
elif health_code == 3:
    if hours_since_check > 10:
        priority = "LOW"
    else:
        priority = "CLEAR"
else:
    priority = "INVALID"

print(f"Alert Priority: {priority}")
