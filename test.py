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

print (team_attributes)
