from datetime import datetime



class ExportWorker:
    
    def __init__(self, vocab_worker, files_worker):
        self.vocab_worker = vocab_worker
        self.files_worker = files_worker
        self.export_directory_name = "Export"
        self.default_export_filename = "irregular_verbs_"
        self.default_export_extension = ".txt"
        self.export_values_delimiter = ";"
        self.export_directory_path = self.files_worker.create_directory(self.export_directory_name)

    
    def export_data(self):
        exportfile_date = self.__create_current_exportfile_name()
        full_exportfile_name = f"{self.default_export_filename}{exportfile_date}{self.default_export_extension}"
        export_pre_data = self.vocab_worker.get_all_irregular_verbs()
        export_data = self.__format_export_data(export_pre_data)
        self.files_worker.append_data_to_file(export_data, full_exportfile_name, self.export_directory_path)
        print(f"Export finished successfully! Exported {len(export_data)} irregular verbs.")


    def __create_current_exportfile_name(self):
        current_date = datetime.now().strftime("%d_%m_%Y")
        return current_date


    def __format_export_data(self, unformatted_export_data):
        formatted_export_data = []
        for iverbs_tuple in unformatted_export_data:
            iverb_string = f"{iverbs_tuple[0]}{self.export_values_delimiter}{iverbs_tuple[1]}{self.export_values_delimiter}{iverbs_tuple[2]}"
            formatted_export_data.append(iverb_string)
        return formatted_export_data