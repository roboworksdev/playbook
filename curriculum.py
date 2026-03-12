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
        "subtitle":   "Storing and updating values in your program.",
        "status":     "available",
        "world_file": "chapter2_coffeeshop.py",
        "concepts":   ["variable", "=", "+=", "-=", "f-string", "print()"],
        "story": (
            "Robby is on shift at the coffee shop. Three cups of coffee are "
            "waiting on the counter for customers at Table A and Table B. "
            "Robby has no way of remembering how many cups she is carrying "
            "— unless she uses a variable.\n\n"
            "A variable is a named container in the program's memory. You "
            "give it a name, store a value inside it, and the rest of the "
            "program can read or change it at any time.\n\n"
            "In this chapter you will use variables to track Robby's cup "
            "count — picking up from the counter and counting down with "
            "every delivery."
        ),
        "missions": [
            {
                "id":          "Mission 1",
                "title":       "Variables — Count the Cups",
                "description": (
                    "Python Concept: variable assignment with = and print() "
                    "with an f-string\n\n"
                    "A variable stores a value under a name. Use = to assign "
                    "it. The f-string lets you embed a variable inside printed "
                    "text using {variable_name}.\n\n"
                    "    cups = 3\n"
                    "    print(f\"Cups: {cups}\")\n\n"
                    "Step 1 — Read the starter code and note where cups is "
                    "assigned.\n"
                    "Step 2 — Click Run and watch Robby drive to the counter "
                    "(cyan circle).\n"
                    "Step 3 — Change cups = 3 to cups = 2 or cups = 5 and "
                    "run again — watch the printed output change."
                ),
                "trigger": {"type": "enter", "zone": "CyanZone"},
                "script": (
                    "# Mission 1: Variables — Count the cups\n"
                    "#\n"
                    "# A variable stores a value under a name. Use = to assign it.\n"
                    "# The f-string lets you insert a variable into printed text: f\"text {variable}\"\n"
                    "#\n"
                    "# Try changing cups = 3 to a different number. What changes in the output?\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "cups = 3          # store the order count in a variable\n"
                    "print(f\"Starting shift. Orders today: {cups} cups\")\n"
                    "\n"
                    "# Drive north to the counter (cyan circle) to begin the delivery\n"
                    "drive(0.4, 0)\n"
                    "time.sleep(2.2)   # adjust until Robby reaches the cyan circle\n"
                    "drive(0, 0)\n"
                    "\n"
                    "print(f\"At the counter. Ready to serve {cups} tables.\")\n"
                    "\n"
                    "# Goal: reach the cyan circle at the counter."
                ),
            },
            {
                "id":          "Mission 2",
                "title":       "Updating Variables — Deliver to Table A",
                "description": (
                    "Python Concept: += and -= operators\n\n"
                    "cups -= 1 subtracts 1 from the variable each time a cup "
                    "is delivered. cups = 3 then cups -= 1 gives cups == 2.\n\n"
                    "Step 1 — Run the starter code. Robby drives to the "
                    "counter then turns toward Table A (green circle).\n"
                    "Step 2 — Notice the printed count after delivery — cups "
                    "is now 2.\n"
                    "Step 3 — Add a second cups -= 1 and print — what is "
                    "cups now?"
                ),
                "trigger": {"type": "enter", "zone": "GreenZone"},
                "script": (
                    "# Mission 2: Updating variables — deliver one cup to Table A\n"
                    "#\n"
                    "# cups -= 1 subtracts 1 from cups each time a cup is delivered.\n"
                    "# Use print() with an f-string to watch the count go down.\n"
                    "#\n"
                    "# This script continues from where Mission 1 ended (at the counter).\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "cups = 3\n"
                    "print(f\"Cups collected: {cups}\")\n"
                    "\n"
                    "# Turn south and drive back towards the tables\n"
                    "drive(0, 1.0)       # turn 180° to face south\n"
                    "time.sleep(0.60)\n"
                    "drive(0.4, 0)       # drive south toward table level\n"
                    "time.sleep(0.90)\n"
                    "drive(0, 1.0)       # turn right (west) toward Table A\n"
                    "time.sleep(0.30)\n"
                    "drive(0.4, 0)       # drive west to Table A (green circle)\n"
                    "time.sleep(1.1)\n"
                    "drive(0, 0)\n"
                    "\n"
                    "cups -= 1           # delivered one cup — update the variable\n"
                    "print(f\"Delivered to Table A! Cups remaining: {cups}\")\n"
                    "\n"
                    "# Goal: reach the green circle at Table A."
                ),
            },
            {
                "id":          "Mission 3",
                "title":       "Variable Check — Complete the Round",
                "description": (
                    "Python Concept: using a variable inside an if statement\n\n"
                    "Variables become powerful inside if statements: "
                    "if cups == 0: print(\"Done!\").\n\n"
                    "Step 1 — Run the starter code. Robby finishes at "
                    "Table B (yellow circle).\n"
                    "Step 2 — Add the if cups == 0 check at the end.\n"
                    "Step 3 — Change cups = 3 to cups = 2 at the top — "
                    "what message prints at the end?"
                ),
                "trigger": {"type": "enter", "zone": "YellowZone"},
                "script": (
                    "# Mission 3: Variable check — complete the full delivery round\n"
                    "#\n"
                    "# After all deliveries, check if cups == 0 and print the correct message.\n"
                    "# This connects variable state to a decision — a key programming skill.\n"
                    "#\n"
                    "# This script continues from where Mission 2 ended (at Table A).\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "cups = 3\n"
                    "print(f\"Starting delivery round. Cups: {cups}\")\n"
                    "\n"
                    "# Deliver to Table A (green circle) — already visited in Mission 2\n"
                    "cups -= 1\n"
                    "print(f\"Table A done. Cups left: {cups}\")\n"
                    "\n"
                    "# Turn east and drive across to Table B (yellow circle)\n"
                    "drive(0, 1.0)       # turn 180° to face east\n"
                    "time.sleep(0.60)\n"
                    "drive(0.4, 0)       # drive east across the shop\n"
                    "time.sleep(2.1)\n"
                    "drive(0, 0)\n"
                    "\n"
                    "cups -= 1           # delivered final cup\n"
                    "print(f\"Table B done. Cups left: {cups}\")\n"
                    "\n"
                    "# Add your variable check below:\n"
                    "# if cups == 0:\n"
                    "#     print(\"All delivered! Shift complete.\")\n"
                    "\n"
                    "# Goal: reach the yellow circle at Table B."
                ),
            },
        ],
        "learning_outcomes": (
            "1. Student can declare and assign a variable using = and print its "
            "value using print() with an f-string — e.g., cups = 3 followed by "
            "print(f\"Cups: {cups}\").\n"
            "2. Student understands how to update a variable in place using += "
            "and -= and can trace the changing value through a sequence of "
            "operations — e.g., cups = 3 then cups -= 1 gives cups == 2.\n"
            "3. Student can use a variable inside an if statement to control "
            "program flow — e.g., if cups == 0: print(\"Done!\") — connecting "
            "stored state to a decision."
        ),
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 3 ─────────────────────────────────────────────────────────────
    {
        "number":     3,
        "title":      "Loops",
        "subtitle":   "Teaching your program to repeat.",
        "status":     "available",
        "world_file": "chapter3_corridor.py",
        "concepts":   ["while", "while True", "if inside loop", "distance()"],
        "story": (
            "Robby has been assigned to patrol a long storage corridor. Two "
            "thick white walls seal the north and south ends. There are no "
            "manual controls this time — Robby must navigate using code "
            "alone.\n\n"
            "The challenge is that she does not know in advance how many "
            "steps to take before hitting a wall. Instead of counting steps, "
            "she needs to keep sensing the distance ahead and react when the "
            "reading drops too low.\n\n"
            "In this chapter you will use a while loop to give Robby the "
            "ability to keep checking, keep moving, and keep adapting — "
            "every single update."
        ),
        "missions": [
            {
                "id":          "Mission 1",
                "title":       "while — Drive Until Close",
                "description": (
                    "Python Concept: while loop with a condition\n\n"
                    "A while loop runs the indented block repeatedly as long "
                    "as its condition is True. When the condition becomes "
                    "False, the loop stops.\n\n"
                    "    while distance(0) > 1.0:\n"
                    "        drive(0.4, 0)\n"
                    "    drive(0, 0)\n\n"
                    "Step 1 — Enable 'Run forever' and click Run.\n"
                    "Step 2 — Watch Robby drive north and stop short of "
                    "the wall.\n"
                    "Step 3 — Change 1.0 to 0.5 then to 2.0 — how does "
                    "that change where Robby stops?"
                ),
                "trigger": {"type": "enter", "zone": "BlueZone"},
                "script": (
                    "# Mission 1: while — Drive until close to the north wall\n"
                    "#\n"
                    "# A while loop repeats as long as its condition is True.\n"
                    "# When distance(0) drops below the threshold, the loop ends.\n"
                    "#\n"
                    "# Enable 'Run forever' before clicking Run.\n"
                    "\n"
                    "while distance(0) > 1.0:\n"
                    "    drive(0.4, 0)    # drive forward while wall is far\n"
                    "\n"
                    "drive(0, 0)          # stop when wall is close\n"
                    "print(f\"Stopped. Distance ahead: {distance(0):.2f} m\")\n"
                    "\n"
                    "# Try changing 1.0 to 0.5 or 2.0.\n"
                    "# Goal: stop Robby inside the blue circle near the north wall."
                ),
            },
            {
                "id":          "Mission 2",
                "title":       "if inside while — Sense and Turn",
                "description": (
                    "Python Concept: if statement inside a while loop; "
                    "turning 180°\n\n"
                    "Combining if with while lets Robby react inside the "
                    "loop. When distance(0) drops below SAFE, she turns 180° "
                    "and heads toward the opposite wall.\n\n"
                    "Note: distance(0) always reads FORWARD — after turning "
                    "180°, it now measures toward the south wall.\n\n"
                    "Step 1 — Read and run the starter code with 'Run forever'.\n"
                    "Step 2 — Watch Robby drive north, detect the wall, "
                    "turn, and head south.\n"
                    "Step 3 — Guide Robby into the orange circle (south wall "
                    "zone) to complete the mission."
                ),
                "trigger": {"type": "enter", "zone": "OrangeZone"},
                "script": (
                    "# Mission 2: if inside while — detect the wall and turn\n"
                    "#\n"
                    "# Add an if statement inside the while loop.\n"
                    "# When the wall ahead is too close, turn 180° to face the other way.\n"
                    "#\n"
                    "# Note: distance(0) always reads FORWARD, relative to Robby's heading.\n"
                    "# After a 180° turn, distance(0) now reads toward the opposite wall.\n"
                    "#\n"
                    "# Enable 'Run forever' before clicking Run.\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "SAFE = 1.0       # turn when closer than this (metres)\n"
                    "\n"
                    "while True:\n"
                    "    if distance(0) < SAFE:\n"
                    "        drive(0, 1.0)        # spin right\n"
                    "        time.sleep(0.60)     # ~180° turn\n"
                    "    else:\n"
                    "        drive(0.4, 0)        # wall is far — drive forward\n"
                    "        time.sleep(0.05)     # short pause between sensor reads\n"
                    "\n"
                    "# Goal: guide Robby into the orange circle near the south wall."
                ),
            },
            {
                "id":          "Mission 3",
                "title":       "while True — Bounce Between the Walls",
                "description": (
                    "Python Concept: while True loop with continuous distance "
                    "sensing; full bounce loop\n\n"
                    "while True runs forever until the program is stopped. By "
                    "using distance(0) inside the loop, Robby keeps reading "
                    "the closest wall ahead and turns whenever it is too close. "
                    "The loop repeats — sense → decide → act — endlessly.\n\n"
                    "Step 1 — Click Reset to place Robby back at the start.\n"
                    "Step 2 — Run the starter code with 'Run forever'.\n"
                    "Step 3 — Watch Robby bounce between the two walls.\n"
                    "Step 4 — Adjust SAFE and the turn sleep time to get "
                    "clean, even bounces."
                ),
                "trigger": {"type": "enter", "zone": "BlueZone"},
                "script": (
                    "# Mission 3: while True — bounce between both walls forever\n"
                    "#\n"
                    "# Robby keeps sensing the wall ahead. When it is too close, she turns 180°.\n"
                    "# The loop never ends on its own — click Stop when you are done.\n"
                    "#\n"
                    "# Click Reset first to place Robby at the starting position.\n"
                    "# Enable 'Run forever' before clicking Run.\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "SAFE = 1.0        # distance threshold (metres) — try 0.8 or 1.5\n"
                    "\n"
                    "while True:\n"
                    "    if distance(0) < SAFE:\n"
                    "        drive(0, 1.0)        # spin right — turn around\n"
                    "        time.sleep(0.60)     # ~180° — adjust for a cleaner turn\n"
                    "    else:\n"
                    "        drive(0.4, 0)        # drive forward — wall is still far\n"
                    "        time.sleep(0.05)     # short pause between sensor reads\n"
                    "\n"
                    "# Goal: Robby bounces cleanly between both walls.\n"
                    "# The blue circle (north wall) triggers Mission 3 complete."
                ),
            },
        ],
        "learning_outcomes": (
            "1. Student can write a while loop with a sensor-based condition — "
            "e.g., while distance(0) > 1.0: drive forward — and explain why "
            "the loop stops when the condition becomes False.\n"
            "2. Student understands how to embed an if statement inside a while "
            "loop to react to changing sensor readings — e.g., turning Robby "
            "around when the wall ahead is too close.\n"
            "3. Student can construct a while True loop that runs indefinitely, "
            "using distance() to continuously sense the environment and "
            "drive()/time.sleep() to act, demonstrating the sense → decide → "
            "act cycle."
        ),
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 4 ─────────────────────────────────────────────────────────────
    {
        "number":     4,
        "title":      "Functions",
        "subtitle":   "Writing reusable blocks of code.",
        "status":     "available",
        "world_file": "chapter4_coffeeshop.py",
        "concepts":   ["def", "function call", "()", "composing functions", "return"],
        "story": (
            "The afternoon rush is over at the coffee shop. Dirty plates have "
            "been left on tables across the room — and Robby needs to collect "
            "them and return them to the kitchen hatch in the north-east corner.\n\n"
            "The problem is that Robby will need to do the same three steps over "
            "and over: look around, pick up a plate, and drop it off at the "
            "kitchen. Writing those steps out in full every time would be "
            "exhausting — and hard to fix if something went wrong.\n\n"
            "In this chapter you will write functions — named, reusable blocks "
            "of code. Define look(), pick_up(), and drop_off() once, then call "
            "them whenever Robby needs to clean up."
        ),
        "missions": [
            {
                "id":          "Mission 1",
                "title":       "def — Define a look() Function",
                "description": (
                    "Python Concept: def — defining and calling a function\n\n"
                    "def creates a named block of code. Define it once, call "
                    "it as many times as you need by writing its name followed "
                    "by ().\n\n"
                    "    def look():\n"
                    "        print(f\"Ahead: {distance(0):.1f} m\")\n\n"
                    "    look()   # call the function\n\n"
                    "Step 1 — Read the starter code. Find the def look(): block.\n"
                    "Step 2 — Enable 'Run forever' and click Run. Watch Robby "
                    "drive toward Plate A while the readings print.\n"
                    "Step 3 — Add a new print line inside look() to also show "
                    "distance(270). Run again — does the new reading appear "
                    "both times look() is called?"
                ),
                "trigger": {"type": "enter", "zone": "GreenZone"},
                "script": (
                    "# Mission 1: def — Define a look() function\n"
                    "#\n"
                    "# def creates a reusable named block of code.\n"
                    "# Call it any number of times by writing its name followed by ().\n"
                    "#\n"
                    "# Enable 'Run forever' before clicking Run.\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "def look():\n"
                    "    \"\"\"Read distances in four directions and report what Robby sees.\"\"\"\n"
                    "    print(f\"North (ahead): {distance(0):.1f} m\")\n"
                    "    print(f\"East  (right): {distance(90):.1f} m\")\n"
                    "    print(f\"South (behind): {distance(180):.1f} m\")\n"
                    "    print(f\"West  (left):  {distance(270):.1f} m\")\n"
                    "\n"
                    "# Call look() from the start — what does Robby sense?\n"
                    "print(\"--- From start ---\")\n"
                    "look()\n"
                    "\n"
                    "# Drive north toward Plate A (green circle)\n"
                    "while distance(0) > 0.5:\n"
                    "    drive(0.4, 0)\n"
                    "drive(0, 0)\n"
                    "\n"
                    "# Call look() again — the readings have changed\n"
                    "print(\"--- At Plate A ---\")\n"
                    "look()\n"
                    "\n"
                    "# Goal: reach the green circle beside Plate A."
                ),
            },
            {
                "id":          "Mission 2",
                "title":       "pick_up() and drop_off() — One Job Each",
                "description": (
                    "Python Concept: multiple functions — each with one clear job\n\n"
                    "Each function should do one thing well. pick_up() drives "
                    "to the plate. drop_off() carries it to the kitchen. "
                    "Calling them in order completes one delivery:\n\n"
                    "    pick_up()    # go to plate\n"
                    "    drop_off()   # take it to kitchen\n\n"
                    "Step 1 — Click Reset, then run the starter code.\n"
                    "Step 2 — Watch Robby drive north to Plate A (pick_up), "
                    "then turn east and head to the kitchen hatch (drop_off).\n"
                    "Step 3 — Swap the two calls: put drop_off() before "
                    "pick_up(). What happens? Why?"
                ),
                "trigger": {"type": "enter", "zone": "BlueZone"},
                "script": (
                    "# Mission 2: pick_up() and drop_off() — one job each\n"
                    "#\n"
                    "# Each function has a single clear purpose.\n"
                    "# pick_up() drives to the dirty plate.\n"
                    "# drop_off() carries it east then north to the kitchen hatch.\n"
                    "#\n"
                    "# Click Reset to start from the beginning.\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "def pick_up():\n"
                    "    \"\"\"Drive north to the dirty plate.\"\"\"\n"
                    "    while distance(0) > 0.5:\n"
                    "        drive(0.4, 0)   # move toward the plate\n"
                    "    drive(0, 0)\n"
                    "    print(\"Plate collected!\")\n"
                    "\n"
                    "def drop_off():\n"
                    "    \"\"\"Drive east then north to the kitchen hatch (blue circle).\"\"\"\n"
                    "    drive(0, 1.0)        # turn right — face east\n"
                    "    time.sleep(0.30)\n"
                    "    drive(0.4, 0)        # drive east toward kitchen column\n"
                    "    time.sleep(2.3)      # adjust until aligned with kitchen hatch\n"
                    "    drive(0, -1.0)       # turn left — face north\n"
                    "    time.sleep(0.30)\n"
                    "    drive(0.4, 0)        # drive north to kitchen hatch\n"
                    "    time.sleep(0.65)     # adjust until Robby reaches the blue circle\n"
                    "    drive(0, 0)\n"
                    "    print(\"Plate delivered to kitchen!\")\n"
                    "\n"
                    "pick_up()    # drive to Plate A\n"
                    "drop_off()   # take it to the kitchen\n"
                    "\n"
                    "# Goal: reach the blue circle at the kitchen hatch."
                ),
            },
            {
                "id":          "Mission 3",
                "title":       "clean_table() — A Function That Calls Functions",
                "description": (
                    "Python Concept: composing functions — a function that "
                    "calls other functions\n\n"
                    "A function can call other functions. clean_table() wraps "
                    "look(), pick_up(), and drop_off() into one named action. "
                    "Call clean_table() whenever a plate needs collecting:\n\n"
                    "    def clean_table():\n"
                    "        look()\n"
                    "        pick_up()\n"
                    "        drop_off()\n\n"
                    "Step 1 — Click Reset, then run the starter code.\n"
                    "Step 2 — Watch Robby perform one full clean-up cycle: "
                    "scan, collect, deliver.\n"
                    "Step 3 — Uncomment the while True loop at the bottom. "
                    "What would happen if the plates never ran out?"
                ),
                "trigger": {"type": "enter", "zone": "BlueZone"},
                "script": (
                    "# Mission 3: clean_table() — a function that calls functions\n"
                    "#\n"
                    "# A function can call other functions inside it.\n"
                    "# clean_table() packages the whole clean-up cycle into one name.\n"
                    "#\n"
                    "# Click Reset to start from the beginning.\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "def look():\n"
                    "    \"\"\"Report what Robby sees in all four directions.\"\"\"\n"
                    "    print(f\"North: {distance(0):.1f} m  |  East: {distance(90):.1f} m\")\n"
                    "    print(f\"South: {distance(180):.1f} m  |  West: {distance(270):.1f} m\")\n"
                    "\n"
                    "def pick_up():\n"
                    "    \"\"\"Drive north to the dirty plate.\"\"\"\n"
                    "    while distance(0) > 0.5:\n"
                    "        drive(0.4, 0)\n"
                    "    drive(0, 0)\n"
                    "    print(\"Plate collected!\")\n"
                    "\n"
                    "def drop_off():\n"
                    "    \"\"\"Carry the plate east then north to the kitchen hatch.\"\"\"\n"
                    "    drive(0, 1.0);  time.sleep(0.30)   # face east\n"
                    "    drive(0.4, 0);  time.sleep(2.3)    # drive east\n"
                    "    drive(0, -1.0); time.sleep(0.30)   # face north\n"
                    "    drive(0.4, 0);  time.sleep(0.65)   # drive to kitchen\n"
                    "    drive(0, 0)\n"
                    "    print(\"Plate delivered!\")\n"
                    "\n"
                    "def clean_table():\n"
                    "    \"\"\"One full clean-up cycle: look, collect, deliver.\"\"\"\n"
                    "    look()\n"
                    "    pick_up()\n"
                    "    drop_off()\n"
                    "\n"
                    "# Call clean_table() to perform one complete delivery\n"
                    "clean_table()\n"
                    "\n"
                    "# To keep cleaning as long as plates appear, use a loop:\n"
                    "# while True:\n"
                    "#     clean_table()\n"
                    "\n"
                    "# Goal: reach the blue circle at the kitchen hatch."
                ),
            },
        ],
        "learning_outcomes": (
            "1. Student can define a function using def and call it by name — "
            "e.g., def look(): followed by look() — and explain why calling "
            "the same function twice produces different output when Robby has "
            "moved.\n"
            "2. Student understands how to split a task into focused functions "
            "— pick_up() for navigation to the plate and drop_off() for the "
            "return journey — and can predict what happens when the call order "
            "is changed.\n"
            "3. Student can compose functions by calling look(), pick_up(), and "
            "drop_off() inside a clean_table() wrapper, and can explain how a "
            "while True loop would allow Robby to keep cleaning indefinitely."
        ),
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 5 ─────────────────────────────────────────────────────────────
    {
        "number":     5,
        "title":      "Data Structure",
        "subtitle":   "Lists and Dictionaries.",
        "status":     "available",
        "world_file": "chapter5_coffeeshop.py",
        "concepts":   ["list", "dictionary", "indexing", "keys", "values", "append()", "len()"],
        "story": (
            "It is morning set-up time at the coffee shop. Cups, plates, "
            "knives, and forks are piled on the counter waiting to be laid "
            "out. Robby needs to figure out what is there — and keep track "
            "of it all in one go.\n\n"
            "Storing every item in its own variable would be exhausting. "
            "Instead, Python gives us two powerful tools: a list groups "
            "items in order so you can count, index, and loop over them; "
            "a dictionary maps names to values so you can look up exactly "
            "what you need by key.\n\n"
            "In this chapter you will use a list to inventory the counter, "
            "a dictionary to record each table's order, and a list of "
            "dictionaries to build the full service plan for the morning rush."
        ),
        "missions": [
            {
                "id":          "Mission 1",
                "title":       "Lists — Inventory the Counter",
                "description": (
                    "Python Concept: list, indexing with [], len()\n\n"
                    "A list stores multiple items in order under one name. "
                    "Use [] to create it and to access items by position "
                    "(index). Indexing starts at 0. Use len() to count "
                    "how many items are inside.\n\n"
                    "    counter = [\"Cup\", \"Cup\", \"Plate\", \"Plate\",\n"
                    "               \"Knife\", \"Knife\", \"Fork\", \"Fork\"]\n"
                    "    print(len(counter))     # 8\n"
                    "    print(counter[0])       # 'Cup'\n"
                    "    print(counter[-1])      # 'Fork'\n\n"
                    "Step 1 — Read the starter code. Spot where the list is "
                    "created and where items are accessed by index.\n"
                    "Step 2 — Click Run and watch Robby drive to the counter "
                    "(cyan circle) while the inventory prints.\n"
                    "Step 3 — Add a print that shows counter[2] — what "
                    "item is at index 2? Why?"
                ),
                "trigger": {"type": "enter", "zone": "CyanZone"},
                "script": (
                    "# Mission 1: Lists — Inventory the counter\n"
                    "#\n"
                    "# A list stores multiple items in order under one name.\n"
                    "# Access items by index (starting at 0). Use len() to count them.\n"
                    "#\n"
                    "# Try: print(counter[2]) — what item is at index 2?\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "# Build a list of every item on the counter\n"
                    "counter = [\"Cup\", \"Cup\", \"Plate\", \"Plate\",\n"
                    "           \"Knife\", \"Knife\", \"Fork\", \"Fork\"]\n"
                    "\n"
                    "print(f\"Items on the counter: {len(counter)}\")\n"
                    "print(f\"First item : {counter[0]}\")    # index 0 = first\n"
                    "print(f\"Last item  : {counter[-1]}\")   # index -1 = last\n"
                    "\n"
                    "# Drive north to the counter (cyan circle)\n"
                    "drive(0.4, 0)\n"
                    "time.sleep(2.2)   # adjust until Robby reaches the cyan circle\n"
                    "drive(0, 0)\n"
                    "\n"
                    "print(f\"At the counter. Ready to lay out {len(counter)} items.\")\n"
                    "\n"
                    "# Goal: reach the cyan circle at the counter."
                ),
            },
            {
                "id":          "Mission 2",
                "title":       "Dictionaries — Build a Table Order",
                "description": (
                    "Python Concept: dictionary, keys, values, dict[key], "
                    "updating a value\n\n"
                    "A dictionary maps keys to values — like a menu: "
                    "look up the item name, get the quantity. Use a string "
                    "key in [] to read or update a value.\n\n"
                    "    order = {\"cups\": 2, \"plates\": 2,\n"
                    "             \"knives\": 2, \"forks\": 2}\n"
                    "    print(order[\"cups\"])    # 2\n"
                    "    order[\"cups\"] -= 1     # one cup placed\n"
                    "    print(order[\"cups\"])    # 1\n\n"
                    "Step 1 — Run the starter code. Robby drives to Table A "
                    "(green circle) while the order is printed.\n"
                    "Step 2 — Notice how order[\"cups\"] changes after one "
                    "cup is placed.\n"
                    "Step 3 — Add order[\"forks\"] -= 1 and print — what "
                    "does the updated dict look like?"
                ),
                "trigger": {"type": "enter", "zone": "GreenZone"},
                "script": (
                    "# Mission 2: Dictionaries — build a table order\n"
                    "#\n"
                    "# A dictionary maps keys to values.\n"
                    "# Use a key in [] to look up or update its value.\n"
                    "#\n"
                    "# This script continues from where Mission 1 ended (at the counter).\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "# Each key is an item name; each value is the quantity needed\n"
                    "order = {\"cups\": 2, \"plates\": 2, \"knives\": 2, \"forks\": 2}\n"
                    "print(f\"Table A order: {order}\")\n"
                    "print(f\"Cups to place: {order['cups']}\")\n"
                    "\n"
                    "# One cup has already been placed — update the count\n"
                    "order[\"cups\"] -= 1\n"
                    "print(f\"After placing one cup: {order}\")\n"
                    "\n"
                    "# Navigate south from the counter to Table A (green circle)\n"
                    "drive(0, 1.0)       # 180° turn to face south\n"
                    "time.sleep(0.60)\n"
                    "drive(0.4, 0)       # drive south toward table level\n"
                    "time.sleep(0.90)\n"
                    "drive(0, 1.0)       # turn right (west) toward Table A\n"
                    "time.sleep(0.30)\n"
                    "drive(0.4, 0)       # drive west to Table A (green circle)\n"
                    "time.sleep(1.1)\n"
                    "drive(0, 0)\n"
                    "\n"
                    "print(f\"At Table A. Remaining items: {order}\")\n"
                    "\n"
                    "# Goal: reach the green circle at Table A."
                ),
            },
            {
                "id":          "Mission 3",
                "title":       "List of Dictionaries — The Full Service Plan",
                "description": (
                    "Python Concept: list of dictionaries, append(), for "
                    "loop over a list\n\n"
                    "A list of dictionaries stores a collection of records — "
                    "one dict per table, all held together in a list. Use "
                    "append() to add a new record, and a for loop to go "
                    "through them all.\n\n"
                    "    tables = [\n"
                    "        {\"name\": \"Table A\", \"cups\": 2},\n"
                    "        {\"name\": \"Table B\", \"cups\": 3},\n"
                    "    ]\n"
                    "    tables.append({\"name\": \"Table C\", \"cups\": 1})\n"
                    "    for t in tables:\n"
                    "        print(t[\"name\"], t[\"cups\"])\n\n"
                    "Step 1 — Run the starter code. Robby drives to Table B "
                    "(yellow circle) while the full plan prints.\n"
                    "Step 2 — Uncomment the for loop and run again — each "
                    "table's order appears on its own line.\n"
                    "Step 3 — Add a fourth table entry with append() — does "
                    "it appear in the loop output?"
                ),
                "trigger": {"type": "enter", "zone": "YellowZone"},
                "script": (
                    "# Mission 3: List of dictionaries — the full service plan\n"
                    "#\n"
                    "# A list of dictionaries stores one record per table.\n"
                    "# Use append() to add a table and a for loop to print them all.\n"
                    "#\n"
                    "# This script continues from where Mission 2 ended (at Table A).\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "# Build the morning service plan — one dict per table\n"
                    "tables = [\n"
                    "    {\"name\": \"Table A\", \"cups\": 2, \"plates\": 2, \"knives\": 2, \"forks\": 2},\n"
                    "    {\"name\": \"Table B\", \"cups\": 3, \"plates\": 2, \"knives\": 2, \"forks\": 2},\n"
                    "]\n"
                    "\n"
                    "# Add a last-minute booking with append()\n"
                    "tables.append({\"name\": \"Table C\", \"cups\": 1, \"plates\": 1, \"knives\": 1, \"forks\": 1})\n"
                    "\n"
                    "print(f\"Tables to serve today: {len(tables)}\")\n"
                    "\n"
                    "# Uncomment the loop to print every table's order:\n"
                    "# for table in tables:\n"
                    "#     print(f\"{table['name']}: {table['cups']} cups, \"\n"
                    "#           f\"{table['plates']} plates, {table['knives']} knives, \"\n"
                    "#           f\"{table['forks']} forks\")\n"
                    "\n"
                    "# Drive east from Table A to Table B (yellow circle)\n"
                    "drive(0, 1.0)       # 180° turn to face east\n"
                    "time.sleep(0.60)\n"
                    "drive(0.4, 0)       # drive east across the shop\n"
                    "time.sleep(2.1)\n"
                    "drive(0, 0)\n"
                    "\n"
                    "print(\"At Table B. Morning service plan complete!\")\n"
                    "\n"
                    "# Goal: reach the yellow circle at Table B."
                ),
            },
        ],
        "learning_outcomes": (
            "1. Student can create a list, access items by index (including "
            "negative indexing), and use len() to count the items — e.g., "
            "counter = [\"Cup\", \"Plate\", \"Knife\"] then counter[0] returns "
            "\"Cup\" and len(counter) returns 3.\n"
            "2. Student understands how to create a dictionary, look up a value "
            "by key, and update it in place — e.g., order[\"cups\"] -= 1 — "
            "and can explain the difference between a list (ordered by position) "
            "and a dictionary (looked up by key).\n"
            "3. Student can build a list of dictionaries, add a new record with "
            "append(), and iterate over it with a for loop — connecting the two "
            "data structures to model a real-world collection of records."
        ),
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 6 ─────────────────────────────────────────────────────────────
    {
        "number":     6,
        "title":      "Maths Algorithms",
        "subtitle":   "Using maths and logic to solve problems step by step.",
        "status":     "available",
        "world_file": "chapter6_coffeeshop.py",
        "concepts":   ["+", "-", "*", "//", "%", "parameters", "return", "accumulator"],
        "story": (
            "It is closing time at the coffee shop. Three tables have been "
            "cleared but the used cups and dishes are still sitting out. "
            "Before Robby can finish her shift she needs to count everything "
            "up — how many coffees were served, how many dishes need washing, "
            "and what the totals look like across all three tables.\n\n"
            "This chapter is about writing algorithms: step-by-step "
            "instructions that use maths to work out an answer. You will use "
            "arithmetic operators to calculate quantities, write functions "
            "that accept numbers as inputs and return a result, and build a "
            "loop that accumulates a running total across every table.\n\n"
            "By the end, Robby will know exactly how many items are heading "
            "to the kitchen — without counting a single thing by hand."
        ),
        "missions": [
            {
                "id":          "Mission 1",
                "title":       "Arithmetic — How Many Coffees Today?",
                "description": (
                    "Python Concept: arithmetic operators "
                    "+  −  *  //  %\n\n"
                    "Python can calculate with numbers just like a "
                    "calculator. // gives the whole-number quotient "
                    "(integer division) and % gives the remainder.\n\n"
                    "    ordered  = 24\n"
                    "    served   = 17\n"
                    "    leftover = ordered - served      # 7\n"
                    "    per_table = ordered // 3         # 8\n"
                    "    remainder = ordered % 3          # 0\n\n"
                    "Step 1 — Read the starter code and trace each "
                    "calculation on paper before you run it.\n"
                    "Step 2 — Click Run and watch Robby drive to the "
                    "counter (cyan circle) while the totals print.\n"
                    "Step 3 — Change ordered to 25 and re-run. What "
                    "does 25 // 3 give? What is 25 % 3?"
                ),
                "trigger": {"type": "enter", "zone": "CyanZone"},
                "script": (
                    "# Mission 1: Arithmetic — how many coffees today?\n"
                    "#\n"
                    "# Use +, -, *, //, % to calculate with numbers.\n"
                    "# // = integer division (whole part only)\n"
                    "# %  = remainder (what is left over)\n"
                    "#\n"
                    "# Try: change ordered to 25. What does 25 // 3 give?\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "ordered   = 24        # coffees ordered today\n"
                    "served    = 17        # coffees actually served\n"
                    "leftover  = ordered - served          # still to serve\n"
                    "per_table = ordered // 3              # spread across 3 tables\n"
                    "remainder = ordered % 3               # cups that don't divide evenly\n"
                    "\n"
                    "print(f\"Coffees ordered : {ordered}\")\n"
                    "print(f\"Coffees served  : {served}\")\n"
                    "print(f\"Still to serve  : {leftover}\")\n"
                    "print(f\"Average per table : {per_table}  (remainder: {remainder})\")\n"
                    "\n"
                    "# Drive north to the counter (cyan circle)\n"
                    "drive(0.4, 0)\n"
                    "time.sleep(2.2)\n"
                    "drive(0, 0)\n"
                    "\n"
                    "print(f\"At the counter. {leftover} coffees still to go!\")\n"
                    "\n"
                    "# Goal: reach the cyan circle at the counter."
                ),
            },
            {
                "id":          "Mission 2",
                "title":       "Parameters and return — calc_dishes()",
                "description": (
                    "Python Concept: function parameters and return value\n\n"
                    "A function can accept inputs (parameters) and send "
                    "a result back (return). This makes the same "
                    "calculation reusable for any table:\n\n"
                    "    def calc_dishes(cups, plates, knives, forks):\n"
                    "        return cups + plates + knives + forks\n\n"
                    "    table_a = calc_dishes(2, 2, 2, 2)   # 8\n"
                    "    table_b = calc_dishes(3, 3, 3, 3)   # 12\n\n"
                    "Step 1 — Run the starter code. Watch the per-table "
                    "counts print as Robby heads to Table A (green circle).\n"
                    "Step 2 — Call calc_dishes again with different "
                    "numbers — the function does the maths every time.\n"
                    "Step 3 — Add a knives parameter to a call and see "
                    "how the total changes."
                ),
                "trigger": {"type": "enter", "zone": "GreenZone"},
                "script": (
                    "# Mission 2: Parameters and return — calc_dishes()\n"
                    "#\n"
                    "# A function with parameters accepts inputs and return sends the result back.\n"
                    "# The same function works for any table — just pass different numbers.\n"
                    "#\n"
                    "# This script continues from where Mission 1 ended (at the counter).\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "def calc_dishes(cups, plates, knives, forks):\n"
                    "    \"\"\"Return the total number of dirty dishes for one table.\"\"\"\n"
                    "    return cups + plates + knives + forks\n"
                    "\n"
                    "# Table A had 2 customers\n"
                    "table_a = calc_dishes(cups=2, plates=2, knives=2, forks=2)\n"
                    "print(f\"Table A dishes: {table_a}\")\n"
                    "\n"
                    "# Table B had 3 customers\n"
                    "table_b = calc_dishes(cups=3, plates=3, knives=3, forks=3)\n"
                    "print(f\"Table B dishes: {table_b}\")\n"
                    "\n"
                    "print(f\"Tables A + B combined: {table_a + table_b}\")\n"
                    "\n"
                    "# Navigate south from the counter to Table A (green circle)\n"
                    "drive(0, 1.0)       # 180° turn to face south\n"
                    "time.sleep(0.60)\n"
                    "drive(0.4, 0)       # drive south toward table level\n"
                    "time.sleep(0.90)\n"
                    "drive(0, 1.0)       # turn right (west) toward Table A\n"
                    "time.sleep(0.30)\n"
                    "drive(0.4, 0)       # drive west to Table A (green circle)\n"
                    "time.sleep(1.1)\n"
                    "drive(0, 0)\n"
                    "\n"
                    "print(f\"At Table A. {table_a} dishes to collect here.\")\n"
                    "\n"
                    "# Goal: reach the green circle at Table A."
                ),
            },
            {
                "id":          "Mission 3",
                "title":       "Accumulator — Total for All Tables",
                "description": (
                    "Python Concept: accumulator pattern — building a "
                    "running total inside a loop\n\n"
                    "Start a variable at zero, then add to it each time "
                    "through the loop. After the loop it holds the grand "
                    "total.\n\n"
                    "    total = 0\n"
                    "    for table in tables:\n"
                    "        dishes = calc_dishes(...)\n"
                    "        total += dishes\n"
                    "    print(total)\n\n"
                    "Step 1 — Click Reset and run the starter code. "
                    "Watch total grow with each table.\n"
                    "Step 2 — Add a fourth table to the list — does "
                    "the total update automatically?\n"
                    "Step 3 — Add a cups_total accumulator alongside "
                    "total — can you count just the cups across all "
                    "tables?"
                ),
                "trigger": {"type": "enter", "zone": "YellowZone"},
                "script": (
                    "# Mission 3: Accumulator — total dishes for all tables\n"
                    "#\n"
                    "# Start total at 0, then add each table's count inside the loop.\n"
                    "# After the loop, total holds the grand sum.\n"
                    "#\n"
                    "# This script continues from where Mission 2 ended (at Table A).\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "def calc_dishes(cups, plates, knives, forks):\n"
                    "    \"\"\"Return the total number of dirty dishes for one table.\"\"\"\n"
                    "    return cups + plates + knives + forks\n"
                    "\n"
                    "# Service log — one dict per table\n"
                    "tables = [\n"
                    "    {\"name\": \"Table A\", \"cups\": 2, \"plates\": 2, \"knives\": 2, \"forks\": 2},\n"
                    "    {\"name\": \"Table B\", \"cups\": 3, \"plates\": 3, \"knives\": 3, \"forks\": 3},\n"
                    "    {\"name\": \"Table C\", \"cups\": 1, \"plates\": 1, \"knives\": 1, \"forks\": 1},\n"
                    "]\n"
                    "\n"
                    "total = 0            # accumulator — starts at zero\n"
                    "for table in tables:\n"
                    "    dishes = calc_dishes(table[\"cups\"], table[\"plates\"],\n"
                    "                         table[\"knives\"], table[\"forks\"])\n"
                    "    print(f\"{table['name']}: {dishes} dishes\")\n"
                    "    total += dishes  # add this table's count to the running total\n"
                    "\n"
                    "print(f\"Total dishes to wash today: {total}\")\n"
                    "\n"
                    "# Drive east from Table A to Table B (yellow circle)\n"
                    "drive(0, 1.0)       # 180° turn to face east\n"
                    "time.sleep(0.60)\n"
                    "drive(0.4, 0)       # drive east across the shop\n"
                    "time.sleep(2.1)\n"
                    "drive(0, 0)\n"
                    "\n"
                    "print(f\"Shift complete! {total} dishes heading to the kitchen.\")\n"
                    "\n"
                    "# Goal: reach the yellow circle at Table B."
                ),
            },
        ],
        "learning_outcomes": (
            "1. Student can use arithmetic operators (+, -, *, //, %) to "
            "calculate integer and remainder results — e.g., 24 // 3 gives "
            "the average coffees per table and 24 % 3 gives the remainder — "
            "and can predict the output before running the code.\n"
            "2. Student can write a function with parameters and a return "
            "value — e.g., def calc_dishes(cups, plates, knives, forks): "
            "return cups + plates + knives + forks — and understands that "
            "calling the function with different arguments reuses the same "
            "calculation without rewriting it.\n"
            "3. Student can apply the accumulator pattern: initialise a "
            "variable to 0, loop over a list of dictionaries, call a "
            "calculation function each iteration, and add the result to the "
            "running total — producing the correct grand sum for any number "
            "of tables."
        ),
        "educator_notes":  "Enter your notes here.",
    },

    # ── Chapter 7 ─────────────────────────────────────────────────────────────
    {
        "number":     7,
        "title":      "Navigation Algorithms",
        "subtitle":   "Line following, obstacle avoidance and wall following.",
        "status":     "available",
        "world_file": "chapter7_maze.py",
        "concepts":   ["while True", "look()", "distance()", "if/elif/else", "control loop", "sensor feedback"],
        "story": (
            "The café has run out of coffee. The last delivery bag is sitting "
            "in the warehouse — but the only way in is through the old service "
            "maze that connects the back of the café to the storeroom. Nobody "
            "has used it in years, and the lights inside are dim.\n\n"
            "Robby is sent in alone. The maze has three sections. The first "
            "is a dark entry hall where a faded yellow line on the floor marks "
            "the safe path — follow it north and Robby will find the gap in the "
            "first barrier. Beyond that is an open arena scattered with heavy "
            "red pillars left by the last renovation. Robby cannot push them — "
            "she must sense them early and steer around each one. The third "
            "section is a narrow exit corridor. There are no more markers, no "
            "map. Robby's only guide is the right-hand wall — keep it at a "
            "steady distance and it will lead to the warehouse door.\n\n"
            "Each section teaches a different algorithm for navigating an "
            "unknown environment. Together they form a complete robotic "
            "navigation toolkit — the same techniques used in real self-driving "
            "vehicles and warehouse robots today."
        ),
        "missions": [
            {
                "id":    "Mission 1",
                "title": "Line Following — Stay on the Yellow Path",
                "description": (
                    "Python Concepts: while True loop, look(), if/elif/else, "
                    "control loop\n\n"
                    "look() returns a list of visible objects. Each entry is:\n"
                    "    [shape, colour, distance, heading, height, width]\n\n"
                    "heading is the angle from Robby's forward direction to the "
                    "object. Positive = object is to the right; "
                    "negative = object is to the left.\n\n"
                    "Line-following rule:\n"
                    "    objects = look()\n"
                    "    yellow  = [o for o in objects if o[1] == \"Yellow\"]\n"
                    "    if yellow:\n"
                    "        heading = yellow[0][3]      # index 3 = heading\n"
                    "        if   heading >  5: drive(0.3,  0.5)  # steer right\n"
                    "        elif heading < -5: drive(0.3, -0.5)  # steer left\n"
                    "        else:              drive(0.4,  0  )  # straight\n\n"
                    "Step 1 — Run the starter code. Watch Robby track the "
                    "yellow markers north toward the gap in Wall 1.\n"
                    "Step 2 — Try changing the heading threshold from 5 to 15. "
                    "Does Robby weave more or less?\n"
                    "Step 3 — What happens if you increase STEER from 0.5 to "
                    "0.9? Can Robby still follow the line smoothly?"
                ),
                "trigger": {"type": "enter", "zone": "LineZone"},
                "script": (
                    "# Mission 1: Line Following — Stay on the Yellow Path\n"
                    "#\n"
                    "# look() returns objects seen by the camera:\n"
                    "#   [shape, colour, distance, heading, height, width]\n"
                    "# heading > 0 → marker is to the RIGHT → steer right (+angular)\n"
                    "# heading < 0 → marker is to the LEFT  → steer left  (-angular)\n"
                    "#\n"
                    "# Try: change STEER or the heading threshold and observe the effect.\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "SPEED  = 0.35    # forward speed (0.0 – 1.0)\n"
                    "STEER  = 0.5     # turning strength when off-centre\n"
                    "THRESH = 5       # degrees — ignore small heading errors\n"
                    "\n"
                    "print(\"Scanning for yellow line...\")\n"
                    "\n"
                    "while True:\n"
                    "    objects = look()\n"
                    "    yellow  = [o for o in objects if o[1] == \"Yellow\"]\n"
                    "\n"
                    "    if yellow:\n"
                    "        nearest = min(yellow, key=lambda o: o[2])  # closest marker\n"
                    "        heading = nearest[3]                        # angle to marker\n"
                    "        print(f\"Line heading: {heading:+.1f}°  dist: {nearest[2]:.2f} m\")\n"
                    "\n"
                    "        if heading > THRESH:\n"
                    "            drive(SPEED,  STEER)    # marker is right — steer right\n"
                    "        elif heading < -THRESH:\n"
                    "            drive(SPEED, -STEER)    # marker is left  — steer left\n"
                    "        else:\n"
                    "            drive(SPEED, 0)         # marker is ahead — straight\n"
                    "    else:\n"
                    "        drive(SPEED * 0.6, 0)       # no marker visible — coast forward\n"
                    "\n"
                    "    time.sleep(0.05)\n"
                    "\n"
                    "# Goal: reach the orange circle just past Wall 1."
                ),
            },
            {
                "id":    "Mission 2",
                "title": "Obstacle Avoidance — Navigate the Red Pillars",
                "description": (
                    "Python Concepts: distance(), multi-angle sensing, "
                    "reactive steering\n\n"
                    "distance(A) returns the LiDAR reading at angle A "
                    "(clockwise from forward). Use three angles to get a "
                    "360° picture of what is ahead:\n\n"
                    "    front      = distance(0)    # straight ahead\n"
                    "    front_left = distance(315)  # 45° to the left\n"
                    "    front_right= distance(45)   # 45° to the right\n\n"
                    "Avoidance rule:\n"
                    "    if front > SAFE and front_left > SAFE and front_right > SAFE:\n"
                    "        drive(0.35, 0)           # all clear\n"
                    "    elif front_right < front_left:\n"
                    "        drive(0.3, -0.7)         # obstacle right — turn left\n"
                    "    else:\n"
                    "        drive(0.3,  0.7)         # obstacle left  — turn right\n\n"
                    "Step 1 — Run the code. Robby steers around all three "
                    "red pillars to reach the gap in Wall 2.\n"
                    "Step 2 — Change SAFE from 1.2 to 0.8. Does Robby cut "
                    "the corners closer? Is that safer or riskier?\n"
                    "Step 3 — Add distance(0) < 0.35 as an emergency-stop "
                    "condition. When would this be useful?"
                ),
                "trigger": {"type": "enter", "zone": "ArenaZone"},
                "script": (
                    "# Mission 2: Obstacle Avoidance — Navigate the Red Pillars\n"
                    "#\n"
                    "# distance(A) returns the LiDAR reading at angle A (clockwise).\n"
                    "# Use front, front-left and front-right to detect obstacles early.\n"
                    "#\n"
                    "# This script continues from where Mission 1 ended (past Wall 1).\n"
                    "# Try: lower SAFE to 0.8 and see how Robby's path changes.\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "SAFE  = 1.2     # metres — start turning before this distance\n"
                    "SPEED = 0.35    # forward speed\n"
                    "\n"
                    "print(\"Entering obstacle arena. Sensors active...\")\n"
                    "\n"
                    "while True:\n"
                    "    front       = distance(0)    # straight ahead\n"
                    "    front_right = distance(45)   # 45° to the right\n"
                    "    front_left  = distance(315)  # 45° to the left (315 = -45)\n"
                    "\n"
                    "    print(f\"F: {front:.2f}  FR: {front_right:.2f}  FL: {front_left:.2f}\")\n"
                    "\n"
                    "    if front > SAFE and front_right > SAFE and front_left > SAFE:\n"
                    "        drive(SPEED, 0)           # all clear — go straight\n"
                    "    elif front_right < front_left:\n"
                    "        drive(SPEED, -0.7)        # obstacle right-front — turn left\n"
                    "    else:\n"
                    "        drive(SPEED,  0.7)        # obstacle left-front  — turn right\n"
                    "\n"
                    "    time.sleep(0.05)\n"
                    "\n"
                    "# Goal: reach the green circle just past Wall 2."
                ),
            },
            {
                "id":    "Mission 3",
                "title": "Wall Following — Find the Exit",
                "description": (
                    "Python Concepts: distance(90), proportional error, "
                    "close_enough(), attach()\n\n"
                    "The right-hand wall rule: always keep the right wall "
                    "at a fixed distance. In an unknown maze, this guarantees "
                    "you will eventually find the exit.\n\n"
                    "    TARGET = 0.85    # metres from right wall\n"
                    "    right  = distance(90)\n"
                    "    error  = right - TARGET\n"
                    "    # positive error → too far from wall → steer right\n"
                    "    # negative error → too close to wall → steer left\n"
                    "    if   error >  0.2: drive(0.3,  0.4)  # drift right\n"
                    "    elif error < -0.2: drive(0.3, -0.4)  # drift left\n"
                    "    else:              drive(0.3,  0  )  # on track\n\n"
                    "Once close_enough() is True, attach() picks up the "
                    "coffee bag.\n\n"
                    "Step 1 — Run the code. Robby follows the right wall "
                    "north through the corridor to the coffee bag.\n"
                    "Step 2 — Change TARGET to 0.5. Robby now hugs the "
                    "right wall. Does she reach the bag?\n"
                    "Step 3 — Try left-hand wall following: use distance(270) "
                    "and flip the steer directions. Does it still find the exit?"
                ),
                "trigger": {"type": "attach", "object": "CoffeeBag"},
                "script": (
                    "# Mission 3: Wall Following — Find the Exit\n"
                    "#\n"
                    "# Keep the right wall (distance(90)) at TARGET metres.\n"
                    "# Compute the error and steer to correct it each loop tick.\n"
                    "# When close_enough() to the CoffeeBag, stop and attach().\n"
                    "#\n"
                    "# This script continues from where Mission 2 ended (past Wall 2).\n"
                    "# Try: change TARGET to 0.5 (hug the wall) or 1.2 (hug the left).\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "TARGET    = 0.85   # desired distance from right corridor wall\n"
                    "TOLERANCE = 0.20   # acceptable error band\n"
                    "SPEED     = 0.25   # forward speed (slow — stay in control)\n"
                    "\n"
                    "print(\"Entering exit corridor. Following right wall to the warehouse...\")\n"
                    "\n"
                    "while True:\n"
                    "    right = distance(90)          # distance to right corridor wall\n"
                    "    error = right - TARGET        # +ve = too far, -ve = too close\n"
                    "\n"
                    "    print(f\"Right wall: {right:.2f} m   Error: {error:+.2f} m\")\n"
                    "\n"
                    "    if close_enough():\n"
                    "        drive(0, 0)\n"
                    "        break                     # coffee bag is in reach!\n"
                    "    elif error > TOLERANCE:\n"
                    "        drive(SPEED,  0.4)        # too far from wall — steer right\n"
                    "    elif error < -TOLERANCE:\n"
                    "        drive(SPEED, -0.4)        # too close to wall — steer left\n"
                    "    else:\n"
                    "        drive(SPEED, 0)           # on target — straight ahead\n"
                    "\n"
                    "    time.sleep(0.05)\n"
                    "\n"
                    "drive(0, 0)\n"
                    "attach()\n"
                    "print(f\"Coffee bag secured! Holding: {holding()}\")\n"
                    "print(\"Robby has the coffee. The café is saved!\")\n"
                    "\n"
                    "# Goal: attach the CoffeeBag at the end of the corridor."
                ),
            },
        ],
        "learning_outcomes": (
            "1. Student can implement a line-following control loop using look() "
            "to retrieve the nearest yellow object, read its heading field, and "
            "apply proportional steering (if heading > threshold: steer right, "
            "elif heading < -threshold: steer left) so the robot tracks a "
            "sequence of floor markers.\n"
            "2. Student can implement a reactive obstacle-avoidance loop using "
            "distance() at three forward angles (0°, 45°, 315°) and a SAFE "
            "threshold, comparing front-left vs front-right readings to choose "
            "which way to turn — and can explain why reducing SAFE increases "
            "risk of collision.\n"
            "3. Student can implement a right-hand wall-following loop using "
            "distance(90) and an error term (right − TARGET), steering "
            "proportionally to stay within a TOLERANCE band, and using "
            "close_enough() as the exit condition before calling attach() — "
            "and can adapt the same algorithm for left-hand wall following by "
            "switching to distance(270) and inverting the steering directions."
        ),
        "educator_notes": (
            "The three missions form a linear path through the maze and build "
            "on each other: Mission 1 uses the camera (look()), Mission 2 uses "
            "LiDAR (distance()), and Mission 3 combines LiDAR with attach(). "
            "All three are instances of the same pattern — a sense-decide-act "
            "control loop — which is worth naming explicitly.\n\n"
            "Common misconceptions to address:\n"
            "- look() heading: students often confuse positive/negative. "
            "Remind them that positive angular velocity turns right, and "
            "positive heading means the target is to the right.\n"
            "- distance(315) vs distance(-45): both are valid for the "
            "front-left diagonal — good opportunity to review the modulo "
            "behaviour described in the spec.\n"
            "- Wall-following threshold: if TOLERANCE is too small the robot "
            "oscillates; if too large it drifts. This is a real PID tuning "
            "concept and connects well to Chapter 8's maths algorithms.\n\n"
            "Extension: ask students to combine all three algorithms into a "
            "single while True loop that handles any zone of the maze "
            "automatically by detecting which sensor type is most useful."
        ),
    },

    # ── Chapter 8 ─────────────────────────────────────────────────────────────
    {
        "number":     8,
        "title":      "Evaluation",
        "subtitle":   "Searching, Sorting, Counting and Math algorithms.",
        "status":     "available",
        "world_file": "chapter8_competition.py",
        "concepts":   ["list of dicts", "accumulator", "linear search", "bubble sort", "sorted()", "lambda", "score formula"],
        "story": (
            "It is the annual Café Bot Championship — the only competition "
            "in the city where service robots race to clear customer tables "
            "and deliver dirty cups and dishes to the kitchen. The café owner "
            "has set the timer. Three rival robots — R-Alpha, R-Beta and "
            "R-Gamma — have already run their laps and posted their scores "
            "on the leaderboard.\n\n"
            "Now it is Robby's turn. Five tables are still loaded with cups "
            "and dishes from the lunch rush. Robby needs to think like a "
            "computer scientist: first survey the floor and build an "
            "inventory list, then search for the busiest table, sort all "
            "tables into the smartest collection order, pick up a cup and "
            "sprint to the kitchen — and finally, calculate every robot's "
            "competition score and find out whether Robby wins the trophy.\n\n"
            "This chapter combines everything you have learned: lists and "
            "dictionaries to store the table data, linear search to find "
            "the maximum, bubble sort to order the route, loops and attach "
            "to drive the delivery, and arithmetic to produce the final "
            "leaderboard. It is not just about finishing — it is about "
            "finishing smart."
        ),
        "missions": [
            {
                "id":    "Mission 1",
                "title": "Count the Cargo — Build the Inventory",
                "description": (
                    "Python Concepts: list of dictionaries, for loop, "
                    "accumulator\n\n"
                    "The floor has five tables. Each table has a different "
                    "number of dirty cups and dishes. Store each table as a "
                    "dictionary inside a list, then loop through and add up "
                    "the totals:\n\n"
                    "    tables = [\n"
                    "        {\"id\": \"T1\", \"items\": 3},\n"
                    "        {\"id\": \"T2\", \"items\": 1},\n"
                    "        ...\n"
                    "    ]\n\n"
                    "    total = 0\n"
                    "    for t in tables:\n"
                    "        total += t[\"items\"]\n"
                    "    print(f\"Total items: {total}\")\n\n"
                    "Step 1 — Read the starter code and predict the total "
                    "before you run it.\n"
                    "Step 2 — Click Run and watch Robby head north to the "
                    "kitchen (cyan circle) to report the count.\n"
                    "Step 3 — Add a new table {\"id\": \"T6\", \"items\": 2} "
                    "to the list. Does the total update automatically?"
                ),
                "trigger": {"type": "enter", "zone": "KitchenZone"},
                "script": (
                    "# Mission 1: Count the Cargo — Build the Inventory\n"
                    "#\n"
                    "# Use a list of dicts to store each table's dirty-item count.\n"
                    "# Loop through the list with an accumulator to find the grand total.\n"
                    "#\n"
                    "# Try: add {\"id\": \"T6\", \"items\": 2} to tables and re-run.\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "# Five tables — one dict per table\n"
                    "tables = [\n"
                    "    {\"id\": \"T1\", \"x\": 2.0, \"y\": 6.5, \"items\": 3},   # 3 cups at T1\n"
                    "    {\"id\": \"T2\", \"x\": 5.0, \"y\": 6.5, \"items\": 1},   # 1 cup  at T2\n"
                    "    {\"id\": \"T3\", \"x\": 8.0, \"y\": 6.5, \"items\": 5},   # 5 cups at T3\n"
                    "    {\"id\": \"T4\", \"x\": 2.0, \"y\": 4.0, \"items\": 2},   # 2 dishes at T4\n"
                    "    {\"id\": \"T5\", \"x\": 8.0, \"y\": 4.0, \"items\": 4},   # 4 dishes at T5\n"
                    "]\n"
                    "\n"
                    "total = 0                       # accumulator — starts at zero\n"
                    "for t in tables:\n"
                    "    print(f\"  {t['id']}: {t['items']} items\")\n"
                    "    total += t[\"items\"]         # add this table's count\n"
                    "\n"
                    "print(f\"\\nTotal dirty items on the floor: {total}\")\n"
                    "print(\"Heading to the kitchen to report...\")\n"
                    "\n"
                    "# Drive north to KitchenZone (cyan circle at the counter)\n"
                    "drive(0.4, 0)\n"
                    "time.sleep(2.0)\n"
                    "drive(0, 0)\n"
                    "\n"
                    "print(\"Inventory reported. Kitchen is ready!\")\n"
                    "\n"
                    "# Goal: reach the cyan circle at the kitchen counter."
                ),
            },
            {
                "id":    "Mission 2",
                "title": "Linear Search — Find the Busiest Table",
                "description": (
                    "Python Concept: linear search — scanning a list to "
                    "find the item with the highest value\n\n"
                    "A linear search checks every item in the list one by "
                    "one. Here, you need to find the table with the most "
                    "dirty items so Robby clears it first:\n\n"
                    "    busiest = tables[0]          # start with first\n"
                    "    for t in tables:\n"
                    "        if t[\"items\"] > busiest[\"items\"]:\n"
                    "            busiest = t          # found a busier one\n"
                    "    print(busiest[\"id\"])\n\n"
                    "Step 1 — Trace through the loop on paper. Which table "
                    "is busiest? (Hint: count the items in the list.)\n"
                    "Step 2 — Click Run. Robby drives from the kitchen "
                    "south-east to the busiest table (red circle).\n"
                    "Step 3 — Change T3's item count to 2. Which table "
                    "becomes busiest now? Does Robby's destination change?"
                ),
                "trigger": {"type": "enter", "zone": "T3Zone"},
                "script": (
                    "# Mission 2: Linear Search — Find the Busiest Table\n"
                    "#\n"
                    "# Scan every item in the list and track the one with the most items.\n"
                    "# This script continues from where Mission 1 ended (at the kitchen).\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "tables = [\n"
                    "    {\"id\": \"T1\", \"x\": 2.0, \"y\": 6.5, \"items\": 3},\n"
                    "    {\"id\": \"T2\", \"x\": 5.0, \"y\": 6.5, \"items\": 1},\n"
                    "    {\"id\": \"T3\", \"x\": 8.0, \"y\": 6.5, \"items\": 5},\n"
                    "    {\"id\": \"T4\", \"x\": 2.0, \"y\": 4.0, \"items\": 2},\n"
                    "    {\"id\": \"T5\", \"x\": 8.0, \"y\": 4.0, \"items\": 4},\n"
                    "]\n"
                    "\n"
                    "# Linear search — find the table with the most items\n"
                    "busiest = tables[0]             # assume the first is busiest to start\n"
                    "for t in tables:\n"
                    "    if t[\"items\"] > busiest[\"items\"]:\n"
                    "        busiest = t             # update whenever a busier table is found\n"
                    "\n"
                    "print(f\"Busiest table: {busiest['id']} — {busiest['items']} items!\")\n"
                    "print(\"Heading there first...\")\n"
                    "\n"
                    "# Drive from kitchen (5,8.5) south-east to T3 (8,6.5)\n"
                    "drive(0, 1.0)       # turn right to face east\n"
                    "time.sleep(0.30)\n"
                    "drive(0.4, 0)       # drive east toward T3\n"
                    "time.sleep(0.90)\n"
                    "drive(0, 1.0)       # turn right to face south\n"
                    "time.sleep(0.30)\n"
                    "drive(0.4, 0)       # drive south to table row\n"
                    "time.sleep(0.60)\n"
                    "drive(0, 0)\n"
                    "\n"
                    "print(f\"At {busiest['id']}. {busiest['items']} dirty cups waiting!\")\n"
                    "\n"
                    "# Goal: reach the red circle at Table T3."
                ),
            },
            {
                "id":    "Mission 3",
                "title": "Bubble Sort — Plan the Route, Deliver the Cup",
                "description": (
                    "Python Concepts: bubble sort, attach / detach\n\n"
                    "A bubble sort rearranges a list by repeatedly comparing "
                    "neighbouring items and swapping them when they are in "
                    "the wrong order. Sorting by item count (highest first) "
                    "gives Robby the most efficient collection route:\n\n"
                    "    for i in range(len(tables)):\n"
                    "        for j in range(len(tables) - 1 - i):\n"
                    "            if tables[j][\"items\"] < tables[j+1][\"items\"]:\n"
                    "                tables[j], tables[j+1] = tables[j+1], tables[j]\n\n"
                    "After sorting, Robby picks up the cup at T3 (the first "
                    "stop on the route) and carries it back to the kitchen.\n\n"
                    "Step 1 — Run the code. Check the printed route is: "
                    "T3, T5, T1, T4, T2.\n"
                    "Step 2 — Watch Robby attach the cup at T3 and drive "
                    "to the kitchen (cyan circle).\n"
                    "Step 3 — Change the items values and re-run. Does the "
                    "sort order change correctly?"
                ),
                "trigger": {"type": "enter_with", "zone": "KitchenZone", "object": "Cup3"},
                "script": (
                    "# Mission 3: Bubble Sort — Plan the Route, Deliver the Cup\n"
                    "#\n"
                    "# Sort tables by item count (highest first) using bubble sort.\n"
                    "# Then pick up Cup3 at T3 and carry it to the kitchen.\n"
                    "# This script continues from where Mission 2 ended (at Table T3).\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "tables = [\n"
                    "    {\"id\": \"T1\", \"x\": 2.0, \"y\": 6.5, \"items\": 3},\n"
                    "    {\"id\": \"T2\", \"x\": 5.0, \"y\": 6.5, \"items\": 1},\n"
                    "    {\"id\": \"T3\", \"x\": 8.0, \"y\": 6.5, \"items\": 5},\n"
                    "    {\"id\": \"T4\", \"x\": 2.0, \"y\": 4.0, \"items\": 2},\n"
                    "    {\"id\": \"T5\", \"x\": 8.0, \"y\": 4.0, \"items\": 4},\n"
                    "]\n"
                    "\n"
                    "# Bubble sort — sort descending by items (most first)\n"
                    "for i in range(len(tables)):\n"
                    "    for j in range(len(tables) - 1 - i):\n"
                    "        if tables[j][\"items\"] < tables[j + 1][\"items\"]:\n"
                    "            tables[j], tables[j + 1] = tables[j + 1], tables[j]\n"
                    "\n"
                    "print(\"Optimal collection route:\")\n"
                    "for rank, t in enumerate(tables, 1):\n"
                    "    print(f\"  {rank}. {t['id']} — {t['items']} items\")\n"
                    "\n"
                    "# Pick up the cup at T3 (robot is here from Mission 2)\n"
                    "attach()\n"
                    "print(\"\\nCup3 picked up! Racing to the kitchen...\")\n"
                    "\n"
                    "# Drive west then north from T3 (8,6.5) to KitchenZone (5,8.5)\n"
                    "drive(0, 1.0)       # turn right to face west\n"
                    "time.sleep(0.30)\n"
                    "drive(0.4, 0)       # drive west toward centre\n"
                    "time.sleep(0.90)\n"
                    "drive(0, 1.0)       # turn right to face north\n"
                    "time.sleep(0.30)\n"
                    "drive(0.4, 0)       # drive north to kitchen\n"
                    "time.sleep(0.60)\n"
                    "drive(0, 0)\n"
                    "\n"
                    "detach()\n"
                    "print(\"Cup3 delivered to the kitchen!\")\n"
                    "\n"
                    "# Goal: reach the cyan circle while carrying Cup3."
                ),
            },
            {
                "id":    "Mission 4",
                "title": "Leaderboard — Who Wins the Trophy?",
                "description": (
                    "Python Concepts: score formula, sorted() with key=, "
                    "lambda\n\n"
                    "The competition score is: jobs_done / time_seconds * 100. "
                    "A higher score means more jobs done in less time.\n\n"
                    "    score = jobs / time * 100\n\n"
                    "sorted() lets you rank a list of dicts by any field "
                    "using a key function:\n\n"
                    "    leaderboard = sorted(\n"
                    "        robots,\n"
                    "        key=lambda r: r[\"score\"],\n"
                    "        reverse=True\n"
                    "    )\n\n"
                    "Step 1 — The starter code includes Robby's result. "
                    "Predict who wins before you run.\n"
                    "Step 2 — Click Run and read the printed leaderboard. "
                    "Watch Robby drive south to the podium (gold circle).\n"
                    "Step 3 — Change Robby's time to 35 seconds. Does she "
                    "move up the leaderboard?"
                ),
                "trigger": {"type": "enter", "zone": "PodiumZone"},
                "script": (
                    "# Mission 4: Leaderboard — Who Wins the Trophy?\n"
                    "#\n"
                    "# Calculate each robot's score (jobs / time * 100), sort the list,\n"
                    "# print the leaderboard, then drive south to the podium.\n"
                    "# This script continues from where Mission 3 ended (at the kitchen).\n"
                    "\n"
                    "import time\n"
                    "\n"
                    "# Competition results — Robby's entry is already included!\n"
                    "robots = [\n"
                    "    {\"name\": \"R-Alpha\", \"jobs\": 11, \"time\": 45},\n"
                    "    {\"name\": \"R-Beta\",  \"jobs\":  8, \"time\": 30},\n"
                    "    {\"name\": \"R-Gamma\", \"jobs\": 13, \"time\": 65},\n"
                    "    {\"name\": \"Robby\",   \"jobs\": 15, \"time\": 47},   # ← Robby's result\n"
                    "]\n"
                    "\n"
                    "# Calculate score for every robot\n"
                    "for r in robots:\n"
                    "    r[\"score\"] = round(r[\"jobs\"] / r[\"time\"] * 100, 1)\n"
                    "\n"
                    "# Sort by score — highest first\n"
                    "leaderboard = sorted(robots, key=lambda r: r[\"score\"], reverse=True)\n"
                    "\n"
                    "print(\"=== CAFÉ BOT CHAMPIONSHIP LEADERBOARD ===\")\n"
                    "medals = [\"1st \", \"2nd \", \"3rd \", \"4th \"]\n"
                    "for rank, r in enumerate(leaderboard):\n"
                    "    medal = medals[rank] if rank < len(medals) else f\"{rank+1}th \"\n"
                    "    print(f\"  {medal} {r['name']:10s}  jobs={r['jobs']}  \"\n"
                    "          f\"time={r['time']}s  score={r['score']}\")\n"
                    "\n"
                    "winner = leaderboard[0]\n"
                    "print(f\"\\nWinner: {winner['name']} with a score of {winner['score']}!\")\n"
                    "\n"
                    "# Drive south from kitchen (5,8.5) to PodiumZone (5,1.5)\n"
                    "drive(0, 1.0)       # turn right 180° to face south\n"
                    "time.sleep(0.60)\n"
                    "drive(0.5, 0)       # sprint south to the podium\n"
                    "time.sleep(2.20)\n"
                    "drive(0, 0)\n"
                    "\n"
                    "if winner[\"name\"] == \"Robby\":\n"
                    "    print(\"Robby takes the trophy!\")\n"
                    "else:\n"
                    "    print(f\"{winner['name']} wins — change Robby's numbers and try again!\")\n"
                    "\n"
                    "# Goal: reach the gold circle at the podium."
                ),
            },
        ],
        "learning_outcomes": (
            "1. Student can build a list of dictionaries representing real-world "
            "data (tables with item counts), loop through the list with a for "
            "loop, and apply the accumulator pattern to compute a grand total — "
            "producing the correct sum for any number of entries.\n"
            "2. Student can implement a linear search by initialising a 'best so "
            "far' variable to the first element and updating it inside a loop "
            "whenever a larger value is found — correctly identifying the "
            "dictionary with the maximum items field.\n"
            "3. Student can implement a bubble sort using nested for loops and "
            "a simultaneous swap (a, b = b, a) to sort a list of dictionaries "
            "in descending order by a numeric field — and can explain why the "
            "inner loop bound shrinks by i each pass.\n"
            "4. Student can calculate a formula-based score for each item in a "
            "list, use sorted() with a lambda key function and reverse=True to "
            "rank the results, and correctly identify the winner from the "
            "printed leaderboard."
        ),
        "educator_notes": (
            "Missions 1–4 form a single end-to-end narrative. Each mission "
            "continues from the robot's position at the end of the previous one, "
            "so they are best run in sequence without pressing Reset between them.\n\n"
            "The competition framing (rival robots R-Alpha, R-Beta, R-Gamma) "
            "motivates the score calculation in Mission 4. Students who make "
            "Robby win by adjusting her numbers see concretely that a higher "
            "score means more efficient delivery.\n\n"
            "Common extension tasks: (a) replace bubble sort with Python's "
            "built-in sorted() and compare code length; (b) add a 'distance' "
            "field to each table dict and modify the score formula to account "
            "for travel time; (c) implement binary search on the sorted list "
            "to find a specific table by item count."
        ),
    },

]
