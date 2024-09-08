import os

def rename_files(root_dir, search_text, replace_text):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Rename files
        for filename in filenames:
            if search_text in filename:
                new_filename = filename.replace(search_text, replace_text)
                os.rename(
                    os.path.join(dirpath, filename),
                    os.path.join(dirpath, new_filename)
                )

if __name__ == "__main__":
    root_directory = "."  # Change this to your project's root directory
    search_text = "horilla"
    replace_text = "HRMS"
    
    rename_files(root_directory, search_text, replace_text)