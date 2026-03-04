# =============================================================================
#  THE Robby CHRONICLES — Chapter 2: "Eyes Wide Open"
#  World file for RoboSim5
# =============================================================================
#
#  STORY
#  -----
#  Robby enters the facility's old storage wing. The lights are on low power —
#  the room is dim and cluttered with abandoned equipment. Her motors work,
#  but without sensors she is blind. You must teach Robby to feel the space
#  around her and navigate without collision.
#
#  MISSIONS
#  --------
#  [2.1]  READ THE SENSOR — find out what's directly ahead:
#
#             print(f"Distance ahead: {distance(0)} m")
#             print(f"Distance right: {distance(90)} m")
#             print(f"Distance left:  {distance(270)} m")
#
#         What is blocking Robby at angle 0?
#         Tip: distance(angle) reads the LiDAR sensor. Angle 0 = forward,
#              then clockwise: 90 = right, 180 = behind, 270 = left.
#
#  [2.2]  STOP BEFORE THE WALL — drive north, but stop 0.8 m before any
#         obstacle:
#
#             import time
#             while distance(0) > 0.8:
#                 drive(0.4, 0.0)
#             drive(0.0, 0.0)
#             print(f"Stopped. Gap ahead: {distance(0):.2f} m")
#
#         Notice: Robby brakes exactly at the threshold — every time.
#         Change 0.8 to 1.5.  Change it to 0.3.  What is the limit?
#
#  [2.3]  OBSTACLE AVOIDANCE — reach Sensor_Charger in the NE corner
#         without touching anything:
#
#             import time
#             SAFE = 0.9     # metres — turn when closer than this
#             while True:
#                 if distance(0) < SAFE:
#                     drive(0.0, 1.0)    # spin right until clear
#                     time.sleep(0.12)
#                 else:
#                     drive(0.4, 0.15)   # forward, slight right drift
#                     time.sleep(0.08)
#
#         SENSE → DECIDE → ACT: this three-step loop is the foundation of
#         all reactive robotics. The orange Sensor_Charger is in the NE corner.
#         Tip: add  print(f"gap={distance(0):.1f}")  inside the loop to see
#              what Robby senses at each step.
#
#  KEY CONCEPTS IN THIS CHAPTER
#  ----------------------------
#    distance(angle)      →  LiDAR reading in metres at given angle
#    if / elif / else     →  conditional execution
#    Boolean expressions  →  True / False, comparison operators (<, >, ==)
#    while True:          →  infinite loop (Ctrl-C or Stop button to exit)
#    break                →  exit a loop immediately
#
#  COMMON MISCONCEPTION
#  --------------------
#    if distance = 0.9    ← assignment (WRONG: this sets a variable)
#    if distance(0) < 0.9 ← comparison (CORRECT: this tests a condition)
#    Robby will display an error if you mix these up — that error IS the lesson.
#
#  EDUCATOR NOTES  →  See The Robby Chronicles — Teacher Guide, Ch.2
# =============================================================================
#
#  WORLD LAYOUT  (10 m × 10 m, origin bottom-left)
#  ------------------------------------------------
#  Robby starts at (2.0, 2.0) facing North (+y direction).
#
#   W                              E
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌─────────────────────────────────┐
# 9 │[=====Shelf_N=======]       ⊕   │  ⊕ = Sensor_Charger (8.5, 8.8)
#   │    [D]          [E]            │
# 8 │                                │
#   │                                │
# 7 │  ● G            ●F    [C]      │  ● = drums (blue cylinders)
#   │  |                             │  | = Shelf_W (west wall)
# 6 │  |                             │
#   │  |                             │
# 5 │  |  ■ Pillar_A   ■ Pillar_B   │  ■ = red structural pillars
#   │  |                             │
# 4 │                                │
#   │                                │
# 3 │                                │  Clear area for square-path practice
#   │                                │
# 2 │  ★ Robby (2,2)                  │  ★ = robot start
#   │                                │
# 1 │                                │
#   └─────────────────────────────────┘
#   0  1  2  3  4  5  6  7  8  9  10
#
#  LiDAR note:
#    From start (2,2) facing north, Pillar_A is at distance ≈ 2.8 m  (angle 0)
#    Pillar_B is visible at distance ≈ 3.6 m slightly right           (angle ~35)
#    West wall is at distance ≈ 1.75 m                                (angle 270)
# =============================================================================

