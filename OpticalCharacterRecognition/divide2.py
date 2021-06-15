f1 = 'skmh.txt'
brak = False
with open('skmh.txt','r') as f, open('Rubina1.txt','a') as fs:
      
    for d in f:
      

       if "TEST(s)" in d:
           brak = True
       if brak==True:
          if "TEST(s)" in d:
               continue
          elif "Note" in d:
              break
          else:
                fs.write(d)


           
#w.close

        

