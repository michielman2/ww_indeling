import random

def generate_teams(nTmCnt):
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

def create_match_order(teams, match_list):
    match_order = []
    teams_matched = '*' 
    all_matched = 0
    match_day = []
    match_count = 0
    random.shuffle(match_list)  

    while all_matched == 0:
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
                match_order += match_day
                print(match_day)
                match_day = []
                teams_matched = '*'
                break
            
        if len(match_day) > 0 & len(match_day) < 5:
            for i in range(5-len(match_day)):
                match_day.append(' - ')
                match_order += match_day
                match_day = []
                teams_matched = '*'

        print(match_count)

        if match_count == len(match_list):
            all_matched = 1
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

def check_file(teams):
    previous_teams = teams
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

            print(matches_played)
            print(least_played, most_played)

            if most_played - least_played > 2:
                correct_schedule = False
                print('false')

    if correct_schedule == False:
        main(12,5)

                
def main(nTmCnt, nCrCnt):
    teams = generate_teams(nTmCnt)
    match_list = create_all_matches(teams)
    match_order = create_match_order(teams,match_list)
    create_schedule_file(match_order, 5)
    check_file(teams)

main(12,5)


