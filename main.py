from src.EIVT_db_worker import DBWorker
from src.EIVT_vocab_worker import VocabWorker
from src.EIVT_iv_adder import IVAdder


version = "0.01"
modes_info_message = "Available Modes: \n\tTraining = 't' or 'training' \n\tAdd = 'a' or 'add' \n\tStatistics = 's' or 'stats' \n\tExport verbs = 'x' or 'export' \n\tInfo = 'i' or 'info' \n\tExit = 'e' or 'exit'"
modes_error_message = "Incorrect mode!"

#for create database run EIVT_db_worker.py
db_worker = DBWorker()
vocab_worker = VocabWorker(db_worker)
iv_adder = IVAdder(db_worker)

print(f"Welcome to the English Irregular Verbs Trainer [EIVT]. v{version}")
print(modes_info_message)

while True:    
    mode = input("Please, select Mode (or 'i' to info / 'e' to exit): ").lower()
    try:
        if 'e' == mode or 'exit' == mode:
            print("EXIT MODE!")
            break
        elif 't' == mode or 'training' == mode:
            print("TRAINING MODE!")
            vocab_worker.get_random_irregular_verbs(3)
        elif 'a' == mode or 'add' == mode:
            print("ADD MODE!")
            iv_adder.upgraded_add_process(vocab_worker)
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