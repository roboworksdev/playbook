# =============================================================================
#  THE Robby CHRONICLES — Chapter 0: "First Boot"
#  World file for RoboSim5
# =============================================================================
#
#  STORY
#  -----
#  Robby powers on for the very first time in a quiet research laboratory.
#  Her motors are locked. Her sensors are dim. But her communication
#  channel is open. Your first mission: help Robby speak.
#
#  Open the Script Editor (OPEN EDITOR button) and complete the missions
#  below. Click RUN after writing each script.
#
#  MISSIONS
#  --------
#  [0.1]  Type this and run it:
#             print("Robby online.")
#         What text appears in the console?
#
#  [0.2]  Print Robby's current battery level using an f-string:
#             print(f"Battery level: {battery_level()}%")
#         What value does battery_level() return?
#
#  [0.3]  Use a variable to store Robby's name, then print a greeting:
#             name = "Robby"
#             model = "MK-1"
#             print(f"Unit {name} {model} standing by.")
#         Change the model number — what happens to the output?
#
#  KEY CONCEPTS IN THIS CHAPTER
#  ----------------------------
#    print()        →  sends text to the console
#    f"...{expr}..."→  f-string: embeds a value inside a string
#    variable = ...  →  stores a value with a name
#    battery_level() →  built-in robot API: returns % charge remaining
#
#  EDUCATOR NOTES  →  See The Robby Chronicles — Teacher Guide, Ch.0
# =============================================================================
#
#  WORLD LAYOUT  (10 m × 10 m, origin bottom-left)
#  ------------------------------------------------
#  Robby starts at (2.0, 2.0) facing North (+y direction).
#
#   W                              E
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌─────────────────────────────────┐
# 9 │ ◦[   W O R K B E N C H   ] ◦  │  ◦ = structural pillars
#   │  [T]     [T]     [T]           │  [T] = terminals
# 8 │                                │
#   │                     [Rack E1]  │
# 7 │ [Cab W]             [Rack E2]  │
#   │                                │
# 6 │                     [Rack E3]  │
#   │         (●) Lab Table          │
# 5 │        ⊙   ⊙                  │  (●) table, ⊙ = stools
#   │                                │
# 4 │                     · Sphere   │
#   │         ⊕ Charger              │
# 3 │                                │  ⊕ = Robby_Charger (orange)
#   │                                │
# 2 │  ★ Robby (2,2)                  │  ★ = robot start position
#   │                                │
# 1 │                                │
#   └─────────────────────────────────┘
#   0  1  2  3  4  5  6  7  8  9  10

# ── Structural support pillars ────────────────────────────────────────────────
#    cylinder  (diameter, height)
create_object("Pillar_NW",  "cylinder", "White",  "fixed",
              (0.25, 1.5, 0),  (1.0, 9.0, 0),  (0, 0, 0))

create_object("Pillar_NE",  "cylinder", "White",  "fixed",
              (0.25, 1.5, 0),  (9.0, 9.0, 0),  (0, 0, 0))

create_object("Pillar_SE",  "cylinder", "White",  "fixed",
              (0.25, 1.5, 0),  (9.0, 1.0, 0),  (0, 0, 0))

# ── North research workbench ──────────────────────────────────────────────────
#    box  (x-width, z-height, y-depth)
#    Spans x = 1.25 → 8.75,  y = 9.0 → 9.6
create_object("Lab_Bench",  "box",      "White",  "fixed",
              (7.5, 0.9, 0.6),  (5.0, 9.3, 0),  (0, 0, 0))

# ── Computer terminals on the bench ──────────────────────────────────────────
#    Narrow flat-screen panels sitting on the workbench surface
create_object("Terminal_A", "box",      "Green",  "fixed",
              (0.45, 0.65, 0.15),  (3.5, 9.0, 0),  (0, 0, 0))

create_object("Terminal_B", "box",      "Green",  "fixed",
              (0.45, 0.65, 0.15),  (5.0, 9.0, 0),  (0, 0, 0))

create_object("Terminal_C", "box",      "Green",  "fixed",
              (0.45, 0.65, 0.15),  (6.5, 9.0, 0),  (0, 0, 0))

# ── East wall equipment racks ─────────────────────────────────────────────────
#    Tall server/equipment racks lining the east wall
#    x-footprint: 9.45 → 9.95  (flush against east wall)
create_object("Rack_E1",    "box",      "Blue",   "fixed",
              (0.5, 1.5, 2.0),  (9.7, 7.5, 0),  (0, 0, 0))

create_object("Rack_E2",    "box",      "Blue",   "fixed",
              (0.5, 1.5, 2.0),  (9.7, 5.5, 0),  (0, 0, 0))

create_object("Rack_E3",    "box",      "Blue",   "fixed",
              (0.5, 1.5, 2.0),  (9.7, 3.0, 0),  (0, 0, 0))

# ── West wall storage cabinet ─────────────────────────────────────────────────
#    Large storage unit on the west side
#    x-footprint: 0.1 → 0.5  (flush against west wall)
create_object("Cabinet_W",  "box",      "White",  "fixed",
              (0.4, 1.5, 2.5),  (0.3, 6.5, 0),  (0, 0, 0))

# ── Central lab table (east side of room) ─────────────────────────────────────
#    x-footprint: 5.5 → 7.5,  y-footprint: 5.0 → 6.0
#    Placed east of centre so Robby's start zone (west side) stays clear
create_object("Lab_Table",  "box",      "White",  "fixed",
              (2.0, 0.8, 1.0),  (6.5, 5.5, 0),  (0, 0, 0))

# ── Lab stools beside the table ───────────────────────────────────────────────
create_object("Stool_1",    "cylinder", "Yellow", "fixed",
              (0.3, 0.65, 0),  (5.2, 5.0, 0),  (0, 0, 0))

create_object("Stool_2",    "cylinder", "Yellow", "fixed",
              (0.3, 0.65, 0),  (5.2, 6.0, 0),  (0, 0, 0))

# ── Specimen orb ──────────────────────────────────────────────────────────────
#    A small glowing sphere on the east side — a visible target for Robby's
#    LiDAR in Chapter 2.  Also useful for testing distance() now.
create_object("Specimen",   "sphere",   "Green",  "fixed",
              (0.35, 0, 0),  (8.5, 3.5, 0),  (0, 0, 0))

# ── Robby's Charging Station ───────────────────────────────────────────────────
#    The orange cylinder in the centre of the lab.
#    Drive Robby within ~0.6 m of it and her battery recharges automatically.
#    You won't need it in Chapter 0 — but remember where it is!
#
#    Position: (5.0, 3.0)
#    From Robby's start at (2, 2):  ~3.2 m ahead-right  (visible ahead)
create_object("Robby_Charger","cylinder","Orange", "fixed",
              (0.6, 0.9, 0),  (5.0, 3.0, 0),  (0, 0, 0))
