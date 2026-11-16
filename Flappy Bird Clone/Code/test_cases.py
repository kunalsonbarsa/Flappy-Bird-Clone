# Test 1: Normal input (y=300, v=0, 2 frames)
y, v = 300, 0
for f in range(2):
    v += 1
    y += v
    print("Test 1 Frame", f + 1, "-> velocity:", v, "| y:", y)

# Test 2a: Ground collision (y=570, bird height 30)
y = 570
print("Test 2a ->", "Collision with ground | Game Over" if y + 30 >= 600 else "OK")

# Test 2b: Top boundary (y=5, v=0, SPACE pressed)
y, v = 5, 0
v = -10
v += 1
y += v
print("Test 2b -> velocity:", v, "| y:", y, "|", "Bird left the screen at the top | Game Over" if y < 0 else "OK")

# Test 3: Invalid key Z (ignored)
y, v = 300, 0
key = "Z"
if key == "SPACE":
    v = -10
v += 1
y += v
print("Test 3 -> Key ignored | velocity:", v, "| y:", y)

# Test 4a: SPACE pressed with v=5
y, v = 300, 5
v = -10
v += 1
y += v
print("Test 4a -> velocity:", v, "| y:", y)

# Test 4b: Pipe at x=39, width 60, bird x=100
pipe_right = 39 + 60
print("Test 4b ->", "Pipe passed | Score: 1" if pipe_right < 100 else "Not passed")