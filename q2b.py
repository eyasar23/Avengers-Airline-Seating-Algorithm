def show_preferred_seats(total_avengers: int, seat_config: str, preference: str) -> str:
    empty = "O"
    occupied = "X"
    aisle = "|"
    char = empty + occupied + aisle
    emp = seat_config.count(empty)

    
    for u in seat_config:
        if u not in char:
            return 'Invalid seat letters!'

    if len(seat_config) == 6:
        if preference == "W":
            if [seat_config[0], seat_config[-1]].count(empty) >= total_avengers:
                return str(seat_config[0], seat_config[-1]).replace("O", "H",total_avengers )
                 
            
            else:
                return 'Boarding Denied!'
        elif preference == "M":
            return 'Invalid seat preference!'
        elif preference == "A":
            if seat_config.count(empty) >= total_avengers:
                return 'Yes, you may board!'
            else:
                return 'Boarding Denied!'
        elif preference == "D":
            if seat_config.count(empty) >= total_avengers:
                return 'Yes, you may board!'
            else:
                return 'Boarding Denied!'
        else:
            return 'Invalid seat preference!'

    elif len(seat_config) == 12:
        if preference == "W":
            if [seat_config[0], seat_config[-1]].count(empty) >= total_avengers:
                seat_config = (
            seat_config[0].replace("O", "H") + 
            seat_config[1:-1] + 
            seat_config[-1].replace("O", "H")
        )
                return seat_config
            else:
                return 'Boarding Denied!'
        elif preference == "M":
            if [seat_config[5], seat_config[6],seat_config[10]].count(empty) >= total_avengers:
                seat_config = (seat_config[:5]+ seat_config[5].replace("O", "H")+ seat_config[6].replace("O", "H")+ seat_config[7:10]+seat_config[10].replace("O", "H")+ seat_config[11:])
                return seat_config
            else:
                return 'Boarding Denied!'
        elif preference == "A":
            if [seat_config[2], seat_config[4], seat_config[7], seat_config[9]].count(empty) >= total_avengers:
                return 'Yes, you may board!'
            else:
                return 'Boarding Denied!'
        elif preference == "D":
            if [seat_config[2], seat_config[4], seat_config[7], seat_config[9]].count(empty) >= total_avengers:
                seat_config = (seat_config[:2] + seat_config[2].replace("O", "D")+ seat_config[3:])
                return seat_config
                return 'Boarding Denied!'
        else:
            return 'Invalid seat preference!'

    elif len(seat_config) == 8:
        if preference == "W":
            if [seat_config[0], seat_config[-1]].count(empty) >= total_avengers:
                return 'Yes, you may board!'
            else:
                return 'Boarding Denied!'
        elif preference == "M":
            return 'Invalid seat preference!'
        elif preference == "A":
            if [seat_config[1], seat_config[3], seat_config[4], seat_config[6]].count(empty) >= total_avengers:
                count = 0
                new_seat_config = ""
                for i in range(len(seat_config)):
                    if i in [1, 3, 4, 6] and seat_config[i] == "O" and count < total_avengers:
                       new_seat_config += "H"  
                       count += 1
                    else:
                         new_seat_config += seat_config[i] 
                return new_seat_config
            else:
                return 'Boarding Denied!'
        elif preference == "D":
            if [seat_config[1], seat_config[3], seat_config[4], seat_config[6]].count(empty) >= total_avengers:
                return 'Yes, you may board!'
            else:
                return 'Boarding Denied!'
        else:
            return 'Invalid seat preference!'

    else:
        return 'Invalid seat configuration!'
