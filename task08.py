def convertMinutes(minutes):
   h = minutes // 60
   m = minutes % 60
   if m > 1 and h > 1 :
      time_string = "{} hours,{} minutes".format(h,m)
   if m > 1 and h <= 1 :
      time_string = "{} hour,{} minutes".format(h,m)
   if m <= 1 and h > 1 :
      time_string = "{} hours,{} minute".format(h,m)
   if m <= 1 and h <= 1 :
      time_string = "{} hour,{} minute".format(h,m)
      
   return time_string
   
convertMinutes(123)
