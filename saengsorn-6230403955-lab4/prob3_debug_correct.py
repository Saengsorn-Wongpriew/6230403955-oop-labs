is_negative = False
while not is_negative:
    devidend = int(input("Please enter the devidend: "))
    devisor = int(input("Please enter the devisor: "))

    if devidend < 0 or devisor < 0:
        is_negative = True
    else:
        if devisor == 0:
            print("Cannot perform devision by zero")
        else:
            print(devidend / devisor)
