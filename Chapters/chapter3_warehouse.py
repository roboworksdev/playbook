# =============================================================================
#  THE Robby CHRONICLES — Chapter 3: "The Retrieval Mission"
#  World file for RoboSim5
# =============================================================================
#
#  STORY
#  -----
#  A tremor shook the facility last night. Supply crates were scattered across
#  the warehouse floor. The team needs them returned to the drop zone before
#  the morning inspection. Robby has been assigned the task — four crates,
#  one robot, no time to waste.
#
#  MISSIONS
#  --------
#  [3.1]  APPROACH AND ATTACH — drive to Crate_1 and pick it up:
#
#             import time
#             # Navigate to Crate_1 (east then north)
#             drive(0.0, 1.0);  time.sleep(0.30)   # face east
#             drive(0.4, 0.0);  time.sleep(0.52)   # go east 1.5 m
#             drive(0.0,-1.0);  time.sleep(0.30)   # face north
#             while not close_enough():
#                 drive(0.2, 0.0)
#             drive(0.0, 0.0)
#             attach()
#             print(f"holding()={holding()}")
#
#  [3.2]  DELIVER AND RELEASE — take the crate to the blue drop zone:
#
#             import time
#             drive(0.0, 1.0);  time.sleep(0.30)   # face east
#             drive(0.4, 0.0);  time.sleep(1.39)   # go east ~4 m
#             drive(0.0,-1.0);  time.sleep(0.30)   # face north
#             drive(0.4, 0.0);  time.sleep(1.35)   # go north ~4 m
#             drive(0.0, 0.0)
#             detach()
#             print(f"holding()={holding()} — crate released!")
#
#  [3.3]  DEFINE THE SKILL — wrap the grab-and-deliver into a function:
#
#             def collect_crate(cx, cy):
#                 """Navigate to crate at (cx,cy), grab it, deliver to zone."""
#                 # ... navigation code here ...
#                 while not close_enough():
#                     drive(0.2, 0.0)
#                 drive(0.0, 0.0)
#                 attach()
#                 # ... drive to drop zone ...
#                 detach()
#
#  [3.4]  CALL IT — once defined, the skill is available forever:
#
#             collect_crate(3.5, 4.0)   # Crate 1
#             collect_crate(7.0, 4.0)   # Crate 2
#             # ... etc.
#
#  KEY CONCEPTS IN THIS CHAPTER
#  ----------------------------
#    while not close_enough():  →  approach until within reach of object
#    attach()                   →  magnetically couple to nearest object
#    detach()                   →  release currently held object
#    holding()                  →  True if Robby is carrying something
#    close_enough()             →  True if a moveable object is ≤ 0.65 m away
#    def name():                →  define a reusable function
#    return                     →  (preview) functions can hand back a value
#
#  TEACHING NOTE
#  -------------
#    Introduce functions using the 'new skill' metaphor:
#    "Once you teach Robby this skill, she knows it forever. The def block is
#    the teaching moment. The call is using the skill."
#    Give learners the working sequential code FIRST, then ask:
#    "What would you change if you had to do this 4 times?"
#
#  EDUCATOR NOTES  →  See The Robby Chronicles — Teacher Guide, Ch.3
# =============================================================================
#
#  WORLD LAYOUT  (10 m × 10 m, origin bottom-left)
#  ------------------------------------------------
#  Robby starts at (2.0, 2.0) facing North (+y direction).
#
#   W                              E
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌─────────────────────────────────┐
# 9 │                                 │
#   │  ⊕Bay       [■4]  □NW    □NE   │  ⊕ = Bay_Charger (1.5, 8.5)
# 8 │  Charger                        │  □ = blue drop zone corner markers
#   │  [■3]            [Rack E2]      │  ■ = orange moveable crate
# 7 │             Drop Zone (7.5,7.0) │
#   │             □SW         □SE    │
# 6 │                                 │
#   │         [Debris]      [Rack E1] │
# 5 │                                 │
#   │  [■1]              [■2]         │
# 4 │                                 │
#   │                                 │
# 3 │                                 │
#   │                                 │
# 2 │  ★ Robby (2,2)                   │  ★ = robot start
#   │                                 │
# 1 │                                 │
#   └─────────────────────────────────┘
#   0  1  2  3  4  5  6  7  8  9  10
#
#  Drop zone: 2 m × 2 m square centred at (7.5, 7.0)
#  Four blue cylinder markers at the corners (not walls — Robby drives inside).
#  Crate sizes: 0.6 m × 0.55 m × 0.6 m (orange, moveable)
#  close_enough() triggers when dist-to-surface < 0.65 m
# =============================================================================

