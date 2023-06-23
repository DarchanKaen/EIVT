from src.EIVT_db_worker import DBWorker
from src.EIVT_iv_adder import IVAdder


version = "0.01"
modes_info_message = "Available Modes: \n\tTraining = 1 \n\tAdd = 2 \n\tStatistics = 3 \n\tExport verbs = 4 \n\tInfo = 5 \n\tExit = 0"
modes_error_message = "Incorrect mode!"

dbWorker = DBWorker()
ivAdder = IVAdder(dbWorker)

print(f"Welcome to the English Irrefular Verbs Trainer [EIVT]. v{version}")
print(modes_info_message)

while True:    
    mode_pre = input("Please, select Mode: ")
    try:
        mode = int(mode_pre)
        if 0 == mode:
            print("EXIT MODE!")
            break
        elif 1 == mode:
            print("TRAINING MODE!")
        elif 2 == mode:
            print("ADD MODE!")
            dbWorker.connect()
            dbWorker.createTable()
            dbWorker.disconnect()
            ivAdder.add_process()
        elif 3 == mode:
            print("STATISTICS MODE!")
        elif 4 == mode:
            print("EXPORT MODE!")
        elif 5 == mode:
            print(modes_info_message)
        else:
            print(modes_error_message )  
    except BaseException as error:
        print(modes_error_message)
        print(error)