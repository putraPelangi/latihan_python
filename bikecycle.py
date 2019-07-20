bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# print list ke 0
print(bicycles[0])

# title list ke 0
print(bicycles[0].title())

# print list -1 akan dihitung dari belakang
print(bicycles[-1])

# fungsi f-string
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
