#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    # temp_time=s.split(":")
    # if "am" in temp_time[-1].lower():
    #     if int(temp_time[0]) == 12:
    #         temp_time[0] = str(0)
    #         temp_time[-1] = temp_time[-1].lower().replace("am", "")
    #         return (":".join(temp_time))
    #     else:
    #         return s.lower().replace("am", "")
    # else:
    #     if int(temp_time[0]) != 12:
    #         temp_time[0] =str(12 + int(temp_time[0]))
    #         temp_time[-1] = temp_time[-1].lower().replace("pm", "")
    #         return (":".join(temp_time))
    #     else:
    #         return s.lower().replace("pm", "")

    temp_time=s.split(":")

    if 'AM' in temp_time[-1] :
        if temp_time[0] == '12':
            temp_time[0] = '00'
            return(":".join(temp_time).replace("AM", ""))
        else:
            return(":".join(temp_time).replace("AM", ""))
    else:
        if temp_time[0] == '12':
            return(":".join(temp_time).replace("PM", ""))
        else:
            temp_time[0] = str(int(temp_time[0])+12)
            return(":".join(temp_time).replace("PM", ""))



if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    # f.write(result + '\n')

    # f.close()
