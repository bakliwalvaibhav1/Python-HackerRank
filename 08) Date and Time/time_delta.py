"""
TITLE: Time Delta

INPUT:
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

OUTPUT:
25200
88200

"""


import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    wd1 = t1[:3]
    dd1 = int(t1[3:6])
    mon1 = t1[7:10]
    yy1 = int(t1[10:15])
    hh1 = int(t1[16:18])
    mm1 = int(t1[19:21])
    ss1 = int(t1[22:24])
    off1 = t1[25:26]
    offh1 = t1[26:28]
    offm1 = t1[28:30]

    z1 = offh1+':'+offm1+':'+'00'


    wd2 = t2[:3]
    dd2 = int(t2[3:6])
    mon2 = t2[7:10]

    yy2 = int(t2[10:15])
    hh2 = int(t2[16:18])
    mm2 = int(t2[19:21])
    ss2 = int(t2[22:24])

    off2 = t2[25:26]
    offh2 = t2[26:28]
    offm2 = t2[28:30]

    z2 = offh2+':'+offm2+':'+'00'
    # List of months.

    month_set = ['Dummy','Jan','Feb','Mar','Apr','May',
                 'Jun','Jul','Aug','Sep','Oct','Nov','Dec']


    timestamp1 = datetime.datetime(yy1, month_set.index(mon1),
    dd1, hour = hh1, minute=mm1, second=ss1, microsecond=0, tzinfo=None)
    timestamp2 = datetime.datetime(yy2, month_set.index(mon2),
    dd2, hour=hh2, minute=mm2, second=ss2, microsecond=0, tzinfo=None)

    offset1 =datetime.time(hour=int(offh1), minute=int(offm1),
    second=0, microsecond=0, tzinfo=None)
    offset2 =datetime.time(hour=int(offh2), minute=int(offm2),
    second=0, microsecond=0, tzinfo=None)

    if(off1 == '+'):
        timestamp1 = timestamp1 - datetime.timedelta(
           hours=int(offh1), minutes=int(offm1))
    if(off1 == '-'):
        timestamp1 = timestamp1 + datetime.timedelta(
           hours=int(offh1), minutes=int(offm1))
    if(off2 == '+'):
        timestamp2 = timestamp2 - datetime.timedelta(
                hours=int(offh2), minutes=int(offm2))
    if(off2 == '-'):
        timestamp2 = timestamp2 + datetime.timedelta(
                 hours=int(offh2), minutes=int(offm2))

    diff = str((abs(int(((timestamp1-datetime.datetime(1970,1,1)).

    total_seconds())-((timestamp2-datetime.datetime(1970,1,1)).total_seconds()      )))))

    return(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
