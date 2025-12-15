import time

clock_shape = [
    ["@@@@@",
     "@   @",
     "@   @",
     "@---@",
     "@   @",
     "@   @",
     "@@@@@"],
    ["----@",
     "-   @",
     "-   @",
     "----@",
     "-   @",
     "-   @",
     "----@"],
    ["@@@@@",
     "-   @",
     "-   @",
     "@@@@@",
     "@   -",
     "@   -",
     "@@@@@"],
    ["@@@@@",
     "-   @",
     "-   @",
     "@@@@@",
     "-   @",
     "-   @",
     "@@@@@"],
    ["@---@",
     "@   @",
     "@   @",
     "@@@@@",
     "-   @",
     "-   @",
     "----@"],
    ["@@@@@",
     "@   -",
     "@   -",
     "@@@@@",
     "-   @",
     "-   @",
     "@@@@@"],
    ["@@@@@",
     "@   -",
     "@   -",
     "@@@@@",
     "@   @",
     "@   @",
     "@@@@@"],
    ["@@@@@",
     "-   @",
     "-   @",
     "----@",
     "-   @",
     "-   @",
     "----@"],
    ["@@@@@",
     "@   @",
     "@   @",
     "@@@@@",
     "@   @",
     "@   @",
     "@@@@@"],
    ["@@@@@",
     "@   @",
     "@   @",
     "@@@@@",
     "-   @",
     "-   @",
     "@@@@@"],
    [" ", "#", "#", " ", "#", "#", " "]
]

def getClock():
    clock_format = time.strftime("%H:%M:%S")
    clock_return = []
    for i in range(len(clock_format)):
        if clock_format[i] == '0':
            clock_return.append(clock_shape[0])
        elif clock_format[i] == '1':
            clock_return.append(clock_shape[1])
        elif clock_format[i] == '2':
            clock_return.append(clock_shape[2])
        elif clock_format[i] == '3':
            clock_return.append(clock_shape[3])
        elif clock_format[i] == '4':
            clock_return.append(clock_shape[4])
        elif clock_format[i] == '5':
            clock_return.append(clock_shape[5])
        elif clock_format[i] == '6':
            clock_return.append(clock_shape[6])
        elif clock_format[i] == '7':
            clock_return.append(clock_shape[7])
        elif clock_format[i] == '8':
            clock_return.append(clock_shape[8])
        elif clock_format[i] == '9':
            clock_return.append(clock_shape[9])
        elif clock_format[i] == ':':
            clock_return.append(clock_shape[10])

    return clock_return

def getClockFormatShape(i):
    clock_format = getClock()

    return f"{clock_format[0][i]} {clock_format[1][i]} {clock_format[2][i]} {clock_format[3][i]} {clock_format[4][i]} {clock_format[5][i]} {clock_format[6][i]} {clock_format[7][i]}"
