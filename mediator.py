import struct
import numpy as np

class Mediator:

    def __init__(self):
        pass

    @staticmethod
    def read_binary_file(file_name, fmt):
        print "reading binary file '%s'" % (file_name)
        with open(file_name, "rb") as f:
            bin_data = f.read()
            data_len = len(bin_data)/struct.calcsize(fmt)
            unpacked = struct.unpack(str(data_len) + fmt, bin_data)
            unpacked_arr = np.array(unpacked)
            return unpacked_arr

    @staticmethod
    def write_binary_file(file_name, arr, fmt):
        print "writing binary file '%s'" % (file_name)
        with open(file_name, "wb") as f:
            data_len = arr.shape[0]
            bin_data = struct.pack(str(data_len) + fmt, *arr)
            f.write(bin_data)

file_name_in = "data/data.bin"
result = Mediator.read_binary_file(file_name_in, "d")
file_name_out = "data/data2.bin"
Mediator.write_binary_file(file_name_out, result, "d")
