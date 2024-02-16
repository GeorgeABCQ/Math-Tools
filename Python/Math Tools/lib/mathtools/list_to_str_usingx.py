def list_to_str_usingx(list):
    str1 = ""
    count = 0
    for i in list:
        i = str(i)
        count += 1
        if count == len(list):
            str1 = str1 + i
        else:
            str1 = str1 + i + " x "
    return str1