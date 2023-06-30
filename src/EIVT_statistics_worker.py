from datetime import datetime



class StatisticsWorker:
    
    def __init__(self, files_worker):
        self.files_worker = files_worker
        self.statistics_directory_name = "Statistics"
        self.default_statistics_filename = "eivt_stats_"
        self.default_statistics_extension = ".txt"
        self.statistics_directory_path = self.files_worker.create_directory(self.statistics_directory_name)


    def addStats(self, training_result, max_questions):
        statfile_date = self.__create_current_statfile_name()
        full_statfile_name = f"{self.default_statistics_filename}{statfile_date}{self.default_statistics_extension}"
        pricese_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        stat_info = f"{pricese_date}. Correct answers: {training_result} / {max_questions}"
        print("stat_info: ", stat_info)
        self.files_worker.append_text_to_file(stat_info, full_statfile_name, self.statistics_directory_path)


    def __create_current_statfile_name(self):
        current_date = datetime.now().strftime("%d_%m_%Y")
        return current_date