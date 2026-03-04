# =============================================================================
#  Python Playbook — Chapter 1: Python Basics
#  World: The Coffee Shop  (10 m × 10 m)
# =============================================================================
#
#  LAYOUT  (origin = bottom-left)
#
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌────────────────────────────────────┐
# 9 │                    [KitchenHatch] │
# 8 │  ☕ CoffeeCup(2,8)               │
# 7 │                                   │
# 6 │        [T1]  ⬛ DirtyPlate(4,6)  │
# 5 │                                   │
# 4 │                    [T2]           │
# 3 │                                   │
# 2 │  ★ Robot (2,2)                   │
# 1 │                                   │
#   └────────────────────────────────────┘
#
#  ★  Robot start   : (2.0, 2.0)
#  ☕  CoffeeCup    : (2.0, 8.0)  moveable sphere  (green)
#  ⬛  DirtyPlate   : (4.0, 6.0)  moveable box     (orange)
#  [KH] KitchenHatch: (9.0, 8.5)  fixed cylinder   (blue)
# =============================================================================

# ── Mission objects ────────────────────────────────────────────────────────────
# CoffeeCup — robot picks this up from the counter and delivers to customer
create_object("CoffeeCup",    "sphere",   "Green",  "moveable",
              (0.3, 0, 0),      (2.0, 8.0, 0),  (0, 0, 0))

# DirtyPlate — dirty dish left by customer that Robby must return to kitchen
create_object("DirtyPlate",   "box",      "Orange", "moveable",
              (0.4, 0.4, 0.15), (4.0, 6.0, 0),  (0, 0, 0))

# KitchenHatch — the kitchen return point (fixed)
create_object("KitchenHatch", "cylinder", "Blue",   "fixed",
              (0.3, 1.2, 0),    (9.0, 8.5, 0),  (0, 0, 0))

# ── Drop zones ─────────────────────────────────────────────────────────────────
create_zone("PickupZone",  2.0, 8.0, 1.1, (0.0, 1.0,  0.0))   # green — coffee counter
create_zone("Table1Zone",  4.0, 6.0, 1.2, (1.0, 0.55, 0.0))   # orange — customer table
create_zone("KitchenZone", 9.0, 8.5, 1.3, (0.0, 0.5,  1.0))   # blue — kitchen hatch
