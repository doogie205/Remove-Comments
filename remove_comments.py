#Ask for a file, if the file exists then user specifies a new file to
#Write to and that will be where the file without any 
#New lines or comments is placed.
import os
import re #use this to find comments mid line

filename = input("What file would you like to remove comments and new lines from?\n")

f = open(filename, "r")

line = "#Start"
cnt = 0
whole_file = ""
while line:
  if((re.search("#", line) != None)):
    temp_array = re.split("#", line, 1)
    #print(temp_array)
    line = temp_array[0]
    if(line == ""):
      line = f.readline()
      continue
    else:
      whole_file += "\n{}".format(line.strip())
      line = f.readline()
      cnt += 1
  else:
   #print("Line {}: {}".format(cnt, line.strip()))
   whole_file += "\n{}".format(line.strip())
   line = f.readline()
   cnt += 1
   
#print(whole_file)
f.close()

new_filename = input("What would you like the new file to be called?\n")

f = open("{}.py".format(new_filename), "w")

f.write(whole_file[1:len(whole_file)])

f.close()
