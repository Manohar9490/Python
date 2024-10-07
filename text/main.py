# with open("c:/Users/manoh/OneDrive/Documents/Python Scripts/text/file.txt") as file:
#   contents =file.read()
#   print(contents)


# with open("c:/Users/manoh/OneDrive/Documents/Python Scripts/text/file.txt", mode="a") as file:
#   file.write("\nlets eat biryani")


with open("file1.txt")  as file:
  file1 = (file.readlines())

with open("file2.txt")  as file:
  file2 = (file.readlines())

result = [ int(n) for n in file1 if n in file2]

print(result)