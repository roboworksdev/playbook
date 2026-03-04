"""Robby Chronicles — curriculum content for all 8 chapters."""

import os

_DIR     = os.path.dirname(os.path.abspath(__file__))
ROBOSIM  = os.path.join(_DIR, "RoboSim")   # path to RoboSim project folder


def script_path(filename: str) -> str:
    return os.path.join(ROBOSIM, filename)


CHAPTERS = [
    # ── Chapter 0 ─────────────────────────────────────────────────────────────
    {
        "number":     0,
        "title":      "First Boot",
        "subtitle":   "Robby powers on for the very first time.",
        "status":     "available",
        "world_file": "chapter0_lab.py",
        "concepts":   ["print()", "f-strings", "variables", "battery_level()"],
        "story": (
            "Robby (Autonomous Robotic Intelligence Agent) powers on in a quiet "
            "research laboratory. Her motors are locked. Her sensors are dim. "
            "But her communication channel is open.\n\n"
            "You are the engineer assigned to restore her. Your first mission: "
            "help Robby speak."
        ),
        "missions": [
            {
                "id":          "0.1",
                "title":       "First Words",
                "description": "Run print(\"Robby online.\") — Robby's very first script.",
                "script":      "ch0_m1_first_words.py",
            },
            {
                "id":          "0.2",
                "title":       "Battery Report",
                "description": "Print Robby's battery level using an f-string.",
                "script":      "ch0_m2_battery_report.py",
            },
            {
                "id":          "0.3",
                "title":       "Identity",
                "description": "Store Robby's name in a variable and print a greeting.",
                "script":      "ch0_m3_variables.py",
            },
        ],
        "educator_notes": (
            "Never introduce syntax and meaning simultaneously. The single biggest "
            "barrier for new programmers is RUNNING a program for the first time — "
            "this chapter removes every other barrier before that moment.\n\n"
            "Mission 0.1 should take under 5 minutes. If it takes longer, something "
            "in the environment setup is wrong — fix that first.\n\n"
            "Prediction habit: before clicking Run, ask learners 'What do you think "
            "will appear?' This builds the mental model that code has predictable "
            "outcomes — the foundation of debugging.\n\n"
            "Common confusion: learners often try to type in the 3D viewport instead "
            "of the script editor. Show the OPEN EDITOR button explicitly first."
        ),
        "hardware_bridge": (
            "Demonstrate print() in a Raspberry Pi terminal:\n\n"
            "    pi@raspberrypi:~ $ python3\n"
            "    >>> print(\"Robby online.\")\n"
            "    Robby online.\n\n"
            "Identical syntax. Identical output. The only difference is the hardware "
            "underneath. This establishes the simulation → physical pipeline from Day 1."
        ),
    },

    # ── Chapter 1 ─────────────────────────────────────────────────────────────
    {
        "number":     1,
        "title":      "Learning to Walk",
        "subtitle":   "Robby's motors are online. Time to move.",
        "status":     "available",
        "world_file": "chapter1_corridor.py",
        "concepts":   ["drive()", "time.sleep()", "for loop", "range()", "speed variable"],
        "story": (
            "Robby's motor systems have been unlocked. She can move — but she has "
            "never walked before.\n\n"
            "Deep in the north of the facility, the Power Room holds a charging "
            "station. Robby must reach it, learn to move precisely, and prove she "
            "is ready for the missions ahead.\n\n"
            "The corridor is clear. The charger is waiting. Teach Robby to walk."
        ),
        "missions": [
            {
                "id":          "1.1",
                "title":       "Drive to the Power Room",
                "description": "Script a timed drive north to the charger using drive() and time.sleep().",
                "script":      "ch1_m1_drive_to_charger.py",
            },
            {
                "id":          "1.2",
                "title":       "Walk the Square",
                "description": "Drive Robby in a square path using a for loop — four sides, four turns.",
                "script":      "ch1_m2_square_path.py",
            },
            {
                "id":          "1.3",
                "title":       "One Change, Big Difference",
                "description": "Change the SPEED variable and watch the whole behaviour adapt.",
                "script":      "ch1_m3_speed_variable.py",
            },
        ],
        "educator_notes": (
            "Use the loop-as-repetition-of-physical-act metaphor:\n"
            "\"Walk 4 steps forward, turn right. Do that 4 times.\"\n\n"
            "Let students PREDICT the shape before running. Draw it on paper first. "
            "This is the single most effective technique for building a loop mental model.\n\n"
            "Common misconception: drive(1.0, 0.0) doesn't mean 'move 1 metre' — "
            "it's a velocity command. Duration matters. Name this explicitly: "
            "this is open-loop vs closed-loop control.\n\n"
            "Mission 1.3 is the most important moment in the chapter. Ask: 'How many "
            "lines would you need to change if speed was written 10 times instead of "
            "stored in a variable?' Let them feel the answer."
        ),
        "hardware_bridge": (
            "Arduino equivalents:\n\n"
            "    drive(0.4, 0.0)  ≈  analogWrite(motorPin, 102)  // 40% of 255\n"
            "    time.sleep(2.4)  ≈  delay(2400)\n\n"
            "Motor PWM values map directly to drive() linear inputs. The open-loop "
            "timing problem (drift, imprecision) is identical in both environments — "
            "a powerful teachable moment about the limits of open-loop control."
        ),
    },

    # ── Chapter 2 ─────────────────────────────────────────────────────────────
    {
        "number":     2,
        "title":      "Eyes Wide Open",
        "subtitle":   "The room is dark. Robby must learn to sense.",
        "status":     "available",
        "world_file": "chapter2_dark_room.py",
        "concepts":   ["distance()", "if/elif/else", "Boolean expressions", "while loop", "Sense → Decide → Act"],
        "story": (
            "Robby enters the facility's old storage wing. The lights are on low "
            "power — the room is dim and cluttered with abandoned equipment.\n\n"
            "Her motors work, but without sensors she is blind. She cannot see "
            "Pillar_A directly in her path. You must teach Robby to feel the space "
            "around her and navigate without collision.\n\n"
            "The orange Sensor_Charger waits in the far north-east corner."
        ),
        "missions": [
            {
                "id":          "2.1",
                "title":       "Feel the Room",
                "description": "Read distance(angle) in 8 directions and find the nearest obstacle.",
                "script":      "ch2_m1_sense_distance.py",
            },
            {
                "id":          "2.2",
                "title":       "Stop Before You Hit",
                "description": "Drive north with a sensor-based stopping condition. Tune STOP_GAP.",
                "script":      "ch2_m2_stop_before_wall.py",
            },
            {
                "id":          "2.3",
                "title":       "Navigate the Dark Room",
                "description": "Reactive obstacle avoidance — Robby finds her own path to the charger.",
                "script":      "ch2_m3_avoid_obstacles.py",
            },
        ],
        "educator_notes": (
            "Problem-first pedagogy: do NOT explain if/else before Mission 2.2. "
            "Let Robby crash first (Mission 2.1 ends with Robby stationary). Ask "
            "'What would make her stop automatically?' THEN introduce the conditional.\n\n"
            "Write SENSE → DECIDE → ACT on the board. Every robot from a Roomba to "
            "a Mars rover uses this structure. Naming the pattern is as important as "
            "coding it.\n\n"
            "Common misconception — assignment vs comparison:\n"
            "    if distance = 1.0    ← assigns 1.0 to distance  (WRONG)\n"
            "    if distance(0) < 1.0 ← tests the condition       (CORRECT)\n\n"
            "Robby's error message when the wrong form is used IS the lesson. "
            "Do not rush past it — read it aloud and decode it together."
        ),
        "hardware_bridge": (
            "HC-SR04 Ultrasonic Sensor (Arduino):\n\n"
            "    long duration = pulseIn(echoPin, HIGH);\n"
            "    float dist = duration * 0.034 / 2;\n"
            "    if (dist < 10.0) { /* stop */ }\n\n"
            "Identical logic to:\n"
            "    if distance(0) < 1.0: drive(0.0, 0.0)\n\n"
            "Threshold values differ (cm vs metres) but the structure is identical. "
            "Show both side by side — same idea, different syntax."
        ),
    },

    # ── Chapter 3 ─────────────────────────────────────────────────────────────
    {
        "number":     3,
        "title":      "The Retrieval Mission",
        "subtitle":   "Four crates. One robot. No time to waste.",
        "status":     "available",
        "world_file": "chapter3_warehouse.py",
        "concepts":   ["close_enough()", "attach()", "detach()", "holding()", "def", "function parameters"],
        "story": (
            "A tremor shook the facility last night. Supply crates were scattered "
            "across the warehouse floor. The team needs them returned to the blue "
            "drop zone before the morning inspection.\n\n"
            "Robby has been assigned the task — four crates, one robot, no time "
            "to waste.\n\n"
            "Teach Robby a new skill: retrieve and deliver. Once she knows the skill, "
            "she can use it forever."
        ),
        "missions": [
            {
                "id":          "3.1",
                "title":       "Make Contact",
                "description": "Navigate to Crate_1, approach using close_enough(), and attach().",
                "script":      "ch3_m1_grab_crate.py",
            },
            {
                "id":          "3.2",
                "title":       "To the Drop Zone",
                "description": "Carry the attached crate to the blue drop zone and detach().",
                "script":      "ch3_m2_deliver_crate.py",
            },
            {
                "id":          "3.3",
                "title":       "Teach Robby a Skill",
                "description": "Extract grab-and-deliver into def collect_crate(cx, cy): and call it for all 4 crates.",
                "script":      "ch3_m3_collect_function.py",
            },
        ],
        "educator_notes": (
            "Use the 'teaching a new skill' metaphor:\n"
            "'Once you define a function, Robby knows that skill forever. "
            "The def block is the teaching. The call is using the skill.'\n\n"
            "Give learners the working sequential code FIRST (Missions 3.1 + 3.2). "
            "Only then ask: 'What would you change if you had to do this 4 times?' "
            "Let them feel the repetition problem before introducing def.\n\n"
            "Function parameters (cx, cy) are previewed here but covered fully in "
            "Chapter 4. Tell learners: 'Think of cx and cy as blank slots filled "
            "in when you call the function.'\n\n"
            "Assessment: Write def return_to_base(): that navigates Robby from any "
            "position back to (2.0, 2.0)."
        ),
        "hardware_bridge": (
            "Functions in Python = subroutines in Arduino C++:\n\n"
            "Python:                         Arduino C++:\n"
            "def collect_crate(cx, cy):       void collectCrate(float cx, float cy) {\n"
            "    navigate_to(cx, cy)              navigateTo(cx, cy);\n"
            "    attach()                         digitalWrite(magnetPin, HIGH);\n"
            "    deliver_to_zone()                deliverToZone();\n"
            "    detach()                         digitalWrite(magnetPin, LOW);\n"
            "                                 }\n\n"
            "The structure is identical. This is the moment to say: 'Programming "
            "languages are different ways of writing the same ideas.'"
        ),
    },

    # ── Chapters 4–7 (stubs) ──────────────────────────────────────────────────
    {
        "number":     4,
        "title":      "Running on Empty",
        "subtitle":   "Battery critical. Plan before you move.",
        "status":     "coming_soon",
        "world_file": "chapter4_multi_room.py",
        "concepts":   ["state variables", "global", "elif chains", "flowcharts", "program design"],
        "story":      "Robby's battery is critical. She must plan her route through a multi-room building, finding chargers before she loses power.",
        "missions":   [],
        "educator_notes":  "Content coming soon.",
        "hardware_bridge": "Content coming soon.",
    },
    {
        "number":     5,
        "title":      "The Robot Team",
        "subtitle":   "Three robots. One mission. Divide and conquer.",
        "status":     "coming_soon",
        "world_file": "chapter5_security_lab.py",
        "concepts":   ["multi-robot", "concurrent execution", "role-based design", "systems thinking"],
        "story":      "Robby finds two other robots. To pass the facility's final security door, all three must work in coordination.",
        "missions":   [],
        "educator_notes":  "Content coming soon.",
        "hardware_bridge": "Content coming soon.",
    },
    {
        "number":     6,
        "title":      "Map the Unknown",
        "subtitle":   "No map exists. Robby must build one herself.",
        "status":     "coming_soon",
        "world_file": "chapter6_unknown.py",
        "concepts":   ["lists", "NumPy arrays", "indexing", "SLAM", "occupancy grid"],
        "story":      "Robby must explore a completely unknown room and find a hidden artefact. No map exists — she must build one herself.",
        "missions":   [],
        "educator_notes":  "Content coming soon.",
        "hardware_bridge": "Content coming soon.",
    },
    {
        "number":     7,
        "title":      "Showtime",
        "subtitle":   "The National Robotics Showcase. Robby's final test.",
        "status":     "coming_soon",
        "world_file": "chapter7_arena.py",
        "concepts":   ["full integration", "autonomous planning", "capstone mission"],
        "story":      "Robby is selected for the National Robotics Showcase. The judges set a final mission. No guided steps — design the full solution from scratch.",
        "missions":   [],
        "educator_notes":  "Content coming soon.",
        "hardware_bridge": "Content coming soon.",
    },
]
