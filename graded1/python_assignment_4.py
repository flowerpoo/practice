import shutil
from datetime import date
from pathlib import Path
import os
import time


def take_backup(src_dir,des_dir):
    today = date.today()    # fetch todays date
    date_format = time.strftime("%d_%b_%Y_%H_%M_%S") # date and time format
    try:
        # getting all files in src dir
        files=os.listdir(src_dir)
        files2=os.listdir(des_dir)
       
        for fname in files:
            # check destination folder contains same file name in sorce folder 
            # if yes then append date and time in the name of file in destination folder 
            if fname in files2:
                src = os.path.join(src_dir, fname)
                des = os.path.join(des_dir, fname+date_format)
                shutil.copy2(src,des)
            #if destination folder not contains source file name then name must be same 
            else:
                src = os.path.join(src_dir, fname)
                des = os.path.join(des_dir, fname)
                shutil.copy2(src,des)
            
        print("Backup success")
       
    except FileNotFoundError:
        print("File Not found please choose correct file")

#f1 source folder
# f2 destination folder
take_backup('f1','f2')