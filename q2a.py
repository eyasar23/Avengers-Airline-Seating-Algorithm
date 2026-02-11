def can_board_with_preference(total_avengers: int, seat_config: str, preference: str) -> str:
    empty = "O"
    occupied ="X"
    aisle= "|"
    char = empty + occupied + aisle 
    emp = seat_config.count(empty)
    
    for u in seat_config:
        if u not in char:
           return'Invalid seat letters!'
    
     
    
    if  len(seat_config) == 6 :
        if    preference == "W" :
              if [seat_config[0] , seat_config[-1]].count('O') >= total_avengers :
                  return 'Yes, you may board!'
              else :
                   return 'Boarding Denied!'
                  
        elif  preference == "M":
              return  'Invalid seat preference!'
        elif  preference == "A":
              if [seat_config[0],seat_config[2],seat_config[3],seat_config[5]].count('O') >= total_avengers :
                 return 'Yes, you may board!'
              else :
                  return 'Boarding Denied!'
               
                  
        elif  preference == "D":
              if [seat_config[0],seat_config[2],seat_config[3],seat_config[5]].count('O') >= total_avengers :
                 return 'Yes, you may board!'
              else :
                  return 'Boarding Denied!'
        else :
            return 'Invalid seat preference!'
    
    
    elif len(seat_config) == 12:
         if    preference == "W":
               if [seat_config[0] , seat_config[-1]].count('O') >= total_avengers :
                   return 'Yes, you may board!'
               else :
                    return 'Boarding Denied!'
     
        
     
         elif  preference == "M":
               if [seat_config[1],seat_config[5],seat_config[6],seat_config[10]].count('O') >= total_avengers :
                   return 'Yes, you may board!'
               else :
                    return 'Boarding Denied!'
         elif  preference == "A":
               if [seat_config[2],seat_config[4],seat_config[7],seat_config[9]].count('O') >= total_avengers :
                   return 'Yes, you may board!'
               else :
                    return 'Boarding Denied!'
         elif  preference == "D":
               if [seat_config[2],seat_config[4],seat_config[7],seat_config[9]].count('O') >= total_avengers :
                   return 'Yes, you may board!'
               else :
                    return 'Boarding Denied!'
         else :
             return 'Invalid seat preference!'
    
    
    elif len(seat_config) == 8:  
         if    preference == "W":
               if [seat_config[0] , seat_config[-1]].count('0') >= total_avengers :
                   return 'Yes, you may board!'
               else :
                    return 'Boarding Denied!'
         elif  preference == "M":
               return  'Invalid seat preference!'
         elif  preference == "A":
               if [seat_config[1],seat_config[3],seat_config[4],seat_config[6]].count('O') >= total_avengers :
                   return 'Yes, you may board!'
               else :
                    return 'Boarding Denied!'
     
                   
         elif  preference == "D":
              if [seat_config[1],seat_config[3],seat_config[4],seat_config[6]].count('O') >= total_avengers :
                  return 'Yes, you may board!'
              else :
                   return 'Boarding Denied!'
         else :
             return 'Invalid seat preference!'
        
    else:
         return 'Invalid seat configuration!'
print(can_board_with_preference(3, "OO|OO|OO", "A")) # Expected output: 'Yes, you may board!'



          

