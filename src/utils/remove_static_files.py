import shutil


# Remove static files
def remove_files(folder_name):
    shutil.rmtree(folder_name, ignore_errors=True)
