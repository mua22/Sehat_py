import re
import csv
import pymongo as pym
#import pandas as pd
list4 = []
list6 = []
list5 = []
list11= []

listn = ['WBC', 'RBC', 'HGB', 'HCT', 'HCV', 'MCH', 'MCHC', '%RDW-CV', 'PLT', 'MPV', '%Neut', '%LYMP', '%MONO', '%EOS', '%BASO', '#NEUT', '#LYMP', '#MONO', '#E0S', '#BASO']
listr = ['4-10', ' 3.8-4.8', ' 12-15', ' 36-46', ' 76-96', ' 27-32', ' 31.5-34.5', ' 11.5-14.5', ' 150-450', ' 7.2-11', ' 40-80', ' 20-40', ' 2-10', '1-10', '<1', '2-8', ' 1-5', '0.2-1', ' 002-.5', '0.002-0.1']
listu = ['x10.e3/ul', 'x10.e6/ul', ' g/dL', ' %', 'fL','pg' ,'g/dL', '%','x10.e3/ul', ' fL', ' %', ' %', ' %', ' %', '%', 'x10.e3/ul', 'x10.e3/ul', 'x10.e3/ul', 'x10.e3/ul', 'x10.e3/ul']
client = pym.MongoClient('mongodb://localhost:27017/')
db = client["CBC2"]
table1 = db["CC2"]
file = 'abc2.txt'
f1 = 'abc1.txt'
n = 0
st = " Test Name"




#while n < 21:
 #   list11.append(st)
  #  n = n+1




#otfile = open("Cbc.json", 'w')

mappings = ['TEST NAME','REFERENCE RANGE','UNIT','RESULT']
lis = []
list1 = []
list2 = []
list3 = []
lis1 = []
list11 = []
list22 = []
list33 = []

t = ()





name = " "
age = " "
phone = " "
date = " "
address = " "
with open(f1) as f:
    id = 1
    for d in f:
       li = list(d.strip().split(' '))
       #print(li[0])

       g = 0

       while g < len(li):
            if li[g] == 'Name' or  li[g] == 'Name:'or  li[g] == 'Name;':
               print(li[g])
               n
               h = 1
               while h < (len(li)) and li[h]!='In-house' and li[h]!='Referring' :
                   if li[h] != ':' and li[h]!= ';'and li[h]!= '=:':
                       #print(li[h])
                       name = name + " " + li[h]
                       

                       
                   h = h+1


            if li[g] == 'Age/Sex':
               #print(li[g])
               #print("yes")
               h = 1
               while h < (len(li)) and li[h]!='In-house'and li[h]!='Report':
                   age = age + " " + li[h]
                   print(age)
                   h = h + 1


            if li[g] == 'Phone':
               #print(li[g])
               # print("yes")
               h = 2
               while h < len(li):
                   phone = phone + " " + li[h]
                   h = h + 1

            
            if li[g] == 'Address' or li[g] == 'Address:':
               #print(li[g])
               # print("yes")
               h = 1
               while h < (len(li)-4) and li[h]!='Report':
                   address = address + " " + li[h]
                   h = h + 1



            if li[g] == 'Reported':
               #print(li[g])
               # print("yes")
               h = 1
               while h < len(li):
                   date = date + " " + li[h]
                   h = h + 1


            g = g+1



p = " "
with open(file) as fn:
    id = 1
    for d in fn:
       li = list(d.strip().split(' '))
       p = li[0]
       m = len(li)
       i=0

       if len(li) != 0:

           while i < 3 and li[i].isdigit() != True and li[i].replace('.', '', 1).isdigit() !=True:
               str = li[i]
               b = 1

               while b < 2 and li[b].isalpha()==True:
                   #print(li[b])
                   if li[b].isalpha() == True:
                       str = str+" "+ li[b]
                   #i = 2
                       #print(str)
                   b = b+1
               lis.append(str)


               i = i + 1

               i = 1

               while i < m-1:
                  if li[i].isdigit() == True or li[i].replace('.','',1).isdigit() == True:
                     if li[i+1] == '-':
                        #print(li[i+1])
                        str = li[i] + '' + li[i+1] + li[i+2]
                        #print(str)
                        list2.append(str)
                     if li[i] == 0-0.2:
                         print("yesss")
                         str = str+li[i]
                         list2.append(str)


                  x = re.findall("^\d-\d.\d|^\d-\d*|^\d.\d\d-\d|<1|^\d-\d.\d|^\d\d-\d\d|^\d.\d-\d|^\d\d\d\d|^\d\d\d-\d\d\d|^\d.\d-\d.\d|^\d\d-\d|^\d-\d\d|^\d-\d.\d|^0-0.2", li[i])
                  #print(list2)

                  if (x):
                      str1 = " "
                      for str in x:
                          print(str)
                          str1 = str1 + str
                      #print(str1)
                      list2.append(str1)
                  s = re.findall("^\s-\d.\d|^-\d.*|^-.\d",li[i])
                  if (s):
                    print("yesss")
                    strr = " "
                    strr1 = " "
                    for str in s:
                      print(str)
                      
                      strr1 = li[i-1] + str
                    print(strr1)
                    list2.append(strr1) 

                  t = re.findall("^\d\d.\d-|^\d.\d-\s",li[i])
                  if (t):
                   print("yesss")
                   strr2 = " "
                   strr3 = " "

                   for str in t:
                      print(str)
                      strr2 = strr2 + str
                      strr3 =  strr2+li[i+1] 
                   #print(strr3)
                   list2.append(strr3)
                   print(list2)



                  i = i+1
                  #print(len(list2))
                  #print(len(lis))

               if (len(lis)> len(list2)):
                   #print("yessss")
                   strn = " no range found"
                   list2.append(strn)
               i = 1
               while i < m:
                   if i != m-1:
                       if li[i].isdigit() == True or li[i].replace('.', '', 1).isdigit() == True:
                           if li[i + 1] != '-':
                               if li[i - 1] != '-':
                                 if len(li[i])<6:
                                   str = li[i]
                                   list1.append(str)
                                   break
                   else:
                       if li[i].isdigit() == True or li[i].replace('.', '', 1).isdigit() == True:
                           if i == m-1 and li[i-1] != '-':
                               str = li[i]
                               list1.append(str)
                   i = i + 1
               if (len(lis)> len(list1)):
                   strn = "value not found"
                   list1.append(strn)
               i = 1
               while i < m:
                   x = re.findall("%|fl|fL|pg|Pg|g/dl|g/dL|^g.*|^f.*",li[i])
                   b = re.findall("^x.*", li[i])

                   if (b):
                       if '6' in li[i+1]:
                           str2 = "x10.e6/ul"
                           list3.append(str2)
                       elif '3' in li[i+1]:

                           str2 = "x10.e3/ul"
                           list3.append(str2)
                       else:
                           str2 = "x10.e /ul"
                           list3.append(str2)
                   if (x):
                           strr = " "
                           for str in x:
                               str1 = strr + str
                               list3.append(str1)

                   i = i + 1
               #print(len(list2))
               #print(len(list3))
               if (len(lis)> len(list3)):
                   strn = "value not found"
                   list3.append(strn)
    j = 0
    k = 0
    list9 = []
    while i < len(lis):
        if "Hb" in lis[i]:
            lis[i] = "HGB"

        if "Total RBC" in lis[i]:
            lis[i] = "RBC"


        if "WBC Count" in lis[i]:
            lis[i] = "WBC"

        if "Neutrophils" in lis[i]:
            lis[i] = "%Neut"
        if "Lymphocytes" in lis[i]:
            lis[i] = "%LYMP"

        if "Monocytes" in lis[i]:
            lis[i] = "%MONO"

        i = i + 1
    
    #dict2 = {}
    #dict2["Patient Name"] = name
    #dict2["Patient Address"] = address
    #dict2["Patient Age"] = age
    #dict2["Date"] = date
    #dict2["Patient Contact"] = phone
    dict = {}
    while k < len(lis):


        #dict[mappings[j]] = lis[k]
        #dict[mappings[j + 1]] = list2[k]
        #dict[mappings[j + 2]] = list3[k]
        #dict[mappings[j + 3]] = list1[k]

        dict["Patient Name"] = name
        dict["Patient Address"] = address
        dict["Patient Age"] = age
        dict["Date"] = date
        dict["Patient Contact"] = phone



        #dict[list11[k] + "Test Name"] = lis[k]


        dict[lis[k] +" "+"Range"] = list2[k]
        dict[lis[k] +" "+"Unit"] = list3[k]

        dict[lis[k] +" "+"Result"] = list1[k]
        list9.append(dict)
        k = k + 1
#print(list9)



print(list1)
#print(lis)

#print(list2)
#print(list3)
#db.table.insert_one(dict)
print(dict) 







