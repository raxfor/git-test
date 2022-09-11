
# Creating a new file called nuevoDocumento.txt
# f = open("nuevoDocumento.txt", "x")

# Creating a new file called nuevoDocumento.txt and writing the text "Biografia de un programador
# inicial en python" in it. Then it is reading the file and printing it.
f = open("nuevoDocumento.txt", "w")
f.write("Biografia de un programador inicial en python")
f.close()
f = open("nuevoDocumento.txt", "r")
print(f.read())
