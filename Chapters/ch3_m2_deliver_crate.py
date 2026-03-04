# ─────────────────────────────────────────────────────────────────
#  Chapter 3  ·  Mission 2 — "To the Drop Zone"
#  Load world:  chapter3_warehouse.py
# ─────────────────────────────────────────────────────────────────
#
#  OBJECTIVE
#  Robby has Crate_1 attached from Mission 1.  Drive her to the
#  blue drop zone (centred at x=7.5, y=7.0) and release the crate
#  inside it.
#
#  NEW CONCEPT
#  ────────────
#  detach()  →  releases the currently held object.
#               The crate stays where Robby drops it.
#               holding() returns False afterwards.
#
#  THE MISSION
#  ───────────
#  1. Complete Mission 1 first to attach Crate_1.
#     Then run this script immediately (Robby still holds the crate).
#
#  2. Watch the crate travel with Robby across the warehouse.
#
#  3. After detach(), manually drive Robby away.
#     Does the crate stay put?  (It should — physics is "moveable"
#     but no force is applied once detached.)
#
#  WHAT TO OBSERVE
#  ───────────────
#  The drop zone is marked by 4 small blue cylinders at its corners.
#  Robby needs to be INSIDE the square when she calls detach().
#  The zone is 2 m × 2 m — plenty of room.
#
#  KEY INSIGHT
#  Notice the sequence of moves below uses the same drive() +
#  time.sleep() pattern from Chapter 1 — but now with cargo.
#  The robot's behaviour (moving) doesn't change; what changes is
#  that she carries a crate.  Abstraction in action.
#
#  CHALLENGE
#  After delivering, go back and collect Crate_2 (at x=7.0, y=4.0)
#  and bring it to the same drop zone.  Write the navigation steps
#  yourself.  Then think: can this be made into a function?
# ─────────────────────────────────────────────────────────────────

import time

print(f"Mission 2 start.  Battery: {battery_level()}%")
print(f"Carrying a crate? {holding()}")
print()

if not holding():
    print("WARNING: Robby is not holding anything.")
    print("Run Mission 1 first to attach Crate_1, then run this script.")
else:
    print("Crate on board. Navigating to drop zone at (7.5, 7.0) ...")
    print()

    # ── Part 1 — face east ─────────────────────────────────────────
    print("Step 1: turning east ...")
    drive(0.0, 1.0)       # turn right (face east)
    time.sleep(0.30)
    drive(0.0, 0.0)

    # ── Part 2 — drive east to x ≈ 7.5 ────────────────────────────
    #    From Crate_1 approach position (x ≈ 3.5): need ~4.0 m east
    print("Step 2: driving east ~4.0 m ...")
    drive(0.4, 0.0)
    time.sleep(1.39)      # ≈ 4.0 m at 2.88 m/s
    drive(0.0, 0.0)

    # ── Part 3 — face north ────────────────────────────────────────
    print("Step 3: turning north ...")
    drive(0.0, -1.0)      # turn left (face north)
    time.sleep(0.30)
    drive(0.0, 0.0)

    # ── Part 4 — drive north to y ≈ 7.0 ───────────────────────────
    #    From Crate_1 approach position (y ≈ 3.1): need ~3.9 m north
    print("Step 4: driving north ~3.9 m ...")
    drive(0.4, 0.0)
    time.sleep(1.35)      # ≈ 3.9 m at 2.88 m/s
    drive(0.0, 0.0)

    # ── Part 5 — release ───────────────────────────────────────────
    print()
    print("Inside drop zone. Releasing crate ...")
    detach()
    print(f"holding() = {holding()} — crate released!")
    print()
    print(f"Final battery: {battery_level()}%")
    print()
    print("Crate 1 delivered!")
    print("Next step: complete Mission 3 to define a collect_crate() function")
    print("and collect the remaining 3 crates.")
