# ─────────────────────────────────────────────────────────────────
#  Chapter 2  ·  Mission 1 — "Feel the Room"
#  Load world:  chapter2_dark_room.py
# ─────────────────────────────────────────────────────────────────
#
#  OBJECTIVE
#  Robby is in the dark storage room. Before she can move safely,
#  she needs to understand her surroundings. In this mission you
#  use the LiDAR sensor to map the nearest obstacle in every
#  direction around her.
#
#  THE SENSOR
#  ──────────
#  distance(angle)  →  returns the distance in metres to the nearest
#                       object in that direction.
#
#  Angle convention (clockwise from front):
#    distance(0)    →  directly ahead (north)
#    distance(90)   →  to the right (east)
#    distance(180)  →  directly behind (south)
#    distance(270)  →  to the left (west)
#
#  THE MISSION
#  ───────────
#  1. Run this script and read the console output carefully.
#     Note which direction has the closest obstacle.
#
#  2. Look at the world map at the top of chapter2_dark_room.py.
#     Can you match each distance reading to an object on the map?
#       distance(0)   ≈ ?    (what is directly north?)
#       distance(90)  ≈ ?    (what is to the right?)
#       distance(270) ≈ ?    (what is to the left?)
#
#  3. Scan more angles:  distance(45),  distance(135),  distance(315).
#     Do any of these hit an obstacle shorter than distance(0)?
#
#  KEY INSIGHT
#  distance(angle) only reads ONE direction at a time.
#  Chapter 6 shows how to read all 360 at once using a list.
#  For now — one angle, one reading, one decision.
#
#  CHALLENGE
#  Write a for loop that prints distance readings every 45°:
#    for a in range(0, 360, 45):
#        print(f"  {a:>3}° → {distance(a):.2f} m")
#  Which direction has the most open space?
# ─────────────────────────────────────────────────────────────────

print(f"Sensor scan start.  Battery: {battery_level()}%")
print("Robby is stationary at (2.0, 2.0) facing north.")
print()

# ── Cardinal directions ────────────────────────────────────────────
print("Cardinal distance readings:")
print(f"  Ahead  (  0°): {distance(0):.2f} m")
print(f"  Right  ( 90°): {distance(90):.2f} m")
print(f"  Behind (180°): {distance(180):.2f} m")
print(f"  Left   (270°): {distance(270):.2f} m")
print()

# ── Diagonal directions ────────────────────────────────────────────
print("Diagonal distance readings:")
print(f"  NE     ( 45°): {distance(45):.2f} m")
print(f"  SE     (135°): {distance(135):.2f} m")
print(f"  SW     (225°): {distance(225):.2f} m")
print(f"  NW     (315°): {distance(315):.2f} m")
print()

# ── Find the nearest obstacle ──────────────────────────────────────
readings = {
    "North":     distance(0),
    "NE":        distance(45),
    "East":      distance(90),
    "SE":        distance(135),
    "South":     distance(180),
    "SW":        distance(225),
    "West":      distance(270),
    "NW":        distance(315),
}

nearest_dir = min(readings, key=readings.get)
nearest_m   = readings[nearest_dir]

print(f"Nearest obstacle: {nearest_dir} at {nearest_m:.2f} m")
print()
print("Can you identify this obstacle on the world map?")
print("Hint: open chapter2_dark_room.py and read the layout diagram.")
