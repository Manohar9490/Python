#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER  = "[name]"

with open("c:/Users/manoh/OneDrive/Documents/Python Scripts/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
    # Your code here

  names = name_file.readlines()
#   print(names)


with open("c:/Users/manoh/OneDrive/Documents/Python Scripts/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
  letter_content = letter_file.read()
#   print(letter_content)
  for name in names:
    new_letter = letter_content.replace(PLACEHOLDER,name.strip())
    with open(f"c:/Users/manoh/OneDrive/Documents/Python Scripts/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name.strip()}.docx", mode="w") as completed_letter:
      completed_letter.write(new_letter)
  