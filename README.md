📁 File Organizer (Python)
This is a Python automation script that organizes files in a selected folder into categories such as Images, Videos, Documents, Audio, and Others.

🚀 Features
Automatically detects file types
Creates folders if they don’t exist
Moves files into appropriate folders
Supports multiple file formats
Works with any directory path
Simple command-line interface

🧠 How It Works
The script scans a folder, identifies file extensions, and moves each file into a corresponding category:
Images → .jpg, .png, .jpeg, .gif
Videos → .mp4, .mkv, .avi
Documents → .pdf, .docx, .txt
Audio → .mp3, .wav
Others → all remaining file types

🛠️ Requirements
Python 3.x
No external libraries required (uses built-in os module)

▶️ How to Run
Clone or download this repository
Open a terminal or command prompt
Run the script:
python file_organizer.py
Enter the folder path when prompted

📂 Example
Before:
Downloads/
  photo.jpg
  video.mp4
  report.pdf
  song.mp3
After:
Downloads/
  Images/
    photo.jpg
  Videos/
    video.mp4
  Documents/
    report.pdf
  Audio/
    song.mp3
  Others/

⚠️ Notes
Make sure the folder path is correct
The script skips folders and only processes files
Existing files with the same name may be overwritten

📌 Future Improvements
Add GUI interface
Add duplicate file handling
Add logging system

👤 Author
Ssenkindu Abdushakuluh
abdushakuluhssenkindu@gmail.com
+256709934423

⭐ If you find this useful
Feel free to star the repository and share it!
