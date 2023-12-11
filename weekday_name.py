def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
def weekday(num):
  valid_nums = 1,2,3,4,5,6,7
  if num == 1:
   print ("sunday")
  if num == 2:
   print ("monday")
  if num == 3:
   print ("tuesday")
  if num == 4:
   print ("wednesday")
  if num == 5:
   print ("thursday")
  if num == 6:
   print ("friday")
  if num == 7:
   print ("saturday")
  if num not in valid_nums:
   print ("none")