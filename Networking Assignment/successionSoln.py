f = open("succession.xml", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("succession.xml", "r")
print(f.read())