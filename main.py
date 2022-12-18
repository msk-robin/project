  
b = [
  [" "," "," "],
  [" "," "," "],
  [" "," "," "],
]

print("Welcome to tic-tac-toe!")
print("Enter your choices like 1,1 or 2,3")
print(f"""
  1   2   3
1 {b[0][0]} | {b[0][1]} | {b[0][2]}
--- --- ---
2 {b[1][0]} | {b[1][1]} | {b[1][2]}
--- --- ---
3 {b[2][0]} | {b[2][1]} | {b[2][2]}
""")
player = "X"


while True:
  choice = input(f"player {player}, where do you want to play? ")
  numbers = choice.split(",")
  row = int(numbers[0]) - 1
  col = int(numbers[1]) - 1
  b[row][col] = player
  print(f"""
  1   2   3
1 {b[0][0]} | {b[0][1]} | {b[0][2]}
--- --- ---
2 {b[1][0]} | {b[1][1]} | {b[1][2]}
--- --- ---
3 {b[2][0]} | {b[2][1]} | {b[2][2]}
""")
  for r in b:
    if r[0] == r[1] == r[2] and r[0] != " ":
      print(f"winner: {r[0]}")
      exit()
  
  for c in range(3):
    if b[0][c] == b[1][c] == b[2][c] and b[0][c] != " ":
      print(f"winner: {b[0][c]}")
      exit()

  if b[0][0] == b[1][1] == b[2][2] and b[0][0] != " ":
    print(f"winner: {b[0][0]}")
    exit()
  if b[0][2] == b[1][1] == b[2][0] and b[0][2] != " ":
    print(f"winner: {b[0][2]}")
    exit()

  if player == "X":
    player = "O"
  else:
    player = "X"