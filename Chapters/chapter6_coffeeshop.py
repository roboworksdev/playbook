# =============================================================================
#  Python Playbook — Chapter 6: Algorithms
#  World: The Coffee Shop  (10 m × 10 m)
# =============================================================================
#
#  LAYOUT  (origin = bottom-left)
#
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌────────────────────────────────────┐
# 9 │[══════════ COUNTER ═══════════════]│  ← white box at y=9.5
# 8 │      ◉ CyanZone (5.0, 8.0)       │  ← triggers Mission 1
# 7 │                                   │
# 6 │                                   │
# 5 │  ◎ Table_A          ◎ Table_B    │  ← yellow cylinders
#   │  ☕☕◈◈             ☕☕☕◈◈◈  │  ← used cups & plates near tables
#   │  ● GreenZone(2.0,5.0)             │  ← triggers Mission 2
#   │                ● YellowZone(8,5)  │  ← triggers Mission 3
# 4 │                                   │
# 3 │      ◎ Table_C (5.0, 3.5)        │  ← yellow cylinder
#   │      ☕◈                          │  ← one cup & plate
# 2 │                                   │
# 1 │  ★ Robot (5.0, 1.0)              │
#   └────────────────────────────────────┘
#
#  STORY
#  -----
#  It is closing time. Three tables have been cleared and the used cups
#  and dishes are still sitting out. Robby needs to count everything up:
#  how many coffees were served, how many dishes need washing, and what
#  the totals look like across all three tables.
#
#  WORLD COORDINATES
#  ★  Robot start  : (5.0, 1.0)
#  ══  Counter     : (5.0, 9.5)  x spans 0.5–9.5  (white, fixed)
#  ◎   Table_A     : (2.0, 5.0)  yellow cylinder — 2 customers
#  ◎   Table_B     : (8.0, 5.0)  yellow cylinder — 3 customers
#  ◎   Table_C     : (5.0, 3.5)  yellow cylinder — 1 customer
#  ☕  Used cups at Table_A : (1.5, 5.4) and (2.5, 5.4)  cyan cylinders
#  ◈   Used plates at Table_A : (1.7, 4.6) and (2.3, 4.6)  orange boxes
#  ☕  Used cups at Table_B : (7.4, 5.4), (8.0, 5.4), (8.6, 5.4)  cyan
#  ◈   Used plates at Table_B : (7.6, 4.6), (8.0, 4.6), (8.4, 4.6)  orange
#  ☕  Used cup  at Table_C : (4.6, 3.7)  cyan cylinder
#  ◈   Used plate at Table_C : (5.4, 3.3)  orange box
#  ◉   CyanZone    : (5.0, 8.0)  radius 1.0 — triggers Mission 1
#  ●   GreenZone   : (2.0, 5.0)  radius 1.0 — triggers Mission 2
#  ●   YellowZone  : (8.0, 5.0)  radius 1.0 — triggers Mission 3
#
#  PATH NOTES  (safe driving routes used in starter scripts)
#  ---------------------------------------------------------
#  Mission 1 — drive north from (5.0, 1.0) to CyanZone (5.0, 8.0)
#               7.0 m at drive(0.4, 0) ≈ sleep 2.2 s
#
#  Mission 2 — from CyanZone: 180° south, drive south, right turn west
#               180° turn : drive(0,1.0) sleep 0.60 s
#               South leg : drive(0.4,0) sleep 0.90 s  → y ≈ 5.0
#               Right turn: drive(0,1.0) sleep 0.30 s  (south → west)
#               West leg  : drive(0.4,0) sleep 1.1 s   → x ≈ 2.0  (GreenZone) ✓
#
#  Mission 3 — from GreenZone: 180° east turn, drive east
#               180° turn : drive(0,1.0) sleep 0.60 s  (west → east)
#               East leg  : drive(0.4,0) sleep 2.1 s   → x ≈ 8.0  (YellowZone) ✓
#
#  TIMING REFERENCE  (drive speed ≈ 2.88 m/s at drive(0.4, 0))
#  90° turn  at drive(0,  1.0) : sleep ≈ 0.30 s
#  180° turn at drive(0,  1.0) : sleep ≈ 0.60 s
#  Robot → CyanZone  (7.0 m north)       : sleep ≈ 2.2 s
#  CyanZone → GreenZone (south then west): sleep ≈ 0.90 s + 1.1 s
#  GreenZone → YellowZone (east)         : sleep ≈ 2.1 s
# =============================================================================