# ── West wall shelf (dark, floor-to-ceiling) ──────────────────────────────────
#    x-footprint: 0.025 → 0.275  (flush against west wall)
#    y-footprint: 3.75 → 7.25   (mid-room, not blocking start or north path)
create_object("Shelf_W",    "box",      "Black",  "fixed",
              (0.25, 1.4, 3.5),  (0.15, 5.5, 0),  (0, 0, 0))

# ── North wall shelf (dark) ───────────────────────────────────────────────────
#    Spans x = 2.0 → 7.0 along the north wall — creates a visual back wall
#    Leaves x = 7 → 10 open: Robby's route to the NE charger
create_object("Shelf_N",    "box",      "Black",  "fixed",
              (5.0, 1.3, 0.2),  (4.5, 9.9, 0),  (0, 0, 0))

# ── Structural pillars (red) ─────────────────────────────────────────────────
#    Pillar_A — directly north of Robby.
#    From start (2, 2): distance(0) ≈ 2.8 m.  Mission 2.1 landmark.
#    x-footprint: 1.775 → 2.225  (centred on Robby's start x)
create_object("Pillar_A",   "cylinder", "Red",    "fixed",
              (0.45, 1.6, 0),  (2.0, 5.0, 0),  (0, 0, 0))

#    Pillar_B — to the east, same latitude as Pillar_A.
#    Gap between A and B: 5.5 - 0.225 - 2.0 - 0.225 = 3.05 m  ✓ (passable)
create_object("Pillar_B",   "cylinder", "Red",    "fixed",
              (0.45, 1.6, 0),  (5.5, 5.0, 0),  (0, 0, 0))

# ── Storage boxes (white) ─────────────────────────────────────────────────────
#    Box_C — east side, beyond Pillar_B, blocks the east wall route
#    x-footprint: 7.05 → 7.95,  y-footprint: 5.05 → 5.95
create_object("Box_C",      "box",      "White",  "fixed",
              (0.9, 1.0, 0.9),  (7.5, 5.5, 0),  (0, 0, 0))

#    Box_D — north area, left of centre
#    x-footprint: 3.05 → 3.95,  y-footprint: 7.55 → 8.45
create_object("Box_D",      "box",      "White",  "fixed",
              (0.9, 1.0, 0.9),  (3.5, 8.0, 0),  (0, 0, 0))

#    Box_E — north-centre-east, creates a chicane with Box_D
#    x-footprint: 5.65 → 6.35,  y-footprint: 6.65 → 7.35
create_object("Box_E",      "box",      "White",  "fixed",
              (0.7, 0.8, 0.7),  (6.0, 7.0, 0),  (0, 0, 0))

# ── Drums (blue cylinders) ────────────────────────────────────────────────────
#    Drum_F — mid-room, north of Pillar_A/B, creates a centre-lane obstacle
#    gap to Pillar_A east: 4.0 - 0.2 - (2.0 + 0.225) = 1.575 m  ✓
#    gap to Pillar_B west: (5.5 - 0.225) - (4.0 + 0.2) = 1.075 m ✓
create_object("Drum_F",     "cylinder", "Blue",   "fixed",
              (0.4, 0.9, 0),  (4.0, 6.5, 0),  (0, 0, 0))

#    Drum_G — north-west, beside the west shelf
#    x-footprint: 1.3 → 1.7,  y-footprint: 7.3 → 7.7
create_object("Drum_G",     "cylinder", "Blue",   "fixed",
              (0.4, 0.9, 0),  (1.5, 7.5, 0),  (0, 0, 0))

# ── Sensor Charging Station ───────────────────────────────────────────────────
#    Robby's destination for Mission 2.3.
#    Placed in the NE corner — Robby must navigate the clutter to reach it.
#
#    Charge triggers at: dist-to-surface < 0.6 m
#      dist-to-surface = dist-to-centre - radius = dist-to-centre - 0.3
#      → triggers when Robby centre is within 0.9 m of (8.5, 8.8)
#
#    Clear approach corridor: east of Box_E (x > 6.35), north of Box_C (y > 5.95)
create_object("Sensor_Charger", "cylinder", "Orange", "fixed",
              (0.6, 0.9, 0),  (8.5, 8.8, 0),  (0, 0, 0))
