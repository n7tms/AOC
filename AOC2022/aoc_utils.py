import os
import subprocess

COOKIE = '53616c7465645f5fa81b69e51cebf457a669874ce2a15e1038f8f07c7b2c764fbdd4ebf3fdba2a0351327ebe2f78f40fd0196440f065c82c90bc05836750f14d'


# def retrieve(year, day):
#     cmd = "curl https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input --cookie \"session=" + COOKIE + "\" > " + str(year) + str(day).zfill(2) + ".txt"
#     # print(os.system(cmd))
#     print(cmd)



def get_input(year, day, force=False):
    # Does force=True? or Does the file not exist?
    #   Yes: retrieve the input data and [over]write the txt file.
    # Does the file exist and force=False?
    #   Yes: return None

    target_file = str(year) + str(day).zfill(2) + ".txt"
    print(target_file)
    if os.path.exists(target_file) and not force:
        print("retrieve(): \'" + target_file + "\' already exists. (force not True)")
        return None
    else:
        cmd = "curl https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input --cookie \"session=" + COOKIE + "\" > " + target_file 
        print(cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        