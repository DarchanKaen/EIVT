class ImportWorker:
    
    def __init__(self, vocab_worker, files_worker):
        self.vocab_worker = vocab_worker
        self.files_worker = files_worker
        self.import_directory_name = "Import"
        self.default_import_full_filename = "eivt_import.txt"
        self.import_values_delimiter = ";"
        self.add_values_delimiter = " "


    def import_data(self):
        import_pre_data = self.files_worker.read_data_from_file(self.default_import_full_filename, self.import_directory_name)
        import_data = self.__format_import_data(import_pre_data)
        for iv_string in import_data:
            self.vocab_worker.add_irregular_verb(iv_string)
        print("Import finished successfully!")


    def __format_import_data(self, unformatted_import_data):
        formatted_import_data = []
        for iverb_raw_string in unformatted_import_data:
            iverb_list = iverb_raw_string.split(self.import_values_delimiter)
            iverb_correct_string = f"{iverb_list[0].strip()}{self.add_values_delimiter}{iverb_list[1].strip()}{self.add_values_delimiter}{iverb_list[2].strip()}"
            formatted_import_data.append(iverb_correct_string)
        return formatted_import_data