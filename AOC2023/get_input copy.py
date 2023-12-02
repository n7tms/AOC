# aoc_utils.py
import os
import subprocess
import time

COOKIE = '53616c7465645f5f141dd45ab20dfb545e65b2aa8bd07bba88954eea1c6e1f4b123aba791fd4f90fa961c1ee8228ee2cbc8d44e47a9540ecb7b63af2364464ce'


# def retrieve(year, day):
#     cmd = "curl https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input --cookie \"session=" + COOKIE + "\" > " + str(year) + str(day).zfill(2) + ".txt"
#     # print(os.system(cmd))
#     print(cmd)



def get_input(year, day, force=False):
    # Does force=True? or Does the file not exist?
    #   Yes: retrieve the input data and [over]write the txt file.
    # Does the file exist and force=False?
    #   Yes: return None

    target_file = "AOC2023\\inputs\\" + str(year) + str(day).zfill(2) + ".txt"
    print(target_file)
    if os.path.exists(target_file) and not force:
        print("retrieve(): \'" + target_file + "\' already exists. (force not True)")
        return None
    else:
        cmd = "curl https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input --cookie \"session=" + COOKIE + "\" > " + target_file 
        print(cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

        # give the subprocess time to finish
        time.sleep(5)

get_input(2023,2,True)
    

