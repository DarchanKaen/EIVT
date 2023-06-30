import os



class FilesWorker:
    
    def __init__(self, core_directory):
        self.core_directory = core_directory

    
    def create_directory(self, directory_name):
        result_directory_path = None
        target_directory = os.path.join(self.core_directory, directory_name)
        try:
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)
            result_directory_path = target_directory
        except BaseException as error:
            print(f"EIVT_ERROR: cannot create directory {target_directory}!")
            print(error)
        return result_directory_path

    def append_text_to_file(self, file_text, file_name, file_directory):
        print("file_name, file_directory:", file_name, file_directory)
        try:
            file_full_path = os.path.join(file_directory, file_name)
            print("file_full_path:", file_full_path)
            with open(file_full_path, "a") as some_file:
                some_file.write(file_text + "\n")
            pass
        except BaseException as error:
            print(f"EIVT_ERROR: add text to file: `{file_name}` in dirctory: `{file_directory}`!")
            print(error)
        
        


    
