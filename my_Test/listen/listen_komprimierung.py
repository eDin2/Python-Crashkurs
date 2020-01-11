xs = [1, 2, 3, 4, 5, 6, 7, 8]

ys = [i * i for i in xs] # diese schriebweise ist das gleiche wie (siehe unten!)
# ys = []
# for i in xs:
#     ys.append(i * i)

print(xs)
print(ys)


# ##########################################################################

students = ["Saban", "Enida", "Edo", "Adis", "Emma"]

length = [len(i) for i in students] # diese schriebweise ist das gleiche wie (siehe unten!)
# length = []
# for i in students:
#     length.append(len(i))

print(length)

