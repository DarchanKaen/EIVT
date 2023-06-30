import os
from src.EIVT_db_worker import DBWorker
from src.EIVT_files_worker import FilesWorker
from src.EIVT_vocab_worker import VocabWorker
from src.EIVT_statistics_worker import StatisticsWorker
from src.EIVT_training_worker import TrainingWorker


self_path = os.path.dirname(__file__)
db_worker = DBWorker()  #for create database run EIVT_db_worker.py !!!
files_worker = FilesWorker(self_path)
vocab_worker = VocabWorker(db_worker)
statistics_worker = StatisticsWorker(files_worker)
training_worker = TrainingWorker(vocab_worker, statistics_worker)


app_codename = "[EIVT]"
app_name = "English Irregular Verbs Trainer [EIVT]"
app_version = "0.07"
app_the = f"{app_name}. v{app_version}"
welcome_message = f"{app_codename}. Welcome to the {app_name}. v{app_version}"
exit_message = f"{app_codename}. Goodbye and good luck!!!"
modes_info_message = f"{app_codename}. Available Modes: \n\tTraining = 't' or 'training' \n\tAdd = 'a' or 'add' \n\tStatistics = 's' or 'stats' \n\tExport verbs = 'x' or 'export' \n\tInfo = 'i' or 'info' \n\tExit = 'e' or 'exit'"
modes_error_message = "Incorrect mode!"


print(welcome_message)
print(modes_info_message)


while True:    
    mode = input(f"{app_codename}. Please, select Mode (or 'i' to info / 'e' to exit): ").lower()
    try:
        if 'e' == mode or 'exit' == mode:
            print(exit_message)
            break
        elif 't' == mode or 'training' == mode:
            training_worker.training_process()
        elif 'a' == mode or 'add' == mode:
            vocab_worker.add_process()
        elif 's' == mode or 'stats' == mode:
            statistics_worker.get_stats()
        elif 'x' == mode or 'export' == mode:
            print("EXPORT MODE!")
        elif 'i' == mode or 'info' == mode:
            print(modes_info_message)
        else:
            print(modes_error_message)  

    except BaseException as error:
        print(error)