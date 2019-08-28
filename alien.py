warna_aliens = ["green", "red", "yellow"]

if "green" in warna_aliens:
    poin = 10
elif "yellow" in warna_aliens:
    poin = 15
elif "red" in warna_aliens:
    poin = 20
else:
    poin = 0
print(f"you earns ${poin} point in this game")
