#Ask for a file, if the file exists then user specifies a new file to
#Write to and that will be where the file without any 
#New lines or comments is placed.
import os
import re #use this to find comments mid line


filename = input("What file would you like to remove comments from?\n")

f = open(filename, "r")

comment_type = input("What comments does your language use? (ex. //)\n")

line = "{}Start".format(comment_type)
cnt = 0
whole_file = ""
while line:
  if((re.search(comment_type, line) != None)):
    if((comment_type == "//" and ((re.search("http://", line) == None) and ((re.search("https://", line) == None)))) or comment_type != "//"):
      temp_array = re.split(comment_type, line, 1)
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

f = open("{}".format(new_filename), "w")

f.write(whole_file[1:len(whole_file)])

f.close()

