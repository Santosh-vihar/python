from text_to_speech import save

a = input("Enter how to save file name: ")
s = input("What do you want to say: ")
e = int(input("Enter to exit (0): "))

while e != 0:
    text = s  # Assign the actual text input
    language = "te"  # Telugu language code
    output_file = f"{a}.mp3"  # Save as MP3 file

    save(text, language, file=output_file)
    
    e = int(input("Enter to exit (0): "))  # To allow exiting properly

print('..file is saved..')
