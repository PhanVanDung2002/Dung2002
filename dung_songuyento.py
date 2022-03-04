for a in range(2,100):
   for b in range(2,a): 
      if a%b == 0: 
         break 
   else: 
      print (a, 'là số nguyên tố')
