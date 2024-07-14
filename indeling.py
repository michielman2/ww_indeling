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
    random.shuffle(match_list)  

    while all_matched == 0:
        for i in range(len(match_list)):
            match = match_list[i]
            if match[0] in teams_matched:
                match
            elif match[2] in teams_matched:
                match            
            else:
                match_order.append(match)
                teams_matched += match
                match_list[i] = '*'

        teams_matched = '*'
        if len(match_order) == len(match_list):
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

def check_file():
    with open('ww_schedule.txt', 'r') as file:
        for line in file:
            teams = ''
            line = line.replace('-','')
            line = line.replace(' ','')
            for team in line:
                if team in teams:
                    print('false')
                else:
                    teams += team


    
teams = generate_teams(12)
match_list = create_all_matches(teams)
match_order = create_match_order(teams,match_list)
print(len(match_order))
create_schedule_file(match_order, 5)
check_file()

