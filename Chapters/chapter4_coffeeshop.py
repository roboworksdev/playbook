# =============================================================================
#  Python Playbook — Chapter 4: Functions
#  World: The Coffee Shop  (10 m × 10 m)
# =============================================================================
#
#  LAYOUT  (origin = bottom-left)
#
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌────────────────────────────────────┐
# 9 │[══════════ COUNTER ═══════════════]│  ← white box at y=9.5
# 8 │                  ◈ Plate_C(7.5,8) │  ← orange, moveable
#   │                        ◉ KitchenHatch(8.5,8.5)│  ← blue cylinder
# 7 │              ◈ Plate_B(5.5,7.0)   │  ← orange, moveable
#   │        [Table_2(5.0,7.5)]         │  ← yellow table
# 6 │  ◈ Plate_A(2.0,6.5)              │  ← orange, moveable → GreenZone
# 5 │                                   │
# 4 │                                   │
# 3 │        [Table_1(5.0,3.0)]         │  ← yellow table
# 2 │  ★ Robot (2.0, 2.0)              │
# 1 │                                   │
#   └────────────────────────────────────┘
#
#  STORY
#  -----
#  The afternoon rush is over. Dirty plates have been left on tables
#  across the coffee shop. Robby needs to collect them and return them
#  to the kitchen hatch in the north-east corner.
#
#  This chapter teaches you to write FUNCTIONS — named, reusable blocks
#  of code. Instead of repeating the same lines every time, you define
#  look(), pick_up(), and drop_off() once, then call them whenever you
#  need them.
#
#  WORLD COORDINATES
#  ★  Robot start     : (2.0, 2.0)  facing north
#  ══  Counter        : (5.0, 9.5)  x spans 0.5–9.5  (white, fixed)
#  ◈  Plate_A         : (2.0, 6.5)  orange moveable box — directly north of start
#  ◈  Plate_B         : (5.5, 7.0)  orange moveable box — centre of room
#  ◈  Plate_C         : (7.5, 8.0)  orange moveable box — near kitchen
#  ◉  KitchenHatch    : (8.5, 8.5)  blue fixed cylinder — kitchen drop-off
#  ●  GreenZone       : (2.0, 6.5)  radius 1.0 — triggers Mission 1
#  ●  BlueZone        : (8.5, 8.5)  radius 1.2 — triggers Mission 2 & 3
#
#  PATH NOTES  (safe driving routes used in starter scripts)
#  ---------------------------------------------------------
#  pick_up()  — drive north from (2.0, 2.0) straight to Plate_A
#               Plate_A south face at y = 6.1  →  distance(0) ≈ 4.1 m from start
#               while distance(0) > 0.5 → stops at y ≈ 5.6  (inside GreenZone) ✓
#
#  drop_off() — from (2.0, 5.6) turn right (east), drive east, turn left (north)
#               East leg  : 2.3 s at drive(0.4, 0)  →  x ≈ 8.6
#               North leg : 0.65 s at drive(0.4, 0) →  y ≈ 7.5  (inside BlueZone) ✓
#
#  TIMING REFERENCE  (drive speed ≈ 2.88 m/s at drive(0.4, 0))
#  90° turn  at drive(0,  1.0) : sleep ≈ 0.30 s (right)
#  90° turn  at drive(0, -1.0) : sleep ≈ 0.30 s (left)
#  Robot → Plate_A  (4.1 m north)        : while-loop driven
#  Plate_A → Kitchen (east then north)   : sleep 2.3 s + sleep 0.65 s
# =============================================================================

# ── Robot start position ───────────────────────────────────────────────────────
set_robot_pos(2.0, 2.0)

# ── Counter (north wall) ──────────────────────────────────────────────────────
create_object("Counter",      "box",      "White",  "fixed",
              (9.0, 0.5, 1.0),  (5.0, 9.5, 0),  (0, 0, 0))

# ── Kitchen hatch — drop-off point in north-east corner ───────────────────────
create_object("KitchenHatch", "cylinder", "Blue",   "fixed",
              (0.3, 1.2, 0),    (8.5, 8.5, 0),  (0, 0, 0))

# ── Dirty plates ──────────────────────────────────────────────────────────────
# Plate_A — directly north of Robby's start; the target for pick_up()
create_object("Plate_A",      "box",      "Orange", "moveable",
              (0.4, 0.4, 0.15), (2.0, 6.5, 0),  (0, 0, 0))

# Plate_B — centre of room; provides visual context and a second collection target
create_object("Plate_B",      "box",      "Orange", "moveable",
              (0.4, 0.4, 0.15), (5.5, 7.0, 0),  (0, 0, 0))

# Plate_C — near kitchen; a third plate closer to the drop-off point
create_object("Plate_C",      "box",      "Orange", "moveable",
              (0.4, 0.4, 0.15), (7.5, 8.0, 0),  (0, 0, 0))

# ── Customer tables (decorative — do not block navigation paths) ──────────────
# Table_1 — south area, well clear of all driving routes
create_object("Table_1",      "cylinder", "Yellow", "fixed",
              (0.5, 0.8, 0),    (5.0, 3.0, 0),  (0, 0, 0))

# Table_2 — north centre, between plates; offset north of drop_off() east path
create_object("Table_2",      "cylinder", "Yellow", "fixed",
              (0.5, 0.8, 0),    (5.0, 7.5, 0),  (0, 0, 0))

# ── Drop zones ─────────────────────────────────────────────────────────────────
# GreenZone — around Plate A; triggers Mission 1
create_zone("GreenZone", 2.0, 6.5, 1.0, (0.0, 1.0, 0.0))   # green

# BlueZone  — around kitchen hatch; triggers Mission 2 and Mission 3
create_zone("BlueZone",  8.5, 8.5, 1.2, (0.0, 0.5, 1.0))   # blue
