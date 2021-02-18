def convert(number): 
   
    hour = number/60
    minutes = number % 60
  
      
    return "%d:%02d" % (hour, minutes) 
      

n = 133
print(convert(n)) 
