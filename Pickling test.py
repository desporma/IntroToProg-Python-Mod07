# ------------------------------------------------- #
# Title: Pickle Test
# Description: Pickle multiple types of data and unpickle.
# ChangeLog: (Who, When, What)
# DEsporma,11.29.2021,Created Script
# ------------------------------------------------- #


# Pre-pickling  ----------------------------------- #
import pickle


# Data -------------------------------------------- #
# Declare variables for pickling
pickle_str = "hello"
pickle_int = 3
pickle_lst = ["apple", "peach", "banana"]
pickle_dic = {"veg1" : "potato", "veg2" : "broccoli", "veg3" : "spinach"}
pickle_all = [pickle_str, pickle_int, pickle_lst, pickle_dic]

# Declare file
file = "pickle.dat"


# Processing -------------------------------------- #
# Write pickled representation of pickle_all as binary code to pickle.dat
objFile = open(file, "ab")
pickle.dump(pickle_all, objFile)
objFile.close()

# Read the pickled representation (binary) of pickle_all from pickle.dat
objFile = open(file, "rb")
objFileData = pickle.load(objFile)
objFile.close()


# Presentation ------------------------------------ #
# Print unpickled contents of pickle.dat
print("Data was unpickled as the following:")
print(objFileData)