number_tuple = (2, 10, 11, 3)
print("{0:<50} {1:>0}".format("input filenames are", str(number_tuple)))

file_list = []
for n in number_tuple:
    f = "file_{:04}".format(n)
    file_list.append(f)
print("{0:<50} {1:>0}".format("zero padded filenames", str(file_list)))

sorted_file = sorted(file_list)
print("{0:<50} {1:>0}".format("sorted filenames are", str(sorted_file)))
