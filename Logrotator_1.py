'''
Created on Oct 9, 2017

@author: LSX1KOR
'''

import os
import time

filename = 'test1.log'
data_MB=1024*1024
size_index=20
temp_siz_index=0

#get the size of the file
if os.path.exists(filename):
    statinfo = os.stat(filename)
    size = statinfo.st_size
    print size
    if size>20:
        file_obj = open(filename, 'r')
        file_num = int(size / 20)

#        if temp_file_num>5:
#            file_num=5
#        else:
#            file_num=temp_file_num

        num = file_num
#        if temp_file_num > 5:
#            file_obj.seek((temp_file_num - file_num) * size_index)
#            temp_siz_index = size_index * (temp_file_num-file_num)

        for i in range(file_num + 1):
            if file_num > 5:
                file_obj.seek(size_index)
                file_num-=1
                print file_num
            else:
                if file_num == 0 :
                    temp_filename = filename
                else:
                    temp_filename = filename.split('.')[0] + '_' + str(file_num) + '.log'
                    file_num = file_num - 1
                print file_num
#                if temp_siz_index + 20 > sixze:
#                    size_index = size
#                else:
#                    temp_siz_index += 20

                with open(temp_filename, 'w') as fobj:
                    #First read from file and then write to another file
                    print "SAM"+str(size_index)
                    print "SATYAM" + str(temp_siz_index)
                    read_data = file_obj.read(size_index)
                    print "This is "+read_data
                    fobj.write(read_data)

        file_obj.close()
    else:
        pass
else:
    print ("No file is persent with the name " +filename)