# ── East wall equipment racks (decorative context) ───────────────────────────
create_object("Rack_E1",    "box",      "Blue",   "fixed",
              (0.5, 1.5, 2.0),  (9.7, 4.0, 0),  (0, 0, 0))

create_object("Rack_E2",    "box",      "Blue",   "fixed",
              (0.5, 1.5, 2.0),  (9.7, 7.5, 0),  (0, 0, 0))

# ── Central debris (fixed obstacle Robby must navigate around) ─────────────────
#    x-footprint: 4.65 → 5.35,  y-footprint: 4.75 → 5.25
create_object("Debris_1",   "box",      "White",  "fixed",
              (0.7, 0.8, 0.5),  (5.0, 5.0, 0),  (0, 0, 0))

# ── Drop zone corner markers (blue flat cylinders) ────────────────────────────
#    These mark the 2 m × 2 m drop zone centred at (7.5, 7.0).
#    Corners are at ±1.0 m in x and y from centre.
#    Robby drives BETWEEN the markers — they do not block entry.
#    Detach the crate anywhere inside the square for a successful delivery.
create_object("Zone_SW",    "cylinder", "Blue",   "fixed",
              (0.2, 0.08, 0),  (6.5, 6.0, 0),  (0, 0, 0))

create_object("Zone_SE",    "cylinder", "Blue",   "fixed",
              (0.2, 0.08, 0),  (8.5, 6.0, 0),  (0, 0, 0))

create_object("Zone_NW",    "cylinder", "Blue",   "fixed",
              (0.2, 0.08, 0),  (6.5, 8.0, 0),  (0, 0, 0))

create_object("Zone_NE",    "cylinder", "Blue",   "fixed",
              (0.2, 0.08, 0),  (8.5, 8.0, 0),  (0, 0, 0))

# ── Orange supply crates (moveable) ──────────────────────────────────────────
#    All four crates are physics="moveable" — Robby can attach() and carry them.
#    Each crate: 0.6 m wide × 0.55 m tall × 0.6 m deep
#    close_enough() triggers when Robby centre is within ~0.95 m of crate centre
#    (dist-to-surface < 0.65: surface = crate-centre ± 0.3 m)

#    Crate_1 — NE of start, nearest and most accessible
#    Robby approach: face east → drive 1.5 m → face north → while not close_enough()
create_object("Crate_1",    "box",      "Orange", "moveable",
              (0.6, 0.55, 0.6),  (3.5, 4.0, 0),  (0, 0, 0))

#    Crate_2 — east side
create_object("Crate_2",    "box",      "Orange", "moveable",
              (0.6, 0.55, 0.6),  (7.0, 4.0, 0),  (0, 0, 0))

#    Crate_3 — north-west, near the charging station
create_object("Crate_3",    "box",      "Orange", "moveable",
              (0.6, 0.55, 0.6),  (1.5, 6.5, 0),  (0, 0, 0))

#    Crate_4 — north-centre, just west of the drop zone
create_object("Crate_4",    "box",      "Orange", "moveable",
              (0.6, 0.55, 0.6),  (4.5, 7.5, 0),  (0, 0, 0))

# ── Bay Charging Station ──────────────────────────────────────────────────────
#    Located in the NW corner — useful during long collection missions.
#    Drive Robby within ~0.9 m of centre to trigger charging.
#
#    STORY NOTE: Robby should check her battery before collecting all four crates.
#    This foreshadows Chapter 4: energy-aware planning.
create_object("Bay_Charger","cylinder", "Orange", "fixed",
              (0.6, 0.9, 0),  (1.5, 8.5, 0),  (0, 0, 0))
