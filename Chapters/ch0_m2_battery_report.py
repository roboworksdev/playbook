# ─────────────────────────────────────────────────────────────────
#  Chapter 0  ·  Mission 2 — "Battery Report"
#  Load world:  chapter0_lab.py
# ─────────────────────────────────────────────────────────────────
#
#  OBJECTIVE
#  Robby needs to report her own status.  Use battery_level() and
#  an f-string to embed a live value inside a printed message.
#
#  NEW CONCEPTS
#    battery_level()    → a built-in robot function that returns a number
#    f"...{expr}..."    → f-string: the { } brackets are replaced by
#                         the VALUE of whatever is inside them
#
#  WHAT TO DO
#  1. Run this script and read the console output.
#  2. Run it several more times — does the battery number change?
#     Why might it decrease slightly each run?
#
#  CHALLENGE
#  Add a second line that prints how much battery is REMAINING
#  as a fraction, e.g.  "Robby has 0.97 of her battery left."
#  Hint: divide battery_level() by 100.
# ─────────────────────────────────────────────────────────────────

# battery_level() returns an integer (0–100).
# Wrap it in an f-string to embed it in a message.
print(f"Battery level: {battery_level()}%")

# You can do maths inside the curly braces:
print(f"Battery as a fraction: {battery_level() / 100}")

# A complete status report:
print(f"--- Robby STATUS REPORT ---")
print(f"  Power:  {battery_level()}%")
print(f"  Status: {'OK' if battery_level() > 20 else 'LOW POWER WARNING'}")
