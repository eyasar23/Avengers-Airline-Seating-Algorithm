def can_assemble(total_avengers: int, seat_config: str) -> str:
    empty = "O"
    occupied ="X"
    aisle= "|"
    char = empty + occupied + aisle 
    emp = seat_config.count(empty)
    
    for u in seat_config:
        if u not in char:
           return'Invalid seat letters!'
    
    if  len(seat_config) in [12,6,8]  :
        if emp >= total_avengers:
           return 'Yes, you may board!'
        else :
             return 'Boarding Denied!'
    else :
           return 'Invalid seat configuration!'
        


    