universe_age = 14_000_000_000
print(universe_age)


bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)


motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)


motorcycles.insert(0, "ducati")
print(motorcycles)

