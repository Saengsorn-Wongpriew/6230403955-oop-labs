import pdb


is_negative = False
while not is_negative:
    devidend = input("Please enter the devidend: ")
    devisor = input("Please enter the devisor: ")

    pdb.set_trace()
    if devidend < 0 or devisor < 0:
        is_negative = True
    else:
        print(devidend / devisor)
