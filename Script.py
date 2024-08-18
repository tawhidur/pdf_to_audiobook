import pyttsx3
from PyPDF2 import PdfReader

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Open and read the PDF file
pdfreader = PdfReader(open('Resume.pdf', 'rb'))

# Initialize an empty string to store all text from the PDF
full_text = ""

# Extract text from each page of the PDF
for page_number in range(len(pdfreader.pages)):
    page = pdfreader.pages[page_number]
    text = page.extract_text()
    if text:
        clean_text = text.strip().replace('\n', ' ')
        full_text += clean_text + " "  # Concatenate text from each page

# Print the text for debugging purposes
print(full_text)

# Save the concatenated text to an MP3 file
speaker.save_to_file(full_text, 'Resume.mp3')
speaker.runAndWait()

# Stop the speaker
speaker.stop()

