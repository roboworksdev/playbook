# =============================================================================
#  Python Playbook — Chapter 1: Conditional Statements
#  World: The Cafe Kitchen  (10 m × 10 m)
# =============================================================================
#
#  LAYOUT  (origin = bottom-left)
#
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌────────────────────────────────────┐
# 9 │                                   │
# 8 │                                   │
# 7 │                                   │
# 6 │                                   │
# 5 │[L]  ════════ WALL ════════  [R]   │
# 4 │                                   │
# 3 │                                   │
# 2 │             ★ Robot (5,2)         │
# 1 │                                   │
#   └────────────────────────────────────┘
#
#  ★  Robot start     : (5.0, 2.0)  centred, 3 units from the wall
#  ══  KitchenWall    : (5.0, 5.0)  x spans 1.5 – 8.5  (white, fixed)
#  [L] LeftDoorZone   : (0.75, 5.0)  left door opening
#  [R] RightDoorZone  : (9.25, 5.0)  right door opening
#
#  The wall runs from x = 1.5 to x = 8.5, leaving door gaps at each end.
#  Robby starts centred at the bottom, travels north, and must use distance()
#  to stop before hitting the wall, then turn and pass through a door.
# =============================================================================

# ── Robot start position ───────────────────────────────────────────────────────
# Centred at x = 5, same distance (3 units) from the wall as the default (2,2)
set_robot_pos(5.0, 2.0)

# ── Wall ───────────────────────────────────────────────────────────────────────
# size = (w, h, d): w = x-extent (7.0), h = height (0.6), d = y-depth (0.3)
# Centered at (5, 5) → spans x: 1.5–8.5, y: 4.85–5.15
create_object("KitchenWall", "box", "White", "fixed",
              (7.0, 0.6, 0.3), (5.0, 5.0, 0), (0, 0, 0))

# ── Drop zones ─────────────────────────────────────────────────────────────────
# WallApproachZone — in front of the wall; triggers Mission 1
create_zone("WallApproachZone", 5.0, 4.2, 1.0, (1.0, 1.0, 0.0))   # yellow

# LeftDoorZone — the left door opening (x gap: 0 – 1.5); triggers Mission 2
create_zone("LeftDoorZone",     0.75, 5.0, 1.0, (0.0, 0.8, 1.0))  # blue

# RightDoorZone — the right door opening (x gap: 8.5 – 10); triggers Mission 3
create_zone("RightDoorZone",    9.25, 5.0, 1.0, (0.0, 1.0, 0.4))  # green
