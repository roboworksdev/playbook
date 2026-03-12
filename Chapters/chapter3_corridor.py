# =============================================================================
#  Python Playbook — Chapter 3: Loops
#  World: The Storage Corridor  (10 m × 10 m)
# =============================================================================
#
#  LAYOUT  (origin = bottom-left)
#
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌────────────────────────────────────┐
# 9 │                                   │
#   │[══════════ NORTH WALL ════════════]│  ← white box at y=8.5, size (10.0, 0.5, 2.0)
# 8 │    ◉ BlueZone (5.0, 7.7)         │
# 7 │                                   │
# 6 │                                   │
# 5 │         ★ Robot (5.0, 5.0)       │
# 4 │                                   │
# 3 │    ◉ OrangeZone (5.0, 2.3)       │
#   │[══════════ SOUTH WALL ════════════]│  ← white box at y=1.5, size (10.0, 0.5, 2.0)
# 2 │                                   │
# 1 │                                   │
#   └────────────────────────────────────┘
#
#  STORY
#  Robby has been assigned to patrol a long storage corridor. Two thick white
#  walls seal the north and south ends. There are no manual controls this
#  time — Robby must navigate using code alone. The challenge is that she
#  does not know in advance how many steps to take before hitting a wall.
#  Instead of counting steps, she needs to keep sensing the distance ahead
#  and react when the reading drops too low.
#
#  WORLD COORDINATES
#  ★  Robot start      : (5.0, 5.0)  centred in the corridor
#  ══  NorthWall       : (5.0, 8.5)  y spans 8.25–8.75  (white, fixed)
#      Surface (inner) : y = 8.25
#  ══  SouthWall       : (5.0, 1.5)  y spans 1.25–1.75  (white, fixed)
#      Surface (inner) : y = 1.75
#  ◉  BlueZone         : (5.0, 7.7)  radius 1.0 — triggers Mission 1 & 3
#  ◉  OrangeZone       : (5.0, 2.3)  radius 1.0 — triggers Mission 2
#  ◆  Cone_1 (marker)  : (5.0, 3.5)  small orange cylinder
#  ◆  Cone_2 (marker)  : (5.0, 5.0)  small orange cylinder
#  ◆  Cone_3 (marker)  : (5.0, 6.5)  small orange cylinder
#
#  LIDAR NOTES
#  Robot starts at y = 5.0, heading north (0°).
#  distance(0)   from (5.0, 5.0) to NorthWall surface (y=8.25) = 3.25 m
#  distance(180) from (5.0, 5.0) to SouthWall surface (y=1.75) = 3.25 m
#
#  With SAFE = 1.0:
#    Heading north — Robby stops at y ≈ 7.25  (inside BlueZone at y=7.7)
#    Heading south — Robby stops at y ≈ 2.75  (inside OrangeZone at y=2.3)
#
#  TIMING REFERENCE  (drive speed ≈ 2.88 m/s at drive(0.4, 0))
#  (5.0, 5.0) → BlueZone   (north, ~2.25 m) : sleep ≈ 0.78 s (loop-driven)
#  (5.0, 5.0) → OrangeZone (south, ~2.25 m) : sleep ≈ 0.78 s (loop-driven)
#  180° turn at drive(0, 1.0)               : sleep ≈ 0.60 s
#  Short sensor-read pause                  : sleep ≈ 0.05 s per loop tick
# =============================================================================

# ── Robot start position ───────────────────────────────────────────────────────
set_robot_pos(5.0, 5.0)

# ── Walls ──────────────────────────────────────────────────────────────────────
# NorthWall — seals the top of the corridor
# size = (half-x, half-y, height): x-full = 10.0, y-depth = 0.5, height = 2.0
create_object("NorthWall", "box", "White", "fixed",
              (10.0, 0.5, 2.0), (5.0, 8.5, 0), (0, 0, 0))

# SouthWall — seals the bottom of the corridor
create_object("SouthWall", "box", "White", "fixed",
              (10.0, 0.5, 2.0), (5.0, 1.5, 0), (0, 0, 0))

# ── Visual markers (orange cones) ──────────────────────────────────────────────
# Small orange cylinders along the centre line to help visualise Robby's path
create_object("Cone_1", "cylinder", "Orange", "fixed",
              (0.1, 0.2, 0), (5.0, 3.5, 0), (0, 0, 0))

create_object("Cone_2", "cylinder", "Orange", "fixed",
              (0.1, 0.2, 0), (5.0, 5.0, 0), (0, 0, 0))

create_object("Cone_3", "cylinder", "Orange", "fixed",
              (0.1, 0.2, 0), (5.0, 6.5, 0), (0, 0, 0))

# ── Drop zones ─────────────────────────────────────────────────────────────────
# BlueZone — near the north wall; triggers Mission 1 and Mission 3
create_zone("BlueZone",   5.0, 7.7, 1.0, (0.0, 0.5, 1.0))   # blue

# OrangeZone — near the south wall; triggers Mission 2
create_zone("OrangeZone", 5.0, 2.3, 1.0, (1.0, 0.5, 0.0))   # orange
