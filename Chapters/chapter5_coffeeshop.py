# =============================================================================
#  Python Playbook — Chapter 5: Data Structure
#  World: The Coffee Shop  (10 m × 10 m)
# =============================================================================
#
#  LAYOUT  (origin = bottom-left)
#
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌────────────────────────────────────┐
# 9 │[══════════ COUNTER ═══════════════]│  ← white box at y=9.5
#   │☕Cup1 ☕Cup2  ◈Plate1 ◈Plate2   │  ← items on counter at y=9.0
#   │              ╴Knife1 ╴Knife2 ⌥Fork1 ⌥Fork2 │
# 8 │      ◉ CyanZone (5.0, 8.0)       │  ← triggers Mission 1
# 7 │                                   │
# 6 │                                   │
# 5 │  ◎ Table_A          ◎ Table_B    │  ← yellow cylinders
#   │  ● GreenZone(2.0,5.0)             │  ← triggers Mission 2
#   │                ● YellowZone(8,5)  │  ← triggers Mission 3
# 4 │                                   │
# 3 │                                   │
# 2 │                                   │
# 1 │  ★ Robot (5.0, 1.0)              │
#   └────────────────────────────────────┘
#
#  STORY
#  -----
#  It is morning set-up time at the coffee shop. Cups, plates, knives,
#  and forks are piled on the counter waiting to be laid out. Robby needs
#  to figure out what is there, build a list of what each table needs,
#  and organise the full service plan before the first customers arrive.
#
#  WORLD COORDINATES
#  ★  Robot start  : (5.0, 1.0)
#  ══  Counter     : (5.0, 9.5)  x spans 0.5–9.5  (white, fixed)
#  ☕  Cup_1       : (1.5, 9.0)  cyan cylinder
#  ☕  Cup_2       : (2.5, 9.0)  cyan cylinder
#  ◈   Plate_1     : (4.0, 9.0)  orange flat box
#  ◈   Plate_2     : (5.0, 9.0)  orange flat box
#  ╴   Knife_1     : (6.5, 9.0)  white thin box
#  ╴   Knife_2     : (7.2, 9.0)  white thin box
#  ⌥   Fork_1      : (8.0, 9.0)  green thin cylinder
#  ⌥   Fork_2      : (8.7, 9.0)  green thin cylinder
#  ◎   Table_A     : (2.0, 5.0)  yellow cylinder
#  ◎   Table_B     : (8.0, 5.0)  yellow cylinder
#  ◉   CyanZone    : (5.0, 8.0)  radius 1.0 — triggers Mission 1
#  ●   GreenZone   : (2.0, 5.0)  radius 1.0 — triggers Mission 2
#  ●   YellowZone  : (8.0, 5.0)  radius 1.0 — triggers Mission 3
#
#  PATH NOTES  (safe driving routes used in starter scripts)
#  ---------------------------------------------------------
#  Mission 1 — drive north from (5.0, 1.0) to CyanZone (5.0, 8.0)
#               7.0 m at drive(0.4, 0) ≈ sleep 2.2 s
#
#  Mission 2 — from CyanZone: 180° south turn, drive south, right turn west
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

# ── Cups on counter ────────────────────────────────────────────────────────────
# Two cyan cylinders representing coffee cups
create_object("Cup_1", "cylinder", "Cyan", "fixed",
              (0.15, 0.25, 0), (1.5, 9.0, 0), (0, 0, 0))

create_object("Cup_2", "cylinder", "Cyan", "fixed",
              (0.15, 0.25, 0), (2.5, 9.0, 0), (0, 0, 0))

# ── Plates on counter ─────────────────────────────────────────────────────────
# Two orange flat boxes representing dinner plates
create_object("Plate_1", "box", "Orange", "fixed",
              (0.3, 0.3, 0.05), (4.0, 9.0, 0), (0, 0, 0))

create_object("Plate_2", "box", "Orange", "fixed",
              (0.3, 0.3, 0.05), (5.0, 9.0, 0), (0, 0, 0))

# ── Knives on counter ─────────────────────────────────────────────────────────
# Two white thin boxes representing knives
create_object("Knife_1", "box", "White", "fixed",
              (0.05, 0.25, 0.05), (6.5, 9.0, 0), (0, 0, 0))

create_object("Knife_2", "box", "White", "fixed",
              (0.05, 0.25, 0.05), (7.2, 9.0, 0), (0, 0, 0))

# ── Forks on counter ──────────────────────────────────────────────────────────
# Two green thin cylinders representing forks
create_object("Fork_1", "cylinder", "Green", "fixed",
              (0.05, 0.25, 0), (8.0, 9.0, 0), (0, 0, 0))

create_object("Fork_2", "cylinder", "Green", "fixed",
              (0.05, 0.25, 0), (8.7, 9.0, 0), (0, 0, 0))

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
