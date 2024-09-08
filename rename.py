import os

def replace_in_file(file_path, search_text, replace_text):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace(search_text, replace_text)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def rename_files_and_dirs(root_dir, search_text, replace_text):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Rename .py files
        for filename in filenames:
            if filename.endswith('.jpg') and search_text in filename:
                new_filename = filename.replace(search_text, replace_text)
                os.rename(
                    os.path.join(dirpath, filename),
                    os.path.join(dirpath, new_filename)
                )
        
        # Rename directories
        for dirname in dirnames:
            if search_text in dirname:
                new_dirname = dirname.replace(search_text, replace_text)
                os.rename(
                    os.path.join(dirpath, dirname),
                    os.path.join(dirpath, new_dirname)
                )

def search_and_replace(root_dir, search_text, replace_text):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.jpg'):
                file_path = os.path.join(dirpath, filename)
                replace_in_file(file_path, search_text, replace_text)
    
    rename_files_and_dirs(root_dir, search_text, replace_text)

if __name__ == "__main__":
    root_directory = "."  # Change this to your project's root directory
    search_text = "HRMS"
    replace_text = "HRMS"
    
    search_and_replace(root_directory, search_text, replace_text)