# ── Robot start position ───────────────────────────────────────────────────────
set_robot_pos(5.0, 1.0)

# ── Counter (north wall) ──────────────────────────────────────────────────────
create_object("Counter", "box", "White", "fixed",
              (9.0, 0.5, 1.0), (5.0, 9.5, 0), (0, 0, 0))

# ── Tables ─────────────────────────────────────────────────────────────────────
# Table_A — west side, 2 customers
create_object("Table_A", "cylinder", "Yellow", "fixed",
              (0.5, 0.8, 0), (2.0, 5.0, 0), (0, 0, 0))

# Table_B — east side, 3 customers
create_object("Table_B", "cylinder", "Yellow", "fixed",
              (0.5, 0.8, 0), (8.0, 5.0, 0), (0, 0, 0))

# Table_C — south centre, 1 customer
create_object("Table_C", "cylinder", "Yellow", "fixed",
              (0.5, 0.8, 0), (5.0, 3.5, 0), (0, 0, 0))

# ── Used cups at Table_A (2 customers) ────────────────────────────────────────
create_object("Cup_A1", "cylinder", "Cyan", "fixed",
              (0.12, 0.20, 0), (1.5, 5.4, 0), (0, 0, 0))

create_object("Cup_A2", "cylinder", "Cyan", "fixed",
              (0.12, 0.20, 0), (2.5, 5.4, 0), (0, 0, 0))

# ── Used plates at Table_A ────────────────────────────────────────────────────
create_object("Plate_A1", "box", "Orange", "fixed",
              (0.25, 0.25, 0.04), (1.7, 4.6, 0), (0, 0, 0))

create_object("Plate_A2", "box", "Orange", "fixed",
              (0.25, 0.25, 0.04), (2.3, 4.6, 0), (0, 0, 0))

# ── Used cups at Table_B (3 customers) ────────────────────────────────────────
create_object("Cup_B1", "cylinder", "Cyan", "fixed",
              (0.12, 0.20, 0), (7.4, 5.4, 0), (0, 0, 0))

create_object("Cup_B2", "cylinder", "Cyan", "fixed",
              (0.12, 0.20, 0), (8.0, 5.4, 0), (0, 0, 0))

create_object("Cup_B3", "cylinder", "Cyan", "fixed",
              (0.12, 0.20, 0), (8.6, 5.4, 0), (0, 0, 0))

# ── Used plates at Table_B ────────────────────────────────────────────────────
create_object("Plate_B1", "box", "Orange", "fixed",
              (0.25, 0.25, 0.04), (7.6, 4.6, 0), (0, 0, 0))

create_object("Plate_B2", "box", "Orange", "fixed",
              (0.25, 0.25, 0.04), (8.0, 4.6, 0), (0, 0, 0))

create_object("Plate_B3", "box", "Orange", "fixed",
              (0.25, 0.25, 0.04), (8.4, 4.6, 0), (0, 0, 0))

# ── Used cup and plate at Table_C (1 customer) ────────────────────────────────
create_object("Cup_C1", "cylinder", "Cyan", "fixed",
              (0.12, 0.20, 0), (4.6, 3.7, 0), (0, 0, 0))

create_object("Plate_C1", "box", "Orange", "fixed",
              (0.25, 0.25, 0.04), (5.4, 3.3, 0), (0, 0, 0))

# ── Drop zones ─────────────────────────────────────────────────────────────────
# CyanZone — in front of the counter; triggers Mission 1
create_zone("CyanZone",   5.0, 8.0, 1.0, (0.0, 1.0, 1.0))   # cyan

# GreenZone — at Table A; triggers Mission 2
create_zone("GreenZone",  2.0, 5.0, 1.0, (0.0, 1.0, 0.0))   # green

# YellowZone — at Table B; triggers Mission 3
create_zone("YellowZone", 8.0, 5.0, 1.0, (1.0, 1.0, 0.0))   # yellow
