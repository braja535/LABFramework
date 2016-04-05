import datetime
import re
import string
import os


"""
    We opened input file in readmode and then applying pattern on each line and
        if pattern found
            apply "linemodification()" function on each line.
                   linemodifcation function apply regular expression on line  and find all the occurances of pattern in line and returns list .
                          then we will replace total string with new string as "time" with "modifed time" on each occurance
                               modification of time is done with "timemodifier_string()" --(have 2 arguments as string with time, and timegap )
                                        and timegap can be get with "timediff()" function
        else if pattern not found
                fetched line will be written to the new file
"""



pattern = re.compile("\d+:\d+:\d+")

# These line are enhances for Object oriented programmings
#def __init__(self,actual_time,existing_time):
#    self.actual_time_loc = actual_time
#    self.existing_time_loc = existing_time
#    self.difference = self.actual_time_loc - self.existing_time_loc

def timediff():
    global difference_time
    timegap_condition =raw_input("Do you have time difference in seconds(Yes/No) : ")
    if timegap_condition.upper() in ['Y','YES'] :
        difference_time = input("Enter time gap in seconds (to create delay in display enter as negative number): ")
        return difference_time
    else :
        actual_time = datetime.datetime.strptime(raw_input("Enter actual Subtitle location (HH:MM:SS format):  ").strip(),"%H:%M:%S")
        existing_time = datetime.datetime.strptime(raw_input("where you want to keep your Subtitle in location (HH:MM:SS format):  ").strip(),"%H:%M:%S")
        if actual_time < existing_time :
            difference_time = actual_time - existing_time
        else :
             difference_time = existing_time - actual_time
    return difference_time.total_seconds()


def linemodification(line):
    strings = pattern.findall(line)
    for a in strings:
        line = string.replace(line,a,timemodifier_string(a,timegap))
    return line
     #iterobj = pattern.finditer(line)
     #for a in iterobj  :#
     #str.replace(line,a.group(),addtime_string(a.group(),timegap))

def timemodifier_string(date_as_string,timegap):
    try:
        datestring = datetime.datetime.strftime(datetime.datetime.strptime(date_as_string,"%H:%M:%S") + datetime.timedelta(seconds=timegap),"%H:%M:%S")
    except :
         datestring = date_as_string
    return datestring

def main():

    inputfile = raw_input("Enter input file name : ")
    save_path = r"C:\Users\badan\Desktop\\"
    outputfile = os.path.join(save_path, inputfile + "_new.srt")
    infsrt = open(inputfile,'r')
    opfsrt = open(outputfile,'w')
    global timegap
    timegap = timediff()
    for eachline in infsrt.xreadlines():
        if pattern.match(eachline):
            opfsrt.write(linemodification(eachline))
        else :
            opfsrt.write(eachline)
    infsrt.close()
    opfsrt.close()

if __name__ == '__main__' :
    main()






######################################################################################################################
#                                       ROUGH WORK for Reference                                                     #
######################################################################################################################
"""
datetime.datetime.strftime(datetime.datetime.strptime(match.group(),"%H:%M:%S") + datetime.timedelta(seconds=35),"%H:%M:%S")
datetime.datetime.now().time().strftime("%H:%M:%S")
 datetime.datetime.strptime("23:40:15","%H:%M:%S")
datetime.datetime.now() - datetime.timedelta(seconds=35)
datetime.datetime.strptime(,"%H:%M:%S")+datetime.timedelta(seconds=35)
 a = rex.finditer("00:00:58,000 --> 00:01:00,640")
for match in a :
    datetime.datetime.strptime(match.group(),"%H:%M:%S") + datetime.timedelta(seconds=35)
ef addtime(line)
   pattern = re.compile("\d+:\d+:\d+")
   a = rex.finditer(line)
   for match in a :
       timestrings = datetime.datetime.strftime(datetime.datetime.strptime(match.group(),"%H:%M:%S") + datetime.timedelta(seconds=35),"%H:%M:%S")
"""
#######################################################################################################################