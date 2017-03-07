import sqlite3

conn = sqlite3.connect('soccer-train.sqlite')
c = conn.cursor()
team_attributes = {}
for row in c.execute('SELECT team_api_id,buildUpPlaySpeedClass, buildUpPlayDribblingClass, buildUpPlayPassingClass, buildUpPlayPositioningClass, chanceCreationPassingClass, chanceCreationCrossingClass, chanceCreationShootingClass, chanceCreationPositioningClass, defencePressureClass, defenceAggressionClass, defenceTeamWidthClass, defenceDefenderLineClass from Team_Attributes') :
    if row[0] not in team_attributes : #Team didn't count before
        team_attributes[row[0]] = []
        team_attributes[row[0]].append({}) #Team buildUpPlaySpeedClass
        if row[1] not in team_attributes[row[0]][0] :
            team_attributes[row[0]][0][row[1]] = 1
        else :
            team_attributes[row[0]][0][row[1]] += 1
        team_attributes[row[0]].append({}) #buildUpPlayDribblingClass
        if row[2] not in team_attributes[row[0]][1] :
            team_attributes[row[0]][1][row[2]] = 1
        else :
            team_attributes[row[0]][1][row[2]] += 1
        team_attributes[row[0]].append({}) #buildUpPlayPassingClass
        if row[3] not in team_attributes[row[0]][2] :
            team_attributes[row[0]][2][row[3]] = 1
        else :
            team_attributes[row[0]][2][row[3]] += 1
        team_attributes[row[0]].append({}) #buildUpPlayPositioningClass
        if row[4] not in team_attributes[row[0]][3] :
            team_attributes[row[0]][3][row[4]] = 1
        else :
            team_attributes[row[0]][3][row[4]] += 1
        team_attributes[row[0]].append({}) #chanceCreationPassingClass
        if row[5] not in team_attributes[row[0]][4] :
            team_attributes[row[0]][4][row[5]] = 1
        else :
            team_attributes[row[0]][4][row[5]] += 1
        team_attributes[row[0]].append({}) #chanceCreationCrossingClass
        if row[6] not in team_attributes[row[0]][5] :
            team_attributes[row[0]][5][row[6]] = 1
        else :
            team_attributes[row[0]][5][row[6]] += 1
        team_attributes[row[0]].append({}) #chanceCreationShootingClass
        if row[7] not in team_attributes[row[0]][6] :
            team_attributes[row[0]][6][row[7]] = 1
        else :
            team_attributes[row[0]][6][row[7]] += 1
        team_attributes[row[0]].append({}) #chanceCreationPositioningClass
        if row[8] not in team_attributes[row[0]][7] :
            team_attributes[row[0]][7][row[8]] = 1
        else :
            team_attributes[row[0]][7][row[8]] += 1
        team_attributes[row[0]].append({}) #defencePressureClass
        if row[9] not in team_attributes[row[0]][8] :
            team_attributes[row[0]][8][row[9]] = 1
        else :
            team_attributes[row[0]][8][row[9]] += 1
        team_attributes[row[0]].append({}) #defenceAggressionClass
        if row[10] not in team_attributes[row[0]][9] :
            team_attributes[row[0]][9][row[10]] = 1
        else :
            team_attributes[row[0]][9][row[10]] += 1
        team_attributes[row[0]].append({}) #defenceTeamWidthClass
        if row[11] not in team_attributes[row[0]][10] :
            team_attributes[row[0]][10][row[11]] = 1
        else :
            team_attributes[row[0]][10][row[11]] += 1
        team_attributes[row[0]].append({}) #defenceDefenderLineClass
        if row[12] not in team_attributes[row[0]][11] :
            team_attributes[row[0]][11][row[12]] = 1
        else :
            team_attributes[row[0]][11][row[12]] += 1
    else :
        if row[1] not in team_attributes[row[0]][0] :
            team_attributes[row[0]][0][row[1]] = 1
        else :
            team_attributes[row[0]][0][row[1]] += 1
        if row[2] not in team_attributes[row[0]][1] :
            team_attributes[row[0]][1][row[2]] = 1
        else :
            team_attributes[row[0]][1][row[2]] += 1
        if row[3] not in team_attributes[row[0]][2] :
            team_attributes[row[0]][2][row[3]] = 1
        else :
            team_attributes[row[0]][2][row[3]] += 1
        if row[4] not in team_attributes[row[0]][3] :
            team_attributes[row[0]][3][row[4]] = 1
        else :
            team_attributes[row[0]][3][row[4]] += 1
        if row[5] not in team_attributes[row[0]][4] :
            team_attributes[row[0]][4][row[5]] = 1
        else :
            team_attributes[row[0]][4][row[5]] += 1
        if row[6] not in team_attributes[row[0]][5] :
            team_attributes[row[0]][5][row[6]] = 1
        else :
            team_attributes[row[0]][5][row[6]] += 1
        if row[7] not in team_attributes[row[0]][6] :
            team_attributes[row[0]][6][row[7]] = 1
        else :
            team_attributes[row[0]][6][row[7]] += 1
        if row[8] not in team_attributes[row[0]][7] :
            team_attributes[row[0]][7][row[8]] = 1
        else :
            team_attributes[row[0]][7][row[8]] += 1
        if row[9] not in team_attributes[row[0]][9] :
            team_attributes[row[0]][8][row[9]] = 1
        else :
            team_attributes[row[0]][8][row[9]] += 1
        if row[10] not in team_attributes[row[0]][9] :
            team_attributes[row[0]][9][row[10]] = 1
        else :
            team_attributes[row[0]][9][row[10]] += 1
        if row[11] not in team_attributes[row[0]][10] :
            team_attributes[row[0]][10][row[11]] = 1
        else :
            team_attributes[row[0]][10][row[11]] += 1
        if row[12] not in team_attributes[row[0]][11] :
            team_attributes[row[0]][11][row[12]] = 1
        else :
            team_attributes[row[0]][11][row[12]] += 1

