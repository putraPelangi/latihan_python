motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# mengubah isi list ke 1
# motorcycles[0] = "ducati"
# print(motorcycles)


# appending list
motorcycles.append("ducati")
print(motorcycles)

# menambah isi list dari kosong dengan append
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

# menyisipkan nilai pada list ke 0
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles)

# menghapus isi list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# use pop untuk cek list terakhir
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# hapus list berdasarkan value
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
