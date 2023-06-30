import os



class FilesWorker:
    
    def __init__(self, core_directory):
        self.core_directory = core_directory
        self.file_line_separator = "\n"

    
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


    def get_files_list_from_directory(self, directory_name):
        directory_files = []
        try:
            directory_files = [file for file in os.listdir(directory_name) if os.path.isfile(os.path.join(directory_name, file))]
        except BaseException as error:
            print(f"EIVT_ERROR: cannot fin files in directory: `{directory_name}`!")
            print(error)
        return directory_files
        

    def append_text_to_file(self, file_text, file_name, file_directory):
        try:
            file_full_path = os.path.join(file_directory, file_name)
            with open(file_full_path, "a") as some_file:
                some_file.write(file_text + self.file_line_separator)
        except BaseException as error:
            print(f"EIVT_ERROR: cannot add text to file: `{file_name}` in directory: `{file_directory}`!")
            print(error)


    def append_data_to_file(self, file_data, file_name, file_directory):
        try:
            file_full_path = os.path.join(file_directory, file_name)
            with open(file_full_path, "w") as some_file:
                for data_line in file_data:
                    some_file.write(data_line + self.file_line_separator)
        except BaseException as error:
            print(f"EIVT_ERROR: cannot export data to: `{file_name}` in directory: `{file_directory}`!")
            print(error)   
        
    
    def read_data_from_file(self, file_name, file_directory):
        file_data = []
        try:
            file_full_path = os.path.join(file_directory, file_name)
            with open(file_full_path, "r") as some_file:
                for data_line in some_file:
                    file_data.append(data_line)
        except BaseException as error:
            print(f"EIVT_ERROR: cannot import data from: `{file_name}` in directory: `{file_directory}`!")
            print(error)   
        return file_data


    
