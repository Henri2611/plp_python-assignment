file_name = input("Enter the filename to read: ")
try:
  file = open(file_name, "r")
  content = file.read()
  file.close()

  print("File read successfully")
   # Modify the content  to make it uppercase
  modified_content = content.upper()

  # Create new filename
  new_file = "modified_" + file_name

  # Write the modified content to new file
  output_file = open(new_file, "w")
  output_file.write(modified_content)
  output_file.close()

  print(f"Modified content saved as '{new_file}'")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied when trying to read '{file_name}'.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")


 
 