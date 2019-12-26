import shutil
import os
import time

BASE_DIR = ""  # the base directory path
NEW_DIR = ""  # the new directory path

while True:
    time.sleep(2)
    if os.path.exists(BASE_DIR) and os.path.isdir(BASE_DIR):
        if not os.listdir(BASE_DIR):  # empty
            pass
        else:  # not empty
            time.sleep(1)
            for i in os.listdir(BASE_DIR):
                shutil.move(BASE_DIR + "/" + i, NEW_DIR)
                print("Success!")
    else:
        print("Given Directory deosn't exist!")
        False
