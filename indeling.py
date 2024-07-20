import random
import sys

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

def fix_home_away(match_list, teams):
    matches_home = {}
    
    lowest_home_count = 5

    for x in range(16):

      for team in teams:
         matches_home[team] = 0

      for match in match_list:
         matches_home[match[0]] += 1
      
      lowest_home_count = 100
      for team in matches_home:
         if matches_home[team] < lowest_home_count:
               lowest_home_count = matches_home[team]
               lowest_home_team = team

      for i in range(len(match_list)):
         match = match_list[i]
         if match[2] == lowest_home_team:
               new_match = match[2] + '-' + match[0]
               match_list[i] = new_match
               break
    print(matches_home)

    return match_list
        
        

def create_matchday(match_list,match_count,not_played):
    match_day = []
    teams_matched = '*'
    random.shuffle(match_list)

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
      for i  in range(len(match_list)):
            if not_played[0] in match_list[i]:
               match_day.append(match_list[i])
               teams_matched += match_list[i]
               match_list[i] = '*'
               match_count += 1                   
               break
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
        matches_played[match[0]] += 1
        matches_played[match[2]] += 1

    if len(match_day) < 5:
      for i in range(5-len(match_day)):
         match_day.append(' - ')    

    match_order += match_day

    print(match_day)
   

    complete = False
    while complete == False:
        viable_day = False
        while viable_day == False:
            matches_played_copy = matches_played.copy()
            match_list_copy = match_list.copy()

            match_day, match_list, match_count, not_played = create_matchday(match_list,match_count,not_played)

            for match in match_day:
                  if match != ' - ':
                     matches_played[match[0]] += 1
                     matches_played[match[2]] += 1

            least_played = 100
            most_played = 0

            for times_played in matches_played:
                  if matches_played[times_played] > most_played:
                     most_played = matches_played[times_played]

                  if matches_played[times_played] < least_played:
                     least_played = matches_played[times_played]

            if most_played - least_played > 1:
                  match_count -= 5
                  matches_played = matches_played_copy.copy()
                  match_list = match_list_copy.copy()
            else:
                  viable_day = True
            if match_day[0] == ' - ':
                complete = True
                match_day = []      

        match_order += match_day
        print(match_day)
        print(least_played,most_played)

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


def main(teamcount, courtcount):
    teams = create_teams(teamcount)
    match_list = create_all_matches(teams)
    match_list = fix_home_away(match_list, teams)
    match_order = create_match_order(teams,match_list)

    create_schedule_file(match_order, courtcount)

main(int(sys.argv[1]),int(sys.argv[2]))

    
