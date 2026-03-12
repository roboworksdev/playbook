# =============================================================================
#  Python Playbook — Chapter 8: Evaluation
#  World: The Robot Cup Run  (10 m × 10 m)
# =============================================================================
#
#  LAYOUT  (origin = bottom-left)
#
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌────────────────────────────────────┐
# 9 │ [══════ KITCHEN COUNTER ════════] │
# 8 │          ◎ KitchenZone(5,8.5)    │
# 7 │  [T1]     [T2]     [T3]          │
# 6 │  ● Cup1   ● Cup2   ● Cup3        │
# 5 │  [T4]               [T5]         │
# 4 │  ■ Dish1             ■ Dish2     │
# 3 │                                  │
# 2 │          ★ Robot(5,2)            │
# 1 │          ◎ PodiumZone(5,1.5)     │
#   └────────────────────────────────────┘
#
#  ★  Robot start  : (5.0, 2.0)
#  ◎  KitchenZone  : (5.0, 8.5)  radius 1.5 — deliver cups/dishes here
#  ◎  PodiumZone   : (5.0, 1.5)  radius 1.0 — competition finish line
#  ●  Cup1         : (2.0, 6.5)  moveable sphere — T1 had 3 customers
#  ●  Cup2         : (5.0, 6.5)  moveable sphere — T2 had 1 customer
#  ●  Cup3         : (8.0, 6.5)  moveable sphere — T3 had 5 customers (busiest!)
#  ■  Dish1        : (2.0, 4.0)  moveable box    — T4 had 2 customers
#  ■  Dish2        : (8.0, 4.0)  moveable box    — T5 had 4 customers
# =============================================================================

# ── Furniture ─────────────────────────────────────────────────────────────────
# Kitchen counter — fixed slab along the back wall
create_object("KitchenCounter", "box", "White", "fixed",
              (8.0, 0.5, 0.4), (5.0, 9.5, 0), (0, 0, 0))

# Customer tables (fixed boxes)
create_object("TableT1", "box", "Yellow", "fixed",
              (0.8, 0.8, 0.5), (2.0, 7.0, 0), (0, 0, 0))
create_object("TableT2", "box", "Yellow", "fixed",
              (0.8, 0.8, 0.5), (5.0, 7.0, 0), (0, 0, 0))
create_object("TableT3", "box", "Yellow", "fixed",
              (0.8, 0.8, 0.5), (8.0, 7.0, 0), (0, 0, 0))
create_object("TableT4", "box", "Yellow", "fixed",
              (0.8, 0.8, 0.5), (2.0, 4.5, 0), (0, 0, 0))
create_object("TableT5", "box", "Yellow", "fixed",
              (0.8, 0.8, 0.5), (8.0, 4.5, 0), (0, 0, 0))

# ── Cups and dishes (one representative item per table) ───────────────────────
# Cup1 at Table T1 — T1 had 3 customers
create_object("Cup1",  "sphere", "Orange", "moveable",
              (0.25, 0, 0), (2.0, 6.5, 0), (0, 0, 0))
# Cup2 at Table T2 — T2 had 1 customer
create_object("Cup2",  "sphere", "Orange", "moveable",
              (0.25, 0, 0), (5.0, 6.5, 0), (0, 0, 0))
# Cup3 at Table T3 — T3 had 5 customers (the busiest table)
create_object("Cup3",  "sphere", "Orange", "moveable",
              (0.25, 0, 0), (8.0, 6.5, 0), (0, 0, 0))
# Dish1 at Table T4 — T4 had 2 customers
create_object("Dish1", "box", "Blue", "moveable",
              (0.4, 0.4, 0.1), (2.0, 4.0, 0), (0, 0, 0))
# Dish2 at Table T5 — T5 had 4 customers
create_object("Dish2", "box", "Blue", "moveable",
              (0.4, 0.4, 0.1), (8.0, 4.0, 0), (0, 0, 0))

# ── Trigger zones ──────────────────────────────────────────────────────────────
create_zone("KitchenZone", 5.0, 8.5, 1.5, (0.0, 1.0, 1.0))   # cyan  — kitchen drop-off
create_zone("T1Zone",      2.0, 6.5, 1.0, (0.0, 1.0, 0.0))   # green
create_zone("T2Zone",      5.0, 6.5, 1.0, (1.0, 1.0, 0.0))   # yellow
create_zone("T3Zone",      8.0, 6.5, 1.0, (1.0, 0.0, 0.0))   # red   — busiest table
create_zone("T4Zone",      2.0, 4.0, 1.0, (0.0, 0.0, 1.0))   # blue
create_zone("T5Zone",      8.0, 4.0, 1.0, (1.0, 0.5, 0.0))   # orange
create_zone("PodiumZone",  5.0, 1.5, 1.0, (1.0, 0.8, 0.0))   # gold  — trophy position

# ── Robot start ────────────────────────────────────────────────────────────────
set_robot_pos(5.0, 2.0)
