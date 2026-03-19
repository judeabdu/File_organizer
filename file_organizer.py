import os
folder = input("Enter folder path: ")
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}
files = os.listdir(folder)
print("\n         FILES AVAILABLE", )
for file in files:
    file_path = os.path.join(folder, file)
    if os.path.isdir(file_path):
        continue
    _, ext = os.path.splitext(file)
    for category, extensions in file_types.items():
        if ext.lower() in extensions:
            category_path = os.path.join(folder, category)
            if not os.path.exists(category_path):
                os.mkdir(category_path)
            destination = os.path.join(category_path, file)
            count = 1
            while os.path.exists(destination):
                name, ext2 = os.path.splitext(file)
                new_name = f"{name}_{count}{ext2}"
                destination = os.path.join(category_path, new_name)
                count += 1
            os.rename(file_path, destination)
            break
print("Files organized successfully!")

