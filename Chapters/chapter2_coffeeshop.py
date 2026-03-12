# =============================================================================
#  Python Playbook — Chapter 2: Variables
#  World: The Coffee Shop  (10 m × 10 m)
# =============================================================================
#
#  LAYOUT  (origin = bottom-left)
#
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌────────────────────────────────────┐
# 9 │[══════════ COUNTER ═══════════════]│  ← white box (9.0, 0.5, 1.0) at (5.0, 9.5)
# 8 │  ☕ Cup1  ☕ Cup2  ☕ Cup3        │  ← 3 cyan cylinders on counter
#   │      ◉ CyanZone (5.0, 8.0)        │
# 7 │                                   │
# 6 │                                   │
# 5 │  ◎ Table_A          ◎ Table_B    │  ← yellow cylinders (radius 0.5)
#   │  ● GreenZone(2.0,5.0)             │
#   │                ● YellowZone(8,5)  │
# 4 │                                   │
# 3 │                                   │
# 2 │                                   │
# 1 │  ★ Robot (5.0, 1.0)              │
#   └────────────────────────────────────┘
#
#  STORY
#  Robby is on shift at the coffee shop. Three cups of coffee are waiting on
#  the counter for customers at Table A and Table B. Robby has no way of
#  remembering how many cups she is carrying — unless she uses a variable.
#
#  WORLD COORDINATES
#  ★  Robot start    : (5.0, 1.0)
#  ══  Counter       : (5.0, 9.5)  x spans 0.5 – 9.5  (white, fixed)
#  ☕  Cup_1         : (3.5, 9.0)  cyan cylinder on counter
#  ☕  Cup_2         : (5.0, 9.0)  cyan cylinder on counter
#  ☕  Cup_3         : (6.5, 9.0)  cyan cylinder on counter
#  ◎  Table_A       : (2.0, 5.0)  yellow cylinder, radius 0.5
#  ◎  Table_B       : (8.0, 5.0)  yellow cylinder, radius 0.5
#  ◉  CyanZone      : (5.0, 8.0)  radius 1.0 — triggers Mission 1
#  ●  GreenZone     : (2.0, 5.0)  radius 1.0 — triggers Mission 2
#  ●  YellowZone    : (8.0, 5.0)  radius 1.0 — triggers Mission 3
#
#  TIMING REFERENCE  (drive speed ≈ 2.88 m/s at drive(0.4, 0))
#  Robot → CyanZone (north, 7.0 m)  : sleep ≈ 2.2 s
#  CyanZone → GreenZone (south+west) : sleep ≈ 0.90 s south, 0.30 s turn, 1.1 s west
#  GreenZone → YellowZone (east)     : sleep ≈ 0.60 s turn, 2.1 s east
#  90° turn  at drive(0, 1.0)        : sleep ≈ 0.30 s
#  180° turn at drive(0, 1.0)        : sleep ≈ 0.60 s
# =============================================================================

# ── Robot start position ───────────────────────────────────────────────────────
set_robot_pos(5.0, 1.0)

# ── Counter ────────────────────────────────────────────────────────────────────
# size = (half-x, half-y, height) convention used by create_object
# White counter running across the top of the room
create_object("Counter", "box", "White", "fixed",
              (9.0, 0.5, 1.0), (5.0, 9.5, 0), (0, 0, 0))

# ── Cups on counter ────────────────────────────────────────────────────────────
# Three small cyan cylinders sitting on the counter surface
create_object("Cup_1", "cylinder", "Cyan", "fixed",
              (0.15, 0.25, 0), (3.5, 9.0, 0), (0, 0, 0))

create_object("Cup_2", "cylinder", "Cyan", "fixed",
              (0.15, 0.25, 0), (5.0, 9.0, 0), (0, 0, 0))

create_object("Cup_3", "cylinder", "Cyan", "fixed",
              (0.15, 0.25, 0), (6.5, 9.0, 0), (0, 0, 0))

# ── Tables ─────────────────────────────────────────────────────────────────────
# Table_A — west side of shop
create_object("Table_A", "cylinder", "Yellow", "fixed",
              (0.5, 0.8, 0), (2.0, 5.0, 0), (0, 0, 0))

# Table_B — east side of shop
create_object("Table_B", "cylinder", "Yellow", "fixed",
              (0.5, 0.8, 0), (8.0, 5.0, 0), (0, 0, 0))

# ── Drop zones ─────────────────────────────────────────────────────────────────
# CyanZone — in front of the counter; triggers Mission 1
create_zone("CyanZone",   5.0, 8.0, 1.0, (0.0, 1.0, 1.0))   # cyan

# GreenZone — at Table A; triggers Mission 2
create_zone("GreenZone",  2.0, 5.0, 1.0, (0.0, 1.0, 0.0))   # green

# YellowZone — at Table B; triggers Mission 3
create_zone("YellowZone", 8.0, 5.0, 1.0, (1.0, 1.0, 0.0))   # yellow
