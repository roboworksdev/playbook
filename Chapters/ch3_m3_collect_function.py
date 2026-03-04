# ─────────────────────────────────────────────────────────────────
#  Chapter 3  ·  Mission 3 — "Teach Robby a New Skill"
#  Load world:  chapter3_warehouse.py
# ─────────────────────────────────────────────────────────────────
#
#  OBJECTIVE
#  The sequential grab-and-deliver code from Missions 1 and 2 works —
#  but only for one crate, and only if you rewrite it four times.
#  In this mission you extract the repetition into a FUNCTION so
#  the whole skill can be called in one line.
#
#  WHY FUNCTIONS?
#  ──────────────
#  def collect_crate(cx, cy):   ← teaches Robby a new skill
#      ...
#
#  collect_crate(3.5, 4.0)     ← Robby uses the skill once
#  collect_crate(7.0, 4.0)     ← ... and again
#
#  One definition.  Many uses.  If you want to change the delivery
#  zone, you change it in ONE place inside the def block.
#  This is why functions exist.
#
#  PARAMETERS (preview — covered fully in Chapter 4)
#  ──────────────────────────────────────────────────
#  cx and cy are INPUT VALUES passed to the function when called.
#  Think of them as 'blank slots' that get filled in on each call:
#    collect_crate(3.5, 4.0)  →  cx=3.5, cy=4.0
#    collect_crate(7.0, 4.0)  →  cx=7.0, cy=4.0
#
#  THE MISSION
#  ───────────
#  1. Read the function definitions below.  Can you trace what each
#     one does before running the script?
#
#  2. Run the script.  Does Robby collect both crates?
#
#  3. Uncomment lines at the bottom to collect Crates 3 and 4.
#     Do you need to change the function?  (You shouldn't.)
#
#  KEY INSIGHT
#  'Once you teach Robby a skill, she knows it forever.'
#  The def block is the teaching.  The call is the doing.
#  A function is a named, reusable piece of behaviour.
#
#  ASSESSMENT CHALLENGE
#  Write:  def return_to_base():
#  Robby drives from wherever she is back to (2.0, 2.0).
#  Hint: use distance() readings to navigate, not fixed sleep times.
# ─────────────────────────────────────────────────────────────────

import time

# Drop zone centre (where Robby deposits all crates)
DROP_X = 7.5
DROP_Y = 7.0

# ── Helper: navigate to absolute position (x, y) ─────────────────
#    Uses face-east-then-north strategy from a known heading.
#    Note: heading accuracy depends on Robby's current orientation.
#    For a full solution, use LiDAR-based navigation (Chapter 6).

def navigate_to(tx, ty):
    """Drive Robby from current position toward target (tx, ty).

    Strategy: face east, drive to target x, face north, drive to target y.
    Timing assumes Robby is roughly at the origin facing north.
    Adjust sleep values if positions differ significantly.
    """
    # Estimate distances (based on Crate_1 approach position ≈ (2.0, 2.0))
    east_dist  = tx - 2.0          # metres east to travel
    north_dist = ty - 2.0          # metres north to travel
    east_time  = east_dist  / 2.88 # seconds at speed 0.4
    north_time = north_dist / 2.88

    if east_time > 0:
        drive(0.0, 1.0);  time.sleep(0.30)     # face east
        drive(0.4, 0.0);  time.sleep(east_time) # drive east
        drive(0.0, 0.0)
        drive(0.0, -1.0); time.sleep(0.30)     # face north
    else:
        drive(0.0, -1.0); time.sleep(0.30)     # face north directly


def approach_crate():
    """Creep forward until close_enough() to the nearest crate."""
    while not close_enough():
        drive(0.2, 0.0)
    drive(0.0, 0.0)


def deliver_to_zone():
    """Carry attached crate to the drop zone and release it."""
    # Face east
    drive(0.0, 1.0);  time.sleep(0.30)
    drive(0.0, 0.0)
    # Drive east to DROP_X
    drive(0.4, 0.0);  time.sleep(1.39)   # ≈ 4 m east (from x≈3.5)
    drive(0.0, 0.0)
    # Face north
    drive(0.0, -1.0); time.sleep(0.30)
    drive(0.0, 0.0)
    # Drive north to DROP_Y
    drive(0.4, 0.0);  time.sleep(1.35)   # ≈ 4 m north (from y≈3.1)
    drive(0.0, 0.0)
    # Release
    detach()
    print(f"  Crate delivered. holding()={holding()}")


# ── The skill: collect a crate from (cx, cy) and deliver it ──────
def collect_crate(cx, cy):
    """Navigate to crate at (cx, cy), grab it, deliver to drop zone.

    Parameters:
        cx (float): x-position of the crate centre
        cy (float): y-position of the crate centre
    """
    print(f"Collecting crate at ({cx}, {cy}) ...")
    navigate_to(cx, cy)    # drive close to the crate
    approach_crate()       # creep until close_enough()
    attach()               # grab
    print(f"  Attached. holding()={holding()}")
    deliver_to_zone()      # carry to drop zone and release


# =================================================================
#  MAIN MISSION — call the skill for each crate
# =================================================================
print(f"Collection mission start.  Battery: {battery_level()}%")
print()

# ── Crate 1 ───────────────────────────────────────────────────────
collect_crate(3.5, 4.0)
print()

# ── Crate 2 ───────────────────────────────────────────────────────
collect_crate(7.0, 4.0)
print()

# ── Crates 3 and 4 (uncomment to collect) ─────────────────────────
# collect_crate(1.5, 6.5)   # Crate_3 — north-west
# collect_crate(4.5, 7.5)   # Crate_4 — north-centre

print(f"Mission complete.  Battery: {battery_level()}%")
print("All collected crates are in the drop zone.")
print()
print("REFLECTION:")
print("  Did you need to change the def blocks to collect each crate?")
print("  What would happen if you changed DROP_X and DROP_Y?")
print("  How many lines would this be WITHOUT functions?")
