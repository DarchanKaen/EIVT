from src.EIVT_db_worker import DBWorker
from src.EIVT_vocab_worker import VocabWorker
from src.EIVT_training_worker import TrainingWorker


app_codename = "[EIVT]"
app_name = "English Irregular Verbs Trainer [EIVT]"
app_version = "0.06"
app_the = f"{app_name}. v{app_version}"
modes_info_message = "Available Modes: \n\tTraining = 't' or 'training' \n\tAdd = 'a' or 'add' \n\tStatistics = 's' or 'stats' \n\tExport verbs = 'x' or 'export' \n\tInfo = 'i' or 'info' \n\tExit = 'e' or 'exit'"
modes_error_message = "Incorrect mode!"

db_worker = DBWorker()  #for create database run EIVT_db_worker.py !!!
vocab_worker = VocabWorker(db_worker)
training_worker = TrainingWorker(vocab_worker)

print(f"Welcome to the {app_name}. v{app_version}")
print(modes_info_message)

while True:    
    mode = input(f"{app_codename}. Please, select Mode (or 'i' to info / 'e' to exit): ").lower()
    try:
        if 'e' == mode or 'exit' == mode:
            print("EXIT MODE!")
            break

        elif 't' == mode or 'training' == mode:
            print("TRAINING MODE!")
            training_worker.training_process()

        elif 'a' == mode or 'add' == mode:
            print("ADD MODE!")
            vocab_worker.add_process()

        elif 's' == mode or 'stats' == mode:
            print("STATISTICS MODE!")

        elif 'x' == mode or 'export' == mode:
            print("EXPORT MODE!")

        elif 'i' == mode or 'info' == mode:
            print(modes_info_message)
        else:
            print(modes_error_message)  

    except BaseException as error:
        print(error)