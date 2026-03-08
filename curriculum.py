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
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 1 ─────────────────────────────────────────────────────────────
    {
        "number":     1,
        "title":      "Conditional Statements",
        "subtitle":   "Teaching your program to make decisions.",
        "status":     "available",
        "world_file": "chapter1_kitchen_wall.py",
        "concepts":   ["if", "elif", "else", "Boolean expressions", "comparison operators"],
        "story": (
            "Robby the Robot is trying to enter the cafe kitchen. His starting "
            "position is at one side of the room, and the kitchen is on the other "
            "side — separated by a long white wall with a door at each end.\n\n"
            "Robby will travel straight towards the wall. You need to program Robby "
            "to stop in front of the wall instead of hitting it. Then turn and travel "
            "along the wall towards one of the doors at the edge.\n\n"
            "In this chapter you will use conditional statements — if, elif, and else "
            "— to give Robby the ability to sense his surroundings and make decisions "
            "about what to do next."
        ),
        "missions": [
            {
                "id":          "Mission 1",
                "title":       "if — Stop Before the Wall",
                "description": (
                    "Python Concept: if statement\n\n"
                    "An if statement runs a block of code only when a condition is "
                    "True. Use distance(0) to read how far ahead the nearest obstacle "
                    "is (0 = straight ahead).\n\n"
                    "    if distance(0) > 1.0:\n"
                    "        drive(1, 0)   # move forward\n"
                    "    else:\n"
                    "        drive(0, 0)   # stop\n\n"
                    "Step 1 — Open the Code Editor and read the starter code.\n"
                    "Step 2 — Enable 'Run forever' so the code loops continuously.\n"
                    "Step 3 — Click Run and watch Robby approach the wall.\n"
                    "Step 4 — Adjust the threshold value until Robby stops safely "
                    "inside the yellow zone in front of the wall."
                ),
                "trigger": {"type": "enter", "zone": "WallApproachZone"},
                "script": (
                    "# Mission 1: if — Stop before the wall\n"
                    "#\n"
                    "# distance(0) returns how far ahead the nearest obstacle is.\n"
                    "# Use an if/else to drive forward or stop.\n"
                    "#\n"
                    "# Enable 'Run forever' before clicking Run.\n"
                    "\n"
                    "if distance(0) > 1.0:\n"
                    "    drive(1, 0)    # drive forward — path is clear\n"
                    "else:\n"
                    "    drive(0, 0)   # stop — wall is too close!\n"
                    "\n"
                    "# Try changing 1.0 to a different number.\n"
                    "# Goal: stop Robby inside the yellow circle."
                ),
            },
            {
                "id":          "Mission 2",
                "title":       "elif — Turn and Find the Left Door",
                "description": (
                    "Python Concept: if / elif / else\n\n"
                    "elif (short for 'else if') lets you check a second condition "
                    "when the first one is False. You can chain as many elif blocks "
                    "as you need.\n\n"
                    "    if distance(0) > 1.0:\n"
                    "        drive(1, 0)       # clear ahead — go forward\n"
                    "    elif distance(270) > 1.5:\n"
                    "        drive(0.3, -0.4)  # wall close — turn left\n"
                    "    else:\n"
                    "        drive(1, 0)       # in doorway — drive through\n\n"
                    "Note: distance(270) reads to the left of the robot.\n\n"
                    "Step 1 — Read and run the starter code with 'Run forever' on.\n"
                    "Step 2 — Adjust the turn direction and speed until Robby "
                    "navigates around the left end of the wall.\n"
                    "Step 3 — Guide Robby into the blue circle (left door) to "
                    "complete the mission."
                ),
                "trigger": {"type": "enter", "zone": "LeftDoorZone"},
                "script": (
                    "# Mission 2: elif — Turn and reach the left door\n"
                    "#\n"
                    "# distance(270) = distance to the LEFT of Robby.\n"
                    "# Add an elif to turn when the wall blocks the path ahead.\n"
                    "#\n"
                    "# Enable 'Run forever' before clicking Run.\n"
                    "\n"
                    "if distance(0) > 1.0:\n"
                    "    drive(1, 0)        # clear ahead — go forward\n"
                    "elif distance(270) > 1.5:\n"
                    "    drive(0.3, -0.4)   # wall ahead — turn left\n"
                    "else:\n"
                    "    drive(1, 0)        # in doorway — drive through\n"
                    "\n"
                    "# Goal: guide Robby into the blue circle (left door)."
                ),
            },
            {
                "id":          "Mission 3",
                "title":       "Boolean Expressions — Choose Your Door",
                "description": (
                    "Python Concept: Boolean expressions\n\n"
                    "A Boolean expression compares two values and produces True or "
                    "False. You can combine conditions using and, or, and not.\n\n"
                    "    if distance(0) > 1.0 and distance(90) > 1.0:\n"
                    "        drive(1, 0.4)   # clear ahead AND to the right\n\n"
                    "In this mission, start from the left door and navigate to the "
                    "right door using combined conditions.\n\n"
                    "Step 1 — Run the starter code with 'Run forever' on.\n"
                    "Step 2 — Modify the conditions to navigate along the wall "
                    "from the left side to the right side.\n"
                    "Step 3 — Reach the green circle (right door) to complete "
                    "the chapter."
                ),
                "trigger": {"type": "enter", "zone": "RightDoorZone"},
                "script": (
                    "# Mission 3: Boolean expressions — Navigate to the right door\n"
                    "#\n"
                    "# Use 'and' / 'or' to combine conditions.\n"
                    "# distance(90) = distance to the RIGHT of Robby.\n"
                    "#\n"
                    "# Enable 'Run forever' before clicking Run.\n"
                    "\n"
                    "if distance(0) > 1.0 and distance(90) > 1.5:\n"
                    "    drive(1, 0.4)    # clear ahead and right — curve right\n"
                    "elif distance(0) > 1.0:\n"
                    "    drive(1, 0)      # clear ahead — go straight\n"
                    "else:\n"
                    "    drive(0, 0.5)    # blocked ahead — turn right\n"
                    "\n"
                    "# Goal: guide Robby into the green circle (right door)."
                ),
            },
        ],
        "learning_outcomes": (
            "1. Student can write an if/else statement to make a decision based on "
            "sensor data — e.g., stopping Robby before he hits the wall using "
            "distance().\n"
            "2. Student understands if/elif/else chains and can use them to handle "
            "multiple conditions — e.g., deciding whether to drive forward, turn, "
            "or stop depending on what Robby's sensors detect.\n"
            "3. Student can construct Boolean expressions using comparison operators "
            "(<, >, ==) and logical operators (and, or, not) to describe real-world "
            "conditions in code."
        ),
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 2 ─────────────────────────────────────────────────────────────
    {
        "number":     2,
        "title":      "Variables",
        "subtitle":   "Presenting output clearly and professionally.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["f-strings", "format()", "str()", "escape characters", "print()"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 3 ─────────────────────────────────────────────────────────────
    {
        "number":     3,
        "title":      "Loops",
        "subtitle":   "Teaching your program to make decisions.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["if", "elif", "else", "Boolean expressions", "comparison operators"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 4 ─────────────────────────────────────────────────────────────
    {
        "number":     4,
        "title":      "Functions",
        "subtitle":   "Repeating actions efficiently.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["for loop", "while loop", "range()", "break", "continue"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 5 ─────────────────────────────────────────────────────────────
    {
        "number":     5,
        "title":      "List Processing",
        "subtitle":   "Lists and Dictionaries.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["list", "dictionary", "indexing", "keys", "values", "append()", "len()"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 6 ─────────────────────────────────────────────────────────────
    {
        "number":     6,
        "title":      "Algorithms",
        "subtitle":   "Writing reusable blocks of code.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["def", "parameters", "return", "scope", "docstrings"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 7 ─────────────────────────────────────────────────────────────
    {
        "number":     7,
        "title":      "Recursion",
        "subtitle":   "Working with collections of data.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["list comprehension", "map()", "filter()", "sorted()", "enumerate()", "zip()"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 8 ─────────────────────────────────────────────────────────────
    {
        "number":     8,
        "title":      "Evaluation",
        "subtitle":   "Searching, Sorting, Counting and Math algorithms.",
        "status":     "available",
        "world_file": "",
        "concepts":   ["linear search", "binary search", "bubble sort", "counting", "math algorithms"],
        "story":      "Content coming soon.",
        "missions":   [],
        "learning_outcomes": "",
        "educator_notes":  "Enter your notes here.",
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
        "educator_notes":  "Enter your notes here.",
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
        "educator_notes":  "Enter your notes here.",
    },
]
