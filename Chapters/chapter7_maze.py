# =============================================================================
#  Python Playbook — Chapter 7: Navigation Algorithms
#  World: The Service Maze  (10 m × 10 m)
# =============================================================================
#
#  LAYOUT  (origin = bottom-left)
#
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌────────────────────────────────────┐
# 9 │            ◎ ExitZone(5,9)         │  ← Warehouse side
#   │        ┃ CorridorL   CorridorR ┃   │  ← x=4 and x=6
# 8 │        ┃  exit corridor        ┃   │
#   │        ┃  ☆ CoffeeBag(5,8.9)  ┃   │
#   │        ┗━━━━━ WarehouseWall ━━━┛   │  ← WarehouseWall y=9.3
#   │ ████████████ ← Wall2 ──  ████████  │  ← Wall2 at y=7.0
# 7 │  Wall2L      GAP(4–6)    Wall2R    │
#   │                                    │
# 6 │   ◉ ObsA(3.5,5.5)  ◉ ObsC(6.5,5.5)│  ← obstacle arena
#   │            ◉ ObsB(5,6.2)           │
# 5 │                                    │
#   │ ████████████ ← Wall1 ──  ████████  │  ← Wall1 at y=4.5
# 4 │  Wall1L      GAP(3.5–6.5) Wall1R   │
#   │                                    │
# 3 │  ● ● ● ● ● Yellow line ● ● ● ●    │  ← line markers at x=5, y=2.0–4.0
# 2 │                                    │
# 1 │           ★ Robot(5,1)             │
#   └────────────────────────────────────┘
#
#  ★  Robot start     : (5.0, 1.0)  facing north
#  ☆  CoffeeBag       : (5.0, 8.9)  moveable green sphere — mission target
#  ◎  ExitZone        : (5.0, 9.0)  radius 1.0  — warehouse marker (cyan)
#  ◉  ObstacleA       : (3.5, 5.5)  red fixed cylinder — blocks left path
#  ◉  ObstacleB       : (5.0, 6.2)  red fixed cylinder — blocks centre path
#  ◉  ObstacleC       : (6.5, 5.5)  red fixed cylinder — blocks right path
#  ●  Line1–Line5     : (5, 2.0–4.0)  yellow fixed flat boxes — guide line
#
#  LIDAR REFERENCE  (robot at (5,1), heading north = 0°, clockwise)
#  distance(0)   = open (gap in Wall1 at x=5)  — no block until outer wall
#  distance(90)  = outer east wall surface ≈ 4.75 m
#  distance(180) = outer south wall surface ≈ 0.75 m
#  distance(270) = outer west wall surface ≈ 4.75 m
#
#  CORRIDOR LIDAR  (robot centred at (5, y) between corridor walls x=4 and x=6)
#  CorridorR inner surface at x=5.85 (centre=6.0, half x-extent=0.15)
#  distance(90) from robot centre (x=5.0) = 5.85 − 5.0 = 0.85 m
#  TARGET_RIGHT = 0.85 keeps robot centred in the 2 m corridor
#
#  TIMING REFERENCE  (drive(0.4, 0) ≈ 2.88 m/s)
#  Robot(5,1) → Wall1 gap (y=4.5)  : ~3.5 m, driven by line-follow loop
#  Arena entry → Wall2 (y=7.0)     : ~2.5 m, driven by avoidance loop
#  Corridor entry → CoffeeBag      : ~1.8 m, driven by wall-follow loop
#  180° turn at drive(0, 1.0)      : sleep ≈ 0.60 s
#  90°  turn at drive(0, 1.0)      : sleep ≈ 0.30 s
# =============================================================================

# ── Maze walls ─────────────────────────────────────────────────────────────────
# Wall1 — first horizontal barrier at y=4.5
# Gap at x=3.5–6.5 (3 m wide, centred on x=5)
# Left segment:  x=0   to x=3.5,  centre=(1.75, 4.5)
# Right segment: x=6.5 to x=10,   centre=(8.25, 4.5)
create_object("Wall1L", "box", "White", "fixed",
              (3.5, 0.3, 1.0), (1.75, 4.5, 0), (0, 0, 0))
create_object("Wall1R", "box", "White", "fixed",
              (3.5, 0.3, 1.0), (8.25, 4.5, 0), (0, 0, 0))

