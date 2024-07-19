import random

def create_teams(nTmCnt):
    alphabeth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    teams = []
    for i in range(nTmCnt):
        teams.append(alphabeth[i])
    return teams

def create_all_matches(teams):
    match = ''
    match_list = []
    for i in range(len(teams) - 1):
        for k in range(i + 1, len(teams)):
            match = teams[i] + '-' + teams[k]
            match_list.append(match)
    
    return match_list

# def create_matchday(match_list,match_count):
#     match_day = []
#     day_count = 0
#     teams_matched = '*'

#     for k in range(3):
#         for i in range(len(match_list)):
#             match = match_list[i]
#             if match[0] in teams_matched:
#                 match
#             elif match[2] in teams_matched:
#                 match            
#             else:
#                 match_day.append(match)
#                 teams_matched += match
#                 match_list[i] = '*'
#                 day_count += 1
#                 match_count += 1

#             if day_count == 5:
#                 return match_day, match_list, match_count
            
#     return match_day, match_list, match_count    

def create_matchday(match_list,match_count,not_played):
    match_day = []
    teams_matched = '*'

    if len(not_played) == 2:
        combined_match = not_played[0] + '-' + not_played[1]
        if combined_match in match_list:
            match_day.append(combined_match)
            teams_matched += combined_match
            index = match_list.index(combined_match)
            match_list[index] = '*'
            match_count += 1  
        else:
            for i  in range(len(match_list)):
                if not_played[0] in match_list[i]:
                    match_day.append(match_list[i])
                    teams_matched += match_list[i]
                    match_list[i] = '*'
                    match_count += 1                   
                    break

            for k  in range(len(match_list)):
                if not_played[1] in match_list[k]:
                    match = match_list[k]
                    if match[0] in teams_matched:
                        match
                    elif match[2] in teams_matched:
                        match
                    else:
                        match_day.append(match_list[k])
                        teams_matched += match_list[k]
                        match_list[k] = '*'
                        match_count += 1  
                        break
        
    elif len(not_played) == 1:
        match_count
    elif len(not_played) == 0:
        match_count

    for k in range(2):
        for i in range(len(match_list)):
            match = match_list[i]
            if match[0] in teams_matched:
                match
            elif match[2] in teams_matched:
                match            
            else:
                match_day.append(match)
                teams_matched += match
                match_list[i] = '*'
                match_count += 1

            if len(match_day) == 5:
                not_played = create_teams(12)
        
                # print(match_day)
                for match in match_day:
                    # print(match)
                    # print(not_played)
                    not_played.remove(match[0])
                    # print(match)
                    # print(not_played)
                    not_played.remove(match[2])

                return match_day, match_list, match_count, not_played
        
    for i in range(5-len(match_day)):
        match_day.append(' - ')

    teams_matched = '*'        

    return match_day, match_list, match_count, not_played      
    

def create_match_order(teams, match_list):
    match_order = []
    matches_played = {}
    for team_letter in teams:
        matches_played[team_letter] = 0
    match_count = 0
    random.shuffle(match_list)  

    match_day = []
    teams_matched = '*'

    for i in range(len(match_list)):
        match = match_list[i]
        if match[0] in teams_matched:
            match
        elif match[2] in teams_matched:
            match            
        else:
            match_day.append(match)
            teams_matched += match
            match_list[i] = '*'
            match_count += 1

        if len(match_day) == 5:
            break  

    not_played = teams.copy()
    
    for match in match_day:
        not_played.remove(match[0])
        not_played.remove(match[2])

    match_order += match_day

    while match_count < len(match_list):
        match_day, match_list, match_count, not_played = create_matchday(match_list,match_count,not_played)
        match_order += match_day

    return match_order


def create_schedule_file(match_order,nCrtCnt):
    line = ''
    line_length = 0

    with open('ww_schedule.txt', 'w') as file:
        for i in range(len(match_order)):
            line += match_order[i] + '   '
            line_length += 1
            if line_length == nCrtCnt:
                line += '\n'
                file.write(line)
                line = ''
                line_length = 0

        if line != '':
            line += ' -    '*(5-line_length)
            file.write(line)

def check_file():
    teams = create_teams(12)

    correct_schedule = True
    matches_played = {}

    for team_letter in teams:
        matches_played[team_letter] = 0

    with open('ww_schedule.txt', 'r') as file:
        most_played = 0 
        for line in file:
            teams = ''
            line = line.replace('-','')
            line = line.replace(' ','')
            line = line.replace('\n','')
            for team in line:
                if team in teams:
                    correct_schedule = False
                else:
                    teams += team
                    matches_played[team] += 1

            least_played = most_played
            for times_played in matches_played:
                if matches_played[times_played] > most_played:
                    most_played = matches_played[times_played]

                if matches_played[times_played] < least_played:
                    least_played = matches_played[times_played]

            if most_played - least_played > 1:
                correct_schedule = False
                print('false')

    if correct_schedule == False:
        main(12,5)

def main(teamcount, courtcount):
    teams = create_teams(teamcount)
    match_list = create_all_matches(teams)
    match_order = create_match_order(teams,match_list)

    create_schedule_file(match_order, courtcount)
    check_file()

main(12,5)

    

