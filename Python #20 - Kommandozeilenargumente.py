import sys

print("Diese Datei heisst", sys.argv[0])
summe = int(sys.argv[1]) + int(sys.argv[2])
with open(sys.argv[3], "w") as file:
	file.write(str(summe))

# Langform für with ... as .... :
# file = open(sys.argv[3], "w")
# file.write(str(summe))
# file.close()
