import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy as sp
import numpy as np
import math
import shutil


##### PART - 1: abstraction of RAWdecoder and FFMENC epoch time from ffmpeg log  ###########

# Reading of file & modification part
f = open("/home/surya/Downloads/Tilakw2/ffmpeg.log",'r')
out = f.readlines()
f.close()
length = len(out)
temp = []
temp1 = []
temp2 = []

for i in range(0,length):
    if "raw_decode() called" in out[i]:
        temp1 = out[i].lstrip().split();
        #print temp1[1]
        temp1_1 = temp1[0].split("[")
        temp1_2 = temp1_1[1].split("]")
        #print(temp1_2[0])
    elif "FFMENC --> Start_time" in out[i]:
        temp2 = out[i].lstrip().split();
        temp2_1 = temp2[0].split("[")
        temp2_2 = temp2_1[1].split("]")
        #print(temp1[7])
    elif "UTILS: the size in append_packet_chunked" in out[i]:
        temp3 = out[i].lstrip().split();
        #print temp1[1]
        temp3_1 = temp3[0].split("[")
        temp3_2 = temp3_1[1].split("]")
        #print(temp1_2[0])
    elif " UTILS:read_frame_internal() no parsing needed:" in out[i]:
        temp4 = out[i].lstrip().split();
        temp4_1 = temp4[0].split("[")
        temp4_2 = temp4_1[1].split("]")
        if len(temp1)!=0 and len(temp2)!=0:
            temp.append(temp1[6]+"\t"+temp1_2[0]+"\t"+temp2_2[0]+"\t"+temp3_2[0]+"\t"+temp4_2[0]+"\n")


#writing modified data to anotherfile
f_out = open("/home/surya/Downloads/Tilakw2/python_generated_raw.log",'w')
for item in temp:
    f_out.write("%s" % item)
f_out.close()
#print(temp)

#shutil.copy2('/home/surya/Downloads/Tilakw2/python_generated_raw.log', '/home/surya/Downloads/Tilakw2/python_generated_raw_part1.log')


##### PART - 2: abstraction of epoch time from render log for particular frame from ffmpeg log ###########

# Reading of file & modification part

# epoch time of render frame from render log will be added to below opened file

f_render = open("/home/surya/Downloads/Tilakw2/render1.log",'r')
out_render = f_render.readlines()
length_render = len(out_render)
f_render.close()

f_bmp = open("/home/surya/Downloads/Tilakw2/python_generated_raw.log",'r')
out_bmp = f_bmp.readlines()
length_bmp = len(out_bmp)
f_bmp.close()
k= 0
z = []
for i in range(0,length_bmp-1):
        temp_1 = out_bmp[i].lstrip().split();
        j = k
        for l in range(j,length_render-1):
            temp_2 = out_render[l].lstrip().split();
            if int(temp_1[0])==int(temp_2[3]):
                temp_1.append(temp_2[0])
                #print(temp_1)
                z.append(temp_1[0]+"\t"+temp_1[5]+"\t"+temp_1[1]+"\t"+temp_1[2]+"\t"+temp_1[3]+"\t"+temp_1[4]+"\n")
                k+=1
                break
#writing modified data
f_out = open("/home/surya/Downloads/Tilakw2/python_generated_raw.log",'w')
for item in z:
    f_out.write("%s" % item)
f_out.close()

#shutil.copy2('/home/surya/Downloads/Tilakw2/python_generated_raw.log', '/home/surya/Downloads/Tilakw2/python_generated_raw_part2.log')


##### PART - 3: abstraction of epoch time from render log for particular frame from serverlog ###########

f_server = open("/home/surya/Downloads/Tilakw2/server.log",'r')
out_server = f_server.readlines()
length_server = len(out_server)
f_server.close()
# epoch time of ffmdec frame from server log will be added to below opened file
f = open("/home/surya/Downloads/Tilakw2/python_generated_raw.log",'r')
out = f.readlines()
length = len(out)

print "length",  length
print "length_server",  length_server

f.close()


z = []
temp_FFMD2_s_p = []
temp_FFMD2_s_c = []
temp_BS_s_p = []
temp_BS_s_c = []
#for n in range(0,length-1):
 #   temp_2_1 = out[n].lstrip().split();
 #   print temp_2_1[0]


for i in range(2,length_server-2):
## i = 20539
    if "TEST FFMDEC2 ->" in out_server[i]:
        temp_1 = out_server[i].lstrip().split();
        #j = k
        temp_FFMD2_s_p = temp_FFMD2_s_c
        temp_FFMD2_s_c = temp_1

        #print "i=", i
        #print "temp_FFMD2_s_p", temp_FFMD2_s_p
        #print "temp_FFMD2_s_c", temp_FFMD2_s_c

    if "Bytes sent" in out_server[i + 1]:
        temp_1_1 = out_server[i + 1].lstrip().split();
        temp_BS_s_p = temp_BS_s_c
        temp_BS_s_c = temp_1_1

        if (temp_BS_s_c[18] > 0) & (len(temp_FFMD2_s_p)>1):
            #print "i+1 in Bytes sent=", i+1
            #print "temp_FFMD2_s_p", temp_FFMD2_s_p
            #print "temp_FFMD2_s_c", temp_FFMD2_s_c
            #print "temp_BS_s_p", temp_BS_s_p
            #print "temp_BS_s_c", temp_BS_s_c

            if int(temp_FFMD2_s_p[8]) == int(temp_BS_s_c[18]):

                for l in range(0,length-1):
                    temp_2 = out[l].lstrip().split();
                    #temp_2_1_n = out[l + 1].lstrip().split();

                    if int(temp_BS_s_c[18]) == int(temp_2[0]):
                        # print(temp_1[8] + "\t" + temp_2_1_1[0])
                        #temp_2.append(temp_1[11])
                        #temp_2.append(temp_1_1[11])

                        temp_2.append(temp_FFMD2_s_p[11])
                        temp_2.append(temp_BS_s_p[11])    ###  To get timestamp of previous frame in Byte sent
                        #temp_2.append(temp_BS_s_c[11])     ### To get timestamp at current frame in Byte sent

                        #print "frame", temp_2[0], "temp_2", temp_2
                        # print(temp_1)
                        # print temp_1[8]
                        z.append(temp_2[0] + "\t" + temp_2[1] + "\t" + temp_2[2] + "\t" + temp_2[3] + "\t" + temp_2[4] + "\t" + temp_2[
                            5] + "\t" + temp_2[6] + "\t" + temp_2[7] + "\n")
                        break



#writing modified data
f_out = open("/home/surya/Downloads/Tilakw2/python_generated_raw.log",'w')
for item in z:
    f_out.write("%s" % item)
f_out.close()
#print(temp)
print("##end: PART-3")


#shutil.copy2('/home/surya/Downloads/Tilakw2/python_generated_raw.log', '/home/surya/Downloads/Tilakw2/python_generated_raw_part3.log')
