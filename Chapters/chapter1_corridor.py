# =============================================================================
#  THE Robby CHRONICLES — Chapter 1: "Learning to Walk"
#  World file for RoboSim5
# =============================================================================
#
#  STORY
#  -----
#  Robby's motor systems are unlocked. She can move — but she has never
#  walked before. Deep in the north of the facility, the Power Room holds
#  a charging station. Robby must reach it, learn to move precisely,
#  and prove she is ready for the missions ahead.
#
#  MISSIONS
#  --------
#  [1.1]  MANUAL DRIVE first  (use W / A / S / D keys).
#         Drive Robby north through the gateway and touch the charger.
#         Notice: how long does it take? How do you steer straight?
#
#         Now write a script to do the same thing automatically:
#
#             import time
#             drive(0.4, 0.0)   # forward at 40% speed
#             time.sleep(5.5)   # adjust this number until Robby reaches the charger
#             drive(0.0, 0.0)   # stop
#
#         Tip: battery_level() drops while moving. Watch the sidebar.
#
#  [1.2]  SQUARE PATH — use a for loop to drive a square:
#
#             import time
#             speed = 0.4       # ← Mission 1.3: change this value
#             for side in range(4):
#                 drive(speed, 0.0)   # drive one side
#                 time.sleep(1.5)     # adjust to get even sides
#                 drive(0.0, 1.0)     # turn right
#                 time.sleep(0.31)    # adjust to get 90° corners
#             drive(0.0, 0.0)
#
#         Does Robby return exactly to where she started?
#         What happens if you adjust time.sleep values slightly?
#
#  [1.3]  Change  speed = 0.4  to  speed = 0.2  and run Mission 1.2 again.
#         Change it to  speed = 0.8 — what is different?
#         KEY INSIGHT: changing one variable changes the whole behaviour.
#
#  KEY CONCEPTS IN THIS CHAPTER
#  ----------------------------
#    import time          →  load the time module (gives us sleep)
#    time.sleep(seconds)  →  pause for a number of seconds
#    drive(linear, angular)
#         linear  : -1.0 (full reverse) … +1.0 (full forward)
#         angular : -1.0 (full left)    … +1.0 (full right)
#    for x in range(4):   →  repeat the indented block 4 times
#    variable = value     →  store a value; change it in one place
#
#  EDUCATOR NOTES  →  See The Robby Chronicles — Teacher Guide, Ch.1
#
#  TIMING REFERENCE (approximate, may vary slightly by system speed)
#  ─────────────────────────────────────────────────────────────────
#    drive(0.4, 0.0)  ≈  2.88 m/s
#    Robby start (2, 2) → charger (2, 9.0): 7.0 m  → sleep ≈ 2.4 s
#    90° right turn at drive(0, 1.0)       → sleep ≈ 0.30 s
#    Square side at speed=0.4, sleep=1.5   ≈  4.3 m per side
#    For a ~2 m square: speed=0.4, sleep=0.7 s per side
# =============================================================================
#
#  WORLD LAYOUT  (10 m × 10 m, origin bottom-left)
#  ------------------------------------------------
#  Robby starts at (2.0, 2.0) facing North (+y direction).
#
#   W                              E
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌─────────────────────────────────┐
# 9 │     ⊕ Power Charger            │  ⊕ = Power_Charger (orange, y=9.0)
#   │  ◉         ◉  [Storage W2]    │  ◉ = Gateway pillars (yellow)
# 8 │                                │
#   │  [Storage W2]    ▲ ▲ ▲ Cones  │  ▲ = guide cones (at x=3.5)
# 7 │                                │  [Rack Ex] = east wall racks
#   │                  ▲             │
# 6 │                                │
#   │              [Monitor Stand]   │
# 5 │                  ▲             │  open square-path area:
#   │                                │  x=1–5, y=2–6 (completely clear)
# 4 │  [Storage W1]    [Rack E3]     │
#   │                                │
# 3 │                  [Rack E2]     │
#   │                                │
# 2 │  ★ Robby (2,2)   [Rack E1]     │  ★ = robot start
#   │                                │
# 1 │              [Supply Crate]    │
#   └─────────────────────────────────┘
#   0  1  2  3  4  5  6  7  8  9  10