#Calculate Prob
for row in c.execute('SELECT team_api_id,COUNT(buildUpPlaySpeedClass), COUNT(buildUpPlayDribblingClass), COUNT(buildUpPlayPassingClass), COUNT(buildUpPlayPositioningClass), COUNT(chanceCreationPassingClass), COUNT(chanceCreationCrossingClass), COUNT(chanceCreationShootingClass), COUNT(chanceCreationPositioningClass), COUNT(defencePressureClass), COUNT(defenceAggressionClass),COUNT( defenceTeamWidthClass), COUNT(defenceDefenderLineClass) from Team_Attributes GROUP BY team_api_id') :
    i = 1
    for attr in team_attributes[row[0]] :
        for key in attr :
            attr[key] /= row[i]
        i+=1

team_normal_style_attr = {}
for key in team_attributes :
    i = 0
    team_normal_style_attr[key] = []
    for row in team_attributes[key] :
        hightest = 0
        team_normal_style_attr[key].append('')
        for k in row :
            if row[k] > hightest :
                hightest = row[k]
                team_normal_style_attr[key][i] = k
        i += 1

for row in c.execute('SELECT Match.match_api_id AS match_api_id,Match.DATE AS DATE,Match.home_team_api_id AS home_team_api_id,Match.away_team_api_id AS away_team_api_id,Match.home_team_goal-Match.away_team_goal AS goal_diff,home_playSpd,home_playDrib,home_playPass,home_playPos,home_chancePass,home_chanceCross,home_chanceShoot,home_chancePos,home_defPress,home_defAgg,home_defWidth,home_defLine,away_playSpd,away_playDrib,away_playPass,away_playPos,away_chancePass,away_chanceCross,away_chanceShoot,away_chancePos,away_defPress,away_defAgg,away_defWidth,away_defLine FROM Match LEFT JOIN (SELECT home_match.match_api_id AS match_api_id,home_match.DATE AS DATE,home_match.home_team_api_id AS home_team_api_id,home_match.away_team_api_id AS away_team_api_id,home_match.goal_diff AS goal_diff,home_playSpd,home_playDrib,home_playPass,home_playPos,home_chancePass,home_chanceCross,home_chanceShoot,home_chancePos,home_defPress,home_defAgg,home_defWidth,home_defLine,away_playSpd,away_playDrib,away_playPass,away_playPos,away_chancePass,away_chanceCross,away_chanceShoot,away_chancePos,away_defPress,away_defAgg,away_defWidth,away_defLine FROM (SELECT match_api_id,MATCH.DATE AS DATE, home_team_api_id,away_team_api_id, home_team_goal-away_team_goal AS goal_diff,Home_Attr.buildUpPlaySpeedClass AS home_playSpd, Home_Attr.buildUpPlayDribblingClass AS home_playDrib, Home_Attr.buildUpPlayPassingClass AS home_playPass, Home_Attr.buildUpPlayPositioningClass AS home_playPos, Home_Attr.chanceCreationPassingClass AS home_chancePass, Home_Attr.chanceCreationCrossingClass AS home_chanceCross, Home_Attr.chanceCreationShootingClass AS home_chanceShoot, Home_Attr.chanceCreationPositioningClass AS home_chancePos, Home_Attr.defencePressureClass AS home_defPress, Home_Attr.defenceAggressionClass AS home_defAgg, Home_Attr.defenceTeamWidthClass AS home_defWidth, Home_Attr.defenceDefenderLineClass AS home_defLine FROM MATCH JOIN Team_Attributes AS Home_Attr ON MATCH.DATE = Home_Attr.DATE AND Home_Attr.team_api_id = home_team_api_id) AS home_match JOIN (SELECT match_api_id,MATCH.DATE AS DATE, home_team_api_id,away_team_api_id, home_team_goal-away_team_goal AS goal_diff,Away_attr.buildUpPlaySpeedClass AS away_playSpd, Away_attr.buildUpPlayDribblingClass AS away_playDrib, Away_attr.buildUpPlayPassingClass AS away_playPass, Away_attr.buildUpPlayPositioningClass AS away_playPos, Away_attr.chanceCreationPassingClass AS away_chancePass, Away_attr.chanceCreationCrossingClass AS away_chanceCross, Away_attr.chanceCreationShootingClass AS away_chanceShoot, Away_attr.chanceCreationPositioningClass AS away_chancePos, Away_attr.defencePressureClass AS away_defPress, Away_attr.defenceAggressionClass AS away_defAgg, Away_attr.defenceTeamWidthClass AS away_defWidth, Away_attr.defenceDefenderLineClass AS away_defLine FROM MATCH JOIN Team_Attributes AS Away_attr ON MATCH.DATE = Away_attr.DATE AND Away_attr.team_api_id = away_team_api_id) AS away_match ON home_match.match_api_id = away_match.match_api_id) AS Data ON Match.match_api_id = Data.match_api_id GROUP BY Match.match_api_id') :
    if row[5] is not None :
        print (row[5])
