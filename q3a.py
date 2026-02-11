def can_allocate_priority_seats(airplane_class: str, class_config: str, heroes: str) -> str:
    if airplane_class not in ('First', 'Business', 'Economy'):
        return 'Unrecognized class!'
    valid_configurations = {6: (1, 4),8: (2, 5),12: (3, 8)}
    if len(class_config) not in valid_configurations or class_config[valid_configurations[len(class_config)][0]] != '|' or class_config[valid_configurations[len(class_config)][1]] != '|':
        return 'Invalid seat configuration!'
    elif any(seat not in 'OX|' for seat in class_config):
        return 'Invalid seat letters!'
    class_length_match = {'First': 6,'Business': 8, 'Economy': 12}
    if class_length_match.get(airplane_class) != len(class_config):
        return "Mismatch between 'airplane_class' and 'seat_config'!"
    for j in heroes:
        if j not in ('T', 'B', 'A', 'D', 'S', 'N', 'C', 'L', 'H'):
            return 'Unrecognized hero, not allowed to board!'
    for hero in heroes:
        seat_assigned = False
        if hero == 'D':
            for i in range(len(class_config)):
                if class_config[i] == 'O' and (i % (len(class_config) // 3) == 0 or (i + 1) % (len(class_config) // 3) == 0):
                    class_config = class_config[:i] + 'D' + class_config[i + 1:]
                    seat_assigned = True
                    break
        elif hero == 'T':
            for i in [0, 5]:
                if class_config[i] == 'O' and airplane_class == 'First':
                    class_config = class_config[:i] + 'T' + class_config[i + 1:]
                    seat_assigned = True
                    break
        elif hero == 'B':
            for i in range(len(class_config) - 1):
                if class_config[i] == 'O' and class_config[i + 1] == '|':
                    class_config = class_config[:i] + 'B' + class_config[i + 1:]
                    seat_assigned = True
                    break
                elif class_config[i] == '|' and class_config[i + 1] == 'O':
                    class_config = class_config[:i] + 'B' + class_config[i + 1:]
                    seat_assigned = True
                    break
        elif hero == 'S':
            for i in range(len(class_config)):
                if class_config[i] == 'O' and airplane_class == 'Economy':
                    class_config = class_config[:i] + 'S' + class_config[i + 1:]
                    seat_assigned = True
                    break
        elif hero == 'N':
            for i in [0, len(class_config) - 1]:
                if class_config[i] == 'O':
                    class_config = class_config[:i] + 'N' + class_config[i + 1:]
                    seat_assigned = True
                    break
        elif hero == 'C':
            for i in range(len(class_config)):
                if class_config[i] == 'O':
                    class_config = class_config[:i] + 'C' + class_config[i + 1:]
                    seat_assigned = True
                    break
        elif hero == 'A':
            for i in range(1, len(class_config) - 1):
                if class_config[i] == 'O':
                    class_config = class_config[:i] + 'A' + class_config[i + 1:]
                    seat_assigned = True
                    break
        elif hero == 'L':
            for i in range(len(class_config)):
                row_start = (i // (len(class_config) // 3)) * (len(class_config) // 3)
                row_end = row_start + (len(class_config) // 3)
                if class_config[i] == 'O' and 'A' not in class_config[row_start:row_end]:
                    class_config = class_config[:i] + 'L' + class_config[i + 1:]
                    seat_assigned = True
                    break
        elif hero == 'H':
            for i in range(len(class_config)):
                if class_config[i] == 'O':
                    class_config = class_config[:i] + 'H' + class_config[i + 1:]
                    seat_assigned = True
                    break
        if not seat_assigned:
            return 'Boarding Denied!'
    return 'Yes, you may board!'