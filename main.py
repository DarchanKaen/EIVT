from src.EIVT_db_worker import DBWorker
from src.EIVT_iv_adder import IVAdder


version = "0.01"
modes_info_message = "Available Modes: \n\tTraining = 't' or 'training' \n\tAdd = 'a' or 'add' \n\tStatistics = 's' or 'stats' \n\tExport verbs = 'x' or 'export' \n\tInfo = 'i' or 'info' \n\tExit = 'e' or 'exit'"
modes_error_message = "Incorrect mode!"

dbWorker = DBWorker()
ivAdder = IVAdder(dbWorker)

print(f"Welcome to the English Irrefular Verbs Trainer [EIVT]. v{version}")
print(modes_info_message)

while True:    
    mode = input("Please, select Mode (or 'i' to info): ").lower()
    try:
        if 'e' == mode or 'exit' == mode:
            print("EXIT MODE!")
            break
        elif 't' == mode or 'training' == mode:
            print("TRAINING MODE!")
        elif 'a' == mode or 'add' == mode:
            print("ADD MODE!")
            dbWorker.connect()
            dbWorker.createTable()
            dbWorker.disconnect()
            ivAdder.add_process()
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