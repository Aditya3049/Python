from guizero import App, Text, PushButton

# Functions -------------

# App -------------------
app = App("TOP SECRET")

# Widgets ---------------
title = Text(app, "Push the red button to find out your spy name")
button = PushButton(app, choose_name, text="Tell me!")

# Display ---------------
app.display()
def choose_name():
 print("Button was pressed")# Imports ---------------


