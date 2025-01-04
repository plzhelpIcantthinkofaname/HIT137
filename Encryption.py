def encrypt_text(text, n, m):  
   """  
   Encrypts the given text based on the provided encryption rules.  
  
   Args:  
      text (str): The text to be encrypted.  
      n (int): The first integer for encryption.  
      m (int): The second integer for encryption.  
  
   Returns:  
      str: The encrypted text.  
   """  
   encrypted_text = ""  
   for char in text:  
      if char.isalpha():  
        ascii_offset = 97 if char.islower() else 65  
        char_position = ord(char) - ascii_offset  
  
        if char.islower() and char_position < 13:  # First half of lowercase alphabet  
           new_position = (char_position + n * m) % 26  
        elif char.islower() and char_position >= 13:  # Second half of lowercase alphabet  
           new_position = (char_position - (n + m)) % 26  
        elif char.isupper() and char_position < 13:  # First half of uppercase alphabet  
           new_position = (char_position - n) % 26  
        else:  # Second half of uppercase alphabet  
           new_position = (char_position + m ** 2) % 26  
  
        encrypted_text += chr(new_position + ascii_offset)  
      else:  
        encrypted_text += char  
  
   return encrypted_text  
  
  
def decrypt_text(text, n, m):  
   """  
   Decrypts the given text based on the provided decryption rules.  
  
   Args:  
      text (str): The text to be decrypted.  
      n (int): The first integer for decryption.  
      m (int): The second integer for decryption.  
  
   Returns:  
      str: The decrypted text.  
   """  
   decrypted_text = ""  
   for char in text:  
      if char.isalpha():  
        ascii_offset = 97 if char.islower() else 65  
        char_position = ord(char) - ascii_offset  
  
        if char.islower() and char_position < 13:  # First half of lowercase alphabet  
           new_position = (char_position - n * m) % 26  
        elif char.islower() and char_position >= 13:  # Second half of lowercase alphabet  
           new_position = (char_position + (n + m)) % 26  
        elif char.isupper() and char_position < 13:  # First half of uppercase alphabet  
           new_position = (char_position + n) % 26  
        else:  # Second half of uppercase alphabet  
           new_position = (char_position - m ** 2) % 26  
  
        decrypted_text += chr(new_position + ascii_offset)  
      else:  
        decrypted_text += char  
  
   return decrypted_text  
  
  
def read_text_from_file(file_name):  
   """  
   Reads text from a file.  
  
   Args:  
      file_name (str): The name of the file to read from.  
  
   Returns:  
      str: The text read from the file.  
   """  
   try:  
      with open(file_name, 'r') as file:  
        return file.read()  
   except FileNotFoundError:  
      print("File not found.")  
      return ""  
  
  
def write_text_to_file(file_name, text):  
   """  
   Writes text to a file.  
  
   Args:  
      file_name (str): The name of the file to write to.  
      text (str): The text to be written.  
   """  
   with open(file_name, 'w') as file:  
      file.write(text)  
  
  
def main():  
   file_name = input("Enter the name of the text file: ")  
   text = read_text_from_file(file_name)  
  
   if text:  
      n = int(input("Enter the value of n: "))  
      m = int(input("Enter the value of m: "))  
  
      encrypted_text = encrypt_text(text, n, m)  
      print("Encrypted Text:")  
      print(encrypted_text)  
  
      encrypted_file_name = "encrypted_text.txt"  
      write_text_to_file(encrypted_file_name, encrypted_text)  
      print(f"Encrypted text written to {encrypted_file_name}")  
  
      decrypted_text = decrypt_text(encrypted_text, n, m)  
      print("Decrypted Text:")  
      print(decrypted_text)  
  
      decrypted_file_name = "decrypted_text.txt"  
      write_text_to_file(decrypted_file_name, decrypted_text)  
      print(f"Decrypted text written to {decrypted_file_name}")  
  
      if decrypted_text == text:  
        print("Decryption successful. The decrypted text matches the original text.")  
      else:  
        print("Decryption failed. The decrypted text does not match the original text.")  
  
  
if __name__ == "__main__":  
   main()