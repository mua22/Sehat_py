f1 = 'skmh.txt'
with open('skmh.txt','r') as f, open('Rubina.txt','a') as fs:
      
    for d in f:
      
       fs.write(d)

       if "TEST(s)" in d:
             break

           
#w.close

        

