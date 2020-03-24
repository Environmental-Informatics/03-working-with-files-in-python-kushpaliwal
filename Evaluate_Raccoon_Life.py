"""
Created on February  25, 2020
by Kush Paliwal

Script to read data file "2008Male00006.txt", process the data,and create a new output file called "Georges_life.txt".
"""

import math

# Mean of list
def list_mean(l):
    listmean = list_sum(l)/len(l)
    return listmean
    
# Cumulative sum of list
def list_sum(l):
    listsum = 0
    for i in range(len(l)):
        listsum = listsum + float(l[i])
    return listsum

# Distance between two points provided as two lists
def list_dis(l1,l2):
    # 1-D array for distance with initial value = 0
    dist=[0]*len(l1)
    for i in range(1,len(l1)):
        l1[i] = float(l1[i])
        l1[i-1] = float(l1[i-1])
        l2[i] = float(l2[i])
        l2[i-1] = float(l2[i-1])
        dist[i] = math.sqrt((l1[i]-l1[i-1])**2+(l2[i]-l2[i-1])**2)
    return dist

# open "2008Male00006.txt"
fo = open("2008Male00006.txt", "r")
lines = fo.readlines()

# close file
fo.close()

n=len(lines)

# store first line of original data as Headers
Headers = lines[0].strip().split(",")

# list to store the content of original data
Data=[]
for line in lines[1:n]:
    if line.find(",") != -1:
        Data.append([n for n in line.strip().split(",")])
    # store line without comma as the Status
    else:
        Status = line.strip()

# dictionary to store Headers and Data (list of values)
Data_dict = {}
for i in range(len(Headers)):
    Data_dict[Headers[i].strip()] = [row[i] for row in Data]

# list to store the distances and add it to dictionary
Distance = {}
Distance['Distance'] = list_dis(Data_dict['X'],Data_dict['Y'])
Data_dict = dict(Data_dict, **Distance)

# Generate output file called "Georges_life.txt"
fw = open("Georges_life.txt", "w")

# header block for the output file
raccoon_name = Headers[3]+Data_dict[Headers[3]][0]
x_ave = str(list_mean(Data_dict['X']))
y_ave = str(list_mean(Data_dict['Y']))
sum_dis = str(list_sum(Data_dict['Distance']))
ave_Engergy = str(list_mean(Data_dict['Energy Level']))

New_Headers = ["Raccoon name: "+ raccoon_name + "\n"
               "Average location: "+ x_ave + ", "+ y_ave + "\n"
               "Distance traveled: "+ sum_dis + "\n"
               "Average energy level: " + ave_Engergy+"\n"
               "Raccoon end state: "+ Status + "\n"]

# store labels of content with TAB delimited
New_Data_label = ["Date\tTime\tX\tY\tAsleep Flag\tBehavior Mode\tDistance Traveled\n"]

# store the select contents of data dictionary with TAB delimited
New_Data=[]
for i in range(len(Data)):
    New_Data.append(Data_dict['Day'][i] + "\t" + Data_dict['Time'][i] + "\t" +
                    str(Data_dict['X'][i]) + "\t" + str(Data_dict['Y'][i]) +
                    "\t" + Data_dict['Asleep'][i] + "\t"+ Data_dict['Behavior Mode'][i]
                    + "\t" + str(Data_dict['Distance'][i]) + "\n")

# write labels of contents
fw.writelines(New_Headers)

# create blank line between header block and next data section
fw.writelines("\n")

# write labels of contents
fw.writelines(New_Data_label)

# write contents of dictionary
fw.writelines(New_Data)

# close file
fw.close()