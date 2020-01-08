#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for x in range(list_length):
        try:
            z = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            z = 0
        except ZeroDivisionError:
            print("division by 0")
            z = 0
        except IndexError:
            print("out of range")
            z = 0
        finally:
            new.append(z)
    return new

