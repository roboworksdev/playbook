# ─────────────────────────────────────────────────────────────────
#  Chapter 0  ·  Mission 3 — "Give Robby an Identity"
#  Load world:  chapter0_lab.py
# ─────────────────────────────────────────────────────────────────
#
#  OBJECTIVE
#  Robby needs a name, a model number, and a designation.
#  Store these as variables and use them in her status message.
#
#  NEW CONCEPT — VRobbyBLES
#    name = "Robby"
#    ↑ left side    ↑ right side
#    The variable   The VALUE stored inside it
#
#  A variable is like a labelled box.  You put a value in the box,
#  give the box a name, and then use the name whenever you want
#  that value.  Change the value once — it changes everywhere.
#
#  WHAT TO DO
#  1. Run the script and read the output.
#  2. Change the values of name, model, and unit_id.
#     Run again — what changes in the output?
#  3. Add a new variable  location = "Lab A"  and include it in
#     the boot message.
#
#  CHALLENGE
#  Add a variable  max_battery = 100  and use it to calculate
#  how full Robby's battery is as a percentage of max_battery.
# ─────────────────────────────────────────────────────────────────

# ── Declare variables ──────────────────────────────────────────
name     = "Robby"        # string  — robot's name
model    = "MK-1"        # string  — model designation
unit_id  = 42            # integer — unique unit number
online   = True          # boolean — is she active?

# ── Use the variables in printed messages ──────────────────────
print(f"Initialising unit {name} ({model}) ...")
print(f"Unit ID   : {unit_id}")
print(f"Online    : {online}")
print(f"Battery   : {battery_level()}%")
print(f"Boot sequence complete.  Welcome, {name}.")