# ── East wall equipment racks ─────────────────────────────────────────────────
#    Four tall racks lining the east wall — creates a corridor ambiance.
#    x-footprint: 9.45 → 9.95  (clear of Robby's path at x = 2)
create_object("Rack_E1",     "box",      "Blue",   "fixed",
              (0.5, 1.5, 2.0),  (9.7, 2.0, 0),  (0, 0, 0))

create_object("Rack_E2",     "box",      "Blue",   "fixed",
              (0.5, 1.5, 2.0),  (9.7, 4.5, 0),  (0, 0, 0))

create_object("Rack_E3",     "box",      "Blue",   "fixed",
              (0.5, 1.5, 2.0),  (9.7, 7.0, 0),  (0, 0, 0))

# ── West wall storage units ───────────────────────────────────────────────────
#    Storage blocks against the west wall.
#    x-footprint: 0.1 → 0.5  (clear of Robby's path at x = 2)
create_object("Storage_W1",  "box",      "Blue",   "fixed",
              (0.4, 1.4, 3.0),  (0.3, 3.5, 0),  (0, 0, 0))

create_object("Storage_W2",  "box",      "Blue",   "fixed",
              (0.4, 1.4, 2.5),  (0.3, 7.3, 0),  (0, 0, 0))

# ── Supply crate (south-east corner, decorative) ──────────────────────────────
#    A simple crate near the start area to give the south room visual weight.
create_object("Supply_Crate","box",      "White",  "fixed",
              (0.9, 0.7, 1.0),  (8.5, 0.6, 0),  (0, 0, 0))

# ── Monitor stand (mid-room landmark, east side) ──────────────────────────────
#    A raised display panel east of centre — gives depth to the open space
#    and provides a LiDAR reflection target for exploration.
create_object("Monitor_Stand","box",     "White",  "fixed",
              (0.8, 1.0, 0.5),  (7.5, 5.0, 0),  (0, 0, 0))

# ── North gateway — two tall yellow pillars ───────────────────────────────────
#    These frame the entrance to the Power Room where the charger lives.
#    The gap between them is 2.4 m wide  (x = 1.0 → 3.4)
#    Robby travels at x ≈ 2.0, so she passes cleanly through the centre.
#
#    Gate pillar clearance check:
#      Left pillar  at x=0.8, radius 0.175 m
#      Robby at x=2.0:  lateral gap = 2.0 - (0.8 + 0.175) = 1.025 m  ✓
#      Right pillar at x=3.2, radius 0.175 m
#      Robby at x=2.0:  lateral gap = (3.2 - 0.175) - 2.0 = 1.025 m  ✓
create_object("Gate_L",      "cylinder", "Yellow", "fixed",
              (0.35, 1.8, 0),  (0.8, 7.8, 0),  (0, 0, 0))

create_object("Gate_R",      "cylinder", "Yellow", "fixed",
              (0.35, 1.8, 0),  (3.2, 7.8, 0),  (0, 0, 0))

# ── Orange guide cones (visual path markers) ──────────────────────────────────
#    Three cones to the right of Robby's north path (x=3.5).
#    They are visual guides only — Robby travels at x=2, so they don't block her.
#    Tip for educators: point these out before Mission 1.1 manual drive.
create_object("Cone_1",      "cylinder", "Orange", "fixed",
              (0.2, 0.55, 0),  (3.5, 3.0, 0),  (0, 0, 0))

create_object("Cone_2",      "cylinder", "Orange", "fixed",
              (0.2, 0.55, 0),  (3.5, 5.0, 0),  (0, 0, 0))

create_object("Cone_3",      "cylinder", "Orange", "fixed",
              (0.2, 0.55, 0),  (3.5, 6.8, 0),  (0, 0, 0))

# ── Power Room Charging Station ───────────────────────────────────────────────
#    Robby's destination.  Located at the far north end, centred on her
#    start x-position (x=2.0) so a straight drive() command reaches it.
#
#    Charging physics:
#      Robot stops at surface: y ≈ 9.0 - 0.4 (radius) - 0.25 (robot) = 8.35 m
#      Charge triggers when dist-to-surface < 0.6 m  →  triggers at y > 8.0 m
#
#    At drive(0.4, 0.0)  speed ≈ 2.88 m/s:
#      Distance from (2,2) to y=8.35  →  6.35 m  →  ~2.2 s
#      Use time.sleep(2.4) to be safe, then refine.
create_object("Power_Charger","cylinder","Orange", "fixed",
              (0.8, 1.0, 0),  (2.0, 9.0, 0),  (0, 0, 0))