# Wall2 — second horizontal barrier at y=7.0
# Narrower gap at x=4.0–6.0 (2 m wide) — forces robot through exit corridor
# Left segment:  x=0   to x=4.0,  centre=(2.0, 7.0)
# Right segment: x=6.0 to x=10,   centre=(8.0, 7.0)
create_object("Wall2L", "box", "White", "fixed",
              (4.0, 0.3, 1.0), (2.0, 7.0, 0), (0, 0, 0))
create_object("Wall2R", "box", "White", "fixed",
              (4.0, 0.3, 1.0), (8.0, 7.0, 0), (0, 0, 0))

# Exit corridor walls — vertical, x=4.0 and x=6.0, from y=7.0 to y=9.3
# 2 m wide corridor — wall-following distance target = 0.85 m from right wall
create_object("CorridorL", "box", "White", "fixed",
              (0.3, 2.3, 1.0), (4.0, 8.15, 0), (0, 0, 0))
create_object("CorridorR", "box", "White", "fixed",
              (0.3, 2.3, 1.0), (6.0, 8.15, 0), (0, 0, 0))

# Warehouse wall — seals the top of the exit corridor at y=9.3
create_object("WarehouseWall", "box", "White", "fixed",
              (2.0, 0.3, 1.0), (5.0, 9.3, 0), (0, 0, 0))

# ── Yellow line markers ────────────────────────────────────────────────────────
# Five flat yellow squares along x=5, spacing 0.5 m from y=2.0 to y=4.0.
# The robot uses look() to track them and steer toward the nearest one.
# Each marker: 25 cm × 25 cm footprint, 5 cm tall (lies flat on the floor).
create_object("Line1", "box", "Yellow", "fixed",
              (0.25, 0.25, 0.05), (5.0, 2.0, 0), (0, 0, 0))
create_object("Line2", "box", "Yellow", "fixed",
              (0.25, 0.25, 0.05), (5.0, 2.5, 0), (0, 0, 0))
create_object("Line3", "box", "Yellow", "fixed",
              (0.25, 0.25, 0.05), (5.0, 3.0, 0), (0, 0, 0))
create_object("Line4", "box", "Yellow", "fixed",
              (0.25, 0.25, 0.05), (5.0, 3.5, 0), (0, 0, 0))
create_object("Line5", "box", "Yellow", "fixed",
              (0.25, 0.25, 0.05), (5.0, 4.0, 0), (0, 0, 0))

# ── Obstacles ──────────────────────────────────────────────────────────────────
# Three red cylinders form a slalom in the obstacle arena (y=4.5 to y=7.0).
# ObstacleA and ObstacleC flank the centre path; ObstacleB blocks straight ahead.
# Each obstacle: 0.5 m diameter, 1.0 m tall — clearly visible in camera and LiDAR.
create_object("ObstacleA", "cylinder", "Red", "fixed",
              (0.5, 1.0, 0), (3.5, 5.5, 0), (0, 0, 0))
create_object("ObstacleB", "cylinder", "Red", "fixed",
              (0.5, 1.0, 0), (5.0, 6.2, 0), (0, 0, 0))
create_object("ObstacleC", "cylinder", "Red", "fixed",
              (0.5, 1.0, 0), (6.5, 5.5, 0), (0, 0, 0))

# ── Mission target ─────────────────────────────────────────────────────────────
# CoffeeBag — at the far end of the exit corridor, in front of the warehouse wall.
# Moveable green sphere, radius 0.3 m.
# close_enough() fires when robot centre is within ~0.95 m of CoffeeBag centre
# (distance to surface < 0.65 m: surface = centre − 0.3 m = y=8.6)
create_object("CoffeeBag", "sphere", "Green", "moveable",
              (0.3, 0, 0), (5.0, 8.9, 0), (0, 0, 0))

# ── Trigger zones ──────────────────────────────────────────────────────────────
# LineZone  — just north of Wall1 gap; fires when robot passes through Wall1
create_zone("LineZone",  5.0, 5.5, 0.8, (0.9, 0.7, 0.0))   # orange

# ArenaZone — just north of Wall2 gap; fires when robot enters the exit corridor
create_zone("ArenaZone", 5.0, 7.5, 0.8, (0.0, 0.8, 0.2))   # green

# ExitZone  — warehouse end of the corridor; visual marker for the story
create_zone("ExitZone",  5.0, 9.0, 1.0, (0.0, 1.0, 1.0))   # cyan

# ── Robot start ────────────────────────────────────────────────────────────────
set_robot_pos(5.0, 1.0)
