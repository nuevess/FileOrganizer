import os
import shutil

folder_to_organize = "/path/to/your/downloads/folder"

file_types = {

    "Documents": [".pdf", ".docx", ".txt"],

    "Images": [".jpg", ".jpeg", ".png"],

    "Videos": [".mp4", ".mov", ".avi"]

}

for filename in os.listdir(folder_to_organize):

    file_path = os.path.join(folder_to_organize, filename)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():

            if any(filename.endswith(ext) for ext in extensions):
                folder_path = os.path.join(folder_to_organize, folder)

                os.makedirs(folder_path, exist_ok=True)

                shutil.move(file_path, folder_path)

            break
