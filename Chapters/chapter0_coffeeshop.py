# =============================================================================
#  Python Playbook — Chapter 0: Introduction
#  World: The Coffee Shop  (10 m × 10 m)
# =============================================================================
#
#  LAYOUT  (origin = bottom-left)
#
#   0  1  2  3  4  5  6  7  8  9  10   ← x
#   ┌────────────────────────────────────┐
# 9 │ [═══════ COUNTER ════════════]    │
# 8 │                          ◉ RedCol │
# 7 │          [T2]     [T3]            │
# 6 │                  ■ YellowBlock    │
# 5 │      [T1]                         │
# 4 │               ● GreenBall         │
# 3 │                                   │
# 2 │  ★ Robot (2,2)                    │
# 1 │                                   │
#   └────────────────────────────────────┘
#
#  ★  Robot start : (2.0, 2.0)
#  ●  GreenBall   : (5.0, 4.0)  moveable sphere
#  ■  YellowBlock : (7.0, 6.5)  moveable box
#  ◉  RedColumn   : (8.5, 8.0)  fixed cylinder
# =============================================================================

# ── Mission objects ───────────────────────────────────────────────────────────
# GreenBall — the ball Robby picks up first
create_object("GreenBall",   "sphere",   "Green",  "moveable",
              (0.35, 0, 0),     (5.0, 4.0, 0),  (0, 0, 0))

# YellowBlock — the block Robby delivers the ball to, then picks up
create_object("YellowBlock", "box",      "Yellow", "moveable",
              (0.5, 0.5, 0.5),  (7.0, 6.5, 0),  (0, 0, 0))

# RedColumn — the final destination
create_object("RedColumn",   "cylinder", "Red",    "fixed",
              (0.3, 1.5, 0),    (8.5, 8.0, 0),  (0, 0, 0))

# ── Drop zones ─────────────────────────────────────────────────────────────────
create_zone("GreenZone",  5.0, 4.0, 1.0, (0.0, 1.0, 0.0))
create_zone("YellowZone", 7.0, 6.5, 1.0, (1.0, 1.0, 0.0))
create_zone("RedZone",    8.5, 8.0, 1.0, (1.0, 0.0, 0.0))
