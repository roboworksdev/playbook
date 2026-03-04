"""Python Playbook — curriculum content for all 11 chapters."""

import os

_DIR     = os.path.dirname(os.path.abspath(__file__))
ROBOSIM  = os.path.join(_DIR, "RoboSim")   # path to RoboSim project folder


def script_path(filename: str) -> str:
    return os.path.join(ROBOSIM, filename)

def world_path(filename: str) -> str:
    return os.path.join(_DIR, "Chapters", filename)


CHAPTERS = [
    # ── Chapter 0 ─────────────────────────────────────────────────────────────
    {
        "number":     0,
        "title":      "Introduction",
        "subtitle":   "Welcome to Python Playbook.",
        "status":     "available",
        "world_file": "chapter0_coffeeshop.py",
        "concepts":   [],
        "story": (
            "Robby the Robot works in a coffee shop. You need to write Python "
            "commands to help Robby navigate the coffee shop and deliver coffee "
            "to customers.\n\n"
            "Before Robby can take any orders, you need to get familiar with "
            "the environment he works in — the layout of the shop, the tools "
            "you have to control him, and the sensors that help him understand "
            "the world around him."
        ),
        "missions": [
            {
                "id":          "Mission 1",
                "title":       "Drive to the Green Ball",
                "description": (
                    "Move towards the green ball by pressing the A W D S keys "
                    "on your keyboard."
                ),
                "trigger":     {"type": "enter", "zone": "GreenZone"},
                "script":      "",
            },
            {
                "id":          "Mission 2",
                "title":       "Catch the Green Ball",
                "description": (
                    "Click the Attach button to catch the green ball."
                ),
                "trigger":     {"type": "attach", "zone": "GreenZone", "object": "GreenBall"},
                "script":      "",
            },
            {
                "id":          "Mission 3",
                "title":       "Deliver to the Yellow Block",
                "description": (
                    "Move with the green ball towards the yellow block."
                ),
                "trigger":     {"type": "enter_with", "zone": "YellowZone", "object": "GreenBall"},
                "script":      "",
            },
            {
                "id":          "Mission 4",
                "title":       "Drop the Green Ball",
                "description": (
                    "Drop the green ball by clicking the Detach button."
                ),
                "trigger":     {"type": "detach", "zone": "YellowZone", "object": "GreenBall"},
                "script":      "",
            },
            {
                "id":          "Mission 5",
                "title":       "Catch the Yellow Block",
                "description": (
                    "Catch the yellow block by clicking the Attach button."
                ),
                "trigger":     {"type": "attach", "zone": "YellowZone", "object": "YellowBlock"},
                "script":      "",
            },
            {
                "id":          "Mission 6",
                "title":       "Place at the Red Column",
                "description": (
                    "Move the yellow block next to the red column and drop it."
                ),
                "trigger":     {"type": "detach", "zone": "RedZone", "object": "YellowBlock"},
                "script":      "",
            },
        ],
        "learning_outcomes": (
            "1. Student should understand how to load a new world.\n"
            "2. Student should understand how to open the editor and code the "
            "simulated robot using the Code Editor.\n"
            "3. Student should understand the functions of the 3 side windows "
            "on the right.\n"
            "4. Student should grasp basic concepts of robot sensors such as "
            "camera and laser sensor."
        ),
        "educator_notes":  "Enter your teacher notes here.",
    },

    # ── Chapter 1 ─────────────────────────────────────────────────────────────
    {
        "number":     1,
        "title":      "Python Basics",
        "subtitle":   "Variables, input and output.",
        "status":     "available",
        "world_file": "chapter1_coffeeshop.py",
        "concepts":   ["variables", "input()", "print()", "data types", "assignment"],
        "story": (
            "Robby the Robot is on duty at the coffee shop. A customer has placed "
            "an order, and it's up to you to help Robby deliver it.\n\n"
            "First, guide Robby to the counter to pick up the freshly brewed coffee. "
            "Then carry it carefully across the shop to the customer's table and set "
            "it down. Once the customer is happy, collect the dirty plate they left "
            "behind and bring it back to the kitchen hatch.\n\n"
            "In this chapter you will also write your first lines of Python — "
            "using variables to store information and print() to display it."
        ),
        "missions": [
            {
                "id":          "Mission 1",
                "title":       "print() — Robby Says Hello",
                "description": (
                    "Python Concept: print()\n\n"
                    "print() displays text on the screen. Anything inside the "
                    "brackets and quotes is shown as output.\n\n"
                    "Step 1 — Open the Code Editor (click the Code Editor button).\n"
                    "Step 2 — The starter code is already loaded. Read it, then "
                    "click Run to execute it.\n"
                    "Step 3 — Try changing the message inside the quotes to "
                    "something different and Run again.\n"
                    "Step 4 — Drive Robby to the green circle (the coffee counter) "
                    "using the A W D S keys to complete the mission."
                ),
                "trigger":     {"type": "enter", "zone": "PickupZone"},
                "script": (
                    "# Mission 1: print() — Show a message on the screen\n"
                    "#\n"
                    "# print() is a built-in Python function.\n"
                    "# Whatever you put inside the brackets is displayed as output.\n"
                    "\n"
                    "print(\"Hello! I am Robby the Robot.\")\n"
                    "print(\"I am ready to deliver coffee!\")\n"
                    "\n"
                    "# Try changing the text above, then click Run again.\n"
                    "# When you are done, drive to the green circle using A W D S."
                ),
            },
            {
                "id":          "Mission 2",
                "title":       "Variables — Store the Order",
                "description": (
                    "Python Concept: Variables\n\n"
                    "A variable is a named container that stores a value. "
                    "You create one using the = sign (called the assignment operator).\n\n"
                    "    order = \"Coffee\"\n\n"
                    "Here, order is the variable name and \"Coffee\" is the value "
                    "stored inside it. You can then use the variable name anywhere "
                    "you would use the value.\n\n"
                    "Step 1 — Read the starter code in the Editor.\n"
                    "Step 2 — Click Run to see the output.\n"
                    "Step 3 — Change the variable value to a different drink name "
                    "and Run again to see how the output changes.\n"
                    "Step 4 — Click Attach to pick up the coffee cup."
                ),
                "trigger":     {"type": "attach", "zone": "PickupZone", "object": "CoffeeCup"},
                "script": (
                    "# Mission 2: Variables — Store a value with a name\n"
                    "#\n"
                    "# A variable stores a value so you can use it later.\n"
                    "# Syntax:  variable_name = value\n"
                    "\n"
                    "order = \"Coffee\"           # str (text) variable\n"
                    "table = 1                   # int (whole number) variable\n"
                    "\n"
                    "print(\"Order:\", order)\n"
                    "print(\"Deliver to table:\", table)\n"
                    "\n"
                    "# Try changing the values above and Run again.\n"
                    "# Then click Attach to pick up the coffee cup."
                ),
            },
            {
                "id":          "Mission 3",
                "title":       "f-strings — Format the Delivery Message",
                "description": (
                    "Python Concept: f-strings\n\n"
                    "An f-string lets you insert variable values directly inside "
                    "a string. Put f before the opening quote, then wrap the "
                    "variable name in curly braces { }.\n\n"
                    "    name = \"Alice\"\n"
                    "    print(f\"Hello, {name}!\")\n"
                    "    # Output: Hello, Alice!\n\n"
                    "Step 1 — Read and run the starter code.\n"
                    "Step 2 — Change customer and table to different values and "
                    "Run again.\n"
                    "Step 3 — Carry the coffee to the orange circle (customer's "
                    "table) using A W D S to complete the mission."
                ),
                "trigger":     {"type": "enter_with", "zone": "Table1Zone", "object": "CoffeeCup"},
                "script": (
                    "# Mission 3: f-strings — Embed variables inside text\n"
                    "#\n"
                    "# An f-string starts with f before the quote.\n"
                    "# Variables go inside curly braces { }.\n"
                    "\n"
                    "order    = \"Coffee\"\n"
                    "table    = 1\n"
                    "customer = \"Alice\"\n"
                    "\n"
                    "print(f\"Delivering {order} to table {table} for {customer}.\")\n"
                    "\n"
                    "# Try changing the variables, then Run again.\n"
                    "# Drive to the orange circle to complete the mission."
                ),
            },
            {
                "id":          "Mission 4",
                "title":       "Updating Variables — Count Deliveries",
                "description": (
                    "Python Concept: Updating variables\n\n"
                    "A variable's value can be changed at any time by assigning "
                    "a new value to it.\n\n"
                    "    deliveries = 0\n"
                    "    deliveries = deliveries + 1   # now equals 1\n\n"
                    "You can also write this with a shortcut:\n\n"
                    "    deliveries += 1\n\n"
                    "Step 1 — Run the starter code and read the output.\n"
                    "Step 2 — Change the starting value of deliveries and Run "
                    "again to see how the final output changes.\n"
                    "Step 3 — Click Detach to set the coffee down for the customer."
                ),
                "trigger":     {"type": "detach", "zone": "Table1Zone", "object": "CoffeeCup"},
                "script": (
                    "# Mission 4: Updating variables\n"
                    "#\n"
                    "# Variables can be reassigned — their value can change.\n"
                    "\n"
                    "deliveries = 0              # starting value\n"
                    "print(f\"Deliveries so far: {deliveries}\")\n"
                    "\n"
                    "deliveries = deliveries + 1 # add 1\n"
                    "print(f\"After this delivery: {deliveries}\")\n"
                    "\n"
                    "# Shortcut: deliveries += 1 does the same thing.\n"
                    "# Try it! Then click Detach to set down the coffee."
                ),
            },
            {
                "id":          "Mission 5",
                "title":       "input() — Ask the Customer's Name",
                "description": (
                    "Python Concept: input()\n\n"
                    "input() pauses the program and waits for the user to type "
                    "something. The typed text is returned as a string and can be "
                    "stored in a variable.\n\n"
                    "    name = input(\"What is your name? \")\n"
                    "    print(f\"Hello, {name}!\")\n\n"
                    "Note: input() works in a terminal or Python shell. In the "
                    "robot editor the starter code uses a preset value so the "
                    "simulation does not freeze — but the concept is the same.\n\n"
                    "Step 1 — Run the starter code and read the output.\n"
                    "Step 2 — Change the value of customer_name and Run again.\n"
                    "Step 3 — Click Attach to pick up the dirty plate."
                ),
                "trigger":     {"type": "attach", "zone": "Table1Zone", "object": "DirtyPlate"},
                "script": (
                    "# Mission 5: input() — Read a value from the user\n"
                    "#\n"
                    "# In a real program you would write:\n"
                    "#   customer_name = input(\"Enter customer name: \")\n"
                    "#\n"
                    "# In the robot editor we assign a preset value instead,\n"
                    "# because input() would pause the simulation.\n"
                    "\n"
                    "customer_name = \"Alex\"      # try changing this name\n"
                    "\n"
                    "print(f\"Thank you, {customer_name}!\")\n"
                    "print(f\"Collecting your plate now.\")\n"
                    "\n"
                    "# Then click Attach to pick up the dirty plate."
                ),
            },
            {
                "id":          "Mission 6",
                "title":       "Putting It Together — Return to Kitchen",
                "description": (
                    "Python Review: variables, print(), f-strings, input()\n\n"
                    "In this final mission you will write your own code from "
                    "scratch to combine everything you have learned.\n\n"
                    "Step 1 — Fill in the blanks in the starter code.\n"
                    "Step 2 — Run your code and check the output makes sense.\n"
                    "Step 3 — Carry the dirty plate to the blue circle "
                    "(kitchen hatch) using A W D S to complete the chapter."
                ),
                "trigger":     {"type": "enter_with", "zone": "KitchenZone", "object": "DirtyPlate"},
                "script": (
                    "# Mission 6: Write your own code!\n"
                    "#\n"
                    "# Fill in the blanks (___) to complete the program.\n"
                    "\n"
                    "robot_name   = ___           # your robot's name (a string)\n"
                    "item         = ___           # what you are carrying\n"
                    "destination  = \"Kitchen\"    # where you are going\n"
                    "\n"
                    "print(f\"{robot_name} is returning the {item} to the {destination}.\")\n"
                    "print(\"Mission complete! Great work today.\")\n"
                    "\n"
                    "# Once the output looks right, drive to the blue circle."
                ),
            },
        ],
        "learning_outcomes": (
            "1. Student understands what a variable is and how to assign one.\n"
            "2. Student can use print() to display text and variable values.\n"
            "3. Student can use f-strings to embed variables inside text.\n"
            "4. Student understands how to update a variable's value.\n"
            "5. Student understands how input() reads user input at runtime.\n"
            "6. Student recognises the basic data types: str, int, float."
        ),
        "educator_notes":  "Enter your teacher notes here.",
    },

    # ── Chapter 2 ─────────────────────────────────────────────────────────────
    {
        "number":     2,
        "title":      "Formatted Print",
        "subtitle":   "Presenting output clearly and professionally.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["f-strings", "format()", "str()", "escape characters", "print()"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your teacher notes here.",
    },

    # ── Chapter 3 ─────────────────────────────────────────────────────────────
    {
        "number":     3,
        "title":      "Conditional Statements",
        "subtitle":   "Teaching your program to make decisions.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["if", "elif", "else", "Boolean expressions", "comparison operators"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your teacher notes here.",
    },

    # ── Chapter 4 ─────────────────────────────────────────────────────────────
    {
        "number":     4,
        "title":      "Loops",
        "subtitle":   "Repeating actions efficiently.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["for loop", "while loop", "range()", "break", "continue"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your teacher notes here.",
    },

    # ── Chapter 5 ─────────────────────────────────────────────────────────────
    {
        "number":     5,
        "title":      "Data Structures",
        "subtitle":   "Lists and Dictionaries.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["list", "dictionary", "indexing", "keys", "values", "append()", "len()"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your teacher notes here.",
    },

    # ── Chapter 6 ─────────────────────────────────────────────────────────────
    {
        "number":     6,
        "title":      "Functions",
        "subtitle":   "Writing reusable blocks of code.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["def", "parameters", "return", "scope", "docstrings"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your teacher notes here.",
    },

    # ── Chapter 7 ─────────────────────────────────────────────────────────────
    {
        "number":     7,
        "title":      "List Processing",
        "subtitle":   "Working with collections of data.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["list comprehension", "map()", "filter()", "sorted()", "enumerate()", "zip()"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your teacher notes here.",
    },

    # ── Chapter 8 ─────────────────────────────────────────────────────────────
    {
        "number":     8,
        "title":      "Algorithms",
        "subtitle":   "Searching, Sorting, Counting and Math algorithms.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["linear search", "binary search", "bubble sort", "counting", "math algorithms"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your teacher notes here.",
    },

    # ── Chapter 9 ─────────────────────────────────────────────────────────────
    {
        "number":     9,
        "title":      "Recursion",
        "subtitle":   "Functions that call themselves.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["recursive functions", "base case", "call stack", "factorial", "Fibonacci"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your teacher notes here.",
    },

    # ── Chapter 10 ────────────────────────────────────────────────────────────
    {
        "number":     10,
        "title":      "Evaluation",
        "subtitle":   "Robotics Project: Pick & Place Sorting.",
        "status":     "available",
        "world_file": "chapter3_warehouse.py",
        "concepts":   ["full integration", "autonomous planning", "sorting", "Pick & Place"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your teacher notes here.",
    },
]
