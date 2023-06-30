from src.EIVT_db_worker import DBWorker
from src.EIVT_iv_adder import IVAdder
from src.EIVT_iv_trainer import IVTrainer


version = "0.01"
modes_info_message = "Available Modes: \n\tTraining = 't' or 'training' \n\tAdd = 'a' or 'add' \n\tStatistics = 's' or 'stats' \n\tExport verbs = 'x' or 'export' \n\tInfo = 'i' or 'info' \n\tExit = 'e' or 'exit'"
modes_error_message = "Incorrect mode!"

db_worker = DBWorker()
iv_adder = IVAdder(db_worker)
iv_trainer = IVTrainer(db_worker)

print(f"Welcome to the English Irregular Verbs Trainer [EIVT]. v{version}")
print(modes_info_message)

while True:    
    mode = input("Please, select Mode (or 'i' to info): ").lower()
    try:
        if 'e' == mode or 'exit' == mode:
            print("EXIT MODE!")
            break
        elif 't' == mode or 'training' == mode:
            print("TRAINING MODE!")
            iv_trainer.get_all_irregular_verbs()
            iv_trainer.get_random_irregular_verbs(3)
        elif 'a' == mode or 'add' == mode:
            print("ADD MODE!")
            db_worker.connect()
            db_worker.createTable()
            db_worker.disconnect()
            iv_adder.add_process()
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