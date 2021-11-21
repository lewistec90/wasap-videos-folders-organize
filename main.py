import os
import shutil

SAMPLE = "VID-20210830-WA0059.mp4"

years = {"2021": "2021"}
months = {"01": "Enero", "02": "Febrero", "03": "Marzo", "04": "Abril", "05": "Mayo", "06": "Junio", "07": "Julio",
          "08": "Agosto", "09": "Setiembre", "10": "Octubre", "11": "Noviembre", "12": "Diciembre"}
days = {"01": "01", "02": "02", "03": "03", "04": "04", "05": "05", "06": "06", "07": "07", "08": "08", "09": "09",
        "10": "10", "11": "11", "12": "12", "13": "13", "14": "14", "15": "15", "16": "16", "17": "17", "18": "18",
        "19": "19", "20": "20", "21": "21", "22": "22", "23": "23", "24": "24", "25": "25", "26": "26", "27": "27",
        "28": "28", "29": "29", "30": "30", "31": "31", }

arr = os.listdir()
arr.pop(0)
arr.pop(0)
print(arr)

# Directory
directory = "Nikhil"

# Parent Directory path
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"

# Path
# path = os.getcwd()
# print(path)
# try:
#     os.mkdir(path + "/test")
# except OSError:
#     print ("Creation of the directory %s failed" % path)
# else:
#     print ("Successfully created the directory %s " % path)

# source = 'C:/Users/sai mohan pulamolu/Desktop/deleted/source/'
# destination = 'C:/Users/sai mohan pulamolu/Desktop/deleted/destination/'
#
# allfiles = os.listdir(source)
#
# for f in allfiles:
#     os.rename(source + f, destination + f)

print(arr[ 0 ][ :-4 ].split('-'))
print("==============================")


def analyze_files(arr_files):
    narray_files = [ ]
    for file in arr_files:
        print(file)
        foldersname = file[ 4:-11 ]
        narray_files.append(foldersname)
        folder = years[ foldersname[ 0:4 ] ] + '-' + months[ foldersname[ 4:6 ] ]
        print(folder)
        destination = os.getcwd() + "\\" + folder
        print(destination)
        os.makedirs(destination, exist_ok=True)
        shutil.move(file, destination + "\\" + file)

    print(narray_files)

    return narray_files


# files = analyze_files(arr)

# print(files)
