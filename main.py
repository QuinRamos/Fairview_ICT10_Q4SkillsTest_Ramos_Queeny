from pyscript import document, display
import numpy as np
import matplotlib.pyplot as plt
import logging

# Suppress matplotlib font logs
logging.getLogger('matplotlib').setLevel(logging.ERROR)

data = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0
}

def update_and_plot(e):
    # Reveal the graph container
    document.getElementById('graph-container').style.display = "block"
    
    # Capture data from the form
    selected_day = document.getElementById("section").value
    count_val = document.getElementById("math").value
    
    if count_val:
        # No more max limit, just direct integer conversion
        data[selected_day] = int(count_val)

    # Clear the old graph
    document.getElementById('output').innerHTML = ""

    # Prepare data
    days = list(data.keys())
    absences = list(data.values())
    
    # Create the plot (Smaller size for the centered layout)
    plt.figure(figsize=(7, 4.5)) 
    plt.plot(days, absences, marker='o', linestyle='-', color="#e289b5", linewidth=2) 
    
    # Styling
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Automatically fits the content perfectly
    plt.tight_layout()

    # Display to the HTML target
    display(plt, target="output")