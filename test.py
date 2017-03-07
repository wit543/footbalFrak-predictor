import sqlite3,random

conn = sqlite3.connect('soccer-train.sqlite')
c = conn.cursor()
team_attributes = {}
for row in c.execute('SELECT team_api_id,buildUpPlaySpeedClass, buildUpPlayDribblingClass, buildUpPlayPassingClass, buildUpPlayPositioningClass, chanceCreationPassingClass, chanceCreationCrossingClass, chanceCreationShootingClass, chanceCreationPositioningClass, defencePressureClass, defenceAggressionClass, defenceTeamWidthClass, defenceDefenderLineClass from Team_Attributes') :
    if row[0] not in team_attributes : #Team didn't count before
        team_attributes[row[0]] = []
        for i in range(0,12) :
            team_attributes[row[0]].append({})
    for i in range(0,12) :
        if (row[i+1] not in team_attributes[row[0]][i]) :
            team_attributes[row[0]][i][row[i+1]] = 1
        else :
            team_attributes[row[0]][i][row[i+1]] += 1
#
# #Calculate Prob
# for row in c.execute('SELECT team_api_id,COUNT(buildUpPlaySpeedClass), COUNT(buildUpPlayDribblingClass), COUNT(buildUpPlayPassingClass), COUNT(buildUpPlayPositioningClass), COUNT(chanceCreationPassingClass), COUNT(chanceCreationCrossingClass), COUNT(chanceCreationShootingClass), COUNT(chanceCreationPositioningClass), COUNT(defencePressureClass), COUNT(defenceAggressionClass),COUNT( defenceTeamWidthClass), COUNT(defenceDefenderLineClass) from Team_Attributes GROUP BY team_api_id') :
#     i = 1
#     for attr in team_attributes[row[0]] :
#         for key in attr :
#             attr[key] /= row[i]
#         i+=1
#
# team_normal_style_attr = {}
# for key in team_attributes :
#     i = 0
#     team_normal_style_attr[key] = []
#     for row in team_attributes[key] :
#         hightest = 0
#         team_normal_style_attr[key].append('')
#         for k in row :
#             if row[k] > hightest :
#                 hightest = row[k]
#                 team_normal_style_attr[key][i] = k
#         i += 1
#
# match_prob = {}
# for row in c.execute('SELECT Match.match_api_id AS match_api_id,Match.home_team_api_id AS home_team_api_id,Match.away_team_api_id AS away_team_api_id,Match.home_team_goal-Match.away_team_goal AS goal_diff,home_playSpd,home_playDrib,home_playPass,home_playPos,home_chancePass,home_chanceCross,home_chanceShoot,home_chancePos,home_defPress,home_defAgg,home_defWidth,home_defLine,away_playSpd,away_playDrib,away_playPass,away_playPos,away_chancePass,away_chanceCross,away_chanceShoot,away_chancePos,away_defPress,away_defAgg,away_defWidth,away_defLine FROM Match LEFT JOIN (SELECT home_match.match_api_id AS match_api_id,home_match.DATE AS DATE,home_match.home_team_api_id AS home_team_api_id,home_match.away_team_api_id AS away_team_api_id,home_match.goal_diff AS goal_diff,home_playSpd,home_playDrib,home_playPass,home_playPos,home_chancePass,home_chanceCross,home_chanceShoot,home_chancePos,home_defPress,home_defAgg,home_defWidth,home_defLine,away_playSpd,away_playDrib,away_playPass,away_playPos,away_chancePass,away_chanceCross,away_chanceShoot,away_chancePos,away_defPress,away_defAgg,away_defWidth,away_defLine FROM (SELECT match_api_id,MATCH.DATE AS DATE, home_team_api_id,away_team_api_id, home_team_goal-away_team_goal AS goal_diff,Home_Attr.buildUpPlaySpeedClass AS home_playSpd, Home_Attr.buildUpPlayDribblingClass AS home_playDrib, Home_Attr.buildUpPlayPassingClass AS home_playPass, Home_Attr.buildUpPlayPositioningClass AS home_playPos, Home_Attr.chanceCreationPassingClass AS home_chancePass, Home_Attr.chanceCreationCrossingClass AS home_chanceCross, Home_Attr.chanceCreationShootingClass AS home_chanceShoot, Home_Attr.chanceCreationPositioningClass AS home_chancePos, Home_Attr.defencePressureClass AS home_defPress, Home_Attr.defenceAggressionClass AS home_defAgg, Home_Attr.defenceTeamWidthClass AS home_defWidth, Home_Attr.defenceDefenderLineClass AS home_defLine FROM MATCH JOIN Team_Attributes AS Home_Attr ON MATCH.DATE = Home_Attr.DATE AND Home_Attr.team_api_id = home_team_api_id) AS home_match JOIN (SELECT match_api_id,MATCH.DATE AS DATE, home_team_api_id,away_team_api_id, home_team_goal-away_team_goal AS goal_diff,Away_attr.buildUpPlaySpeedClass AS away_playSpd, Away_attr.buildUpPlayDribblingClass AS away_playDrib, Away_attr.buildUpPlayPassingClass AS away_playPass, Away_attr.buildUpPlayPositioningClass AS away_playPos, Away_attr.chanceCreationPassingClass AS away_chancePass, Away_attr.chanceCreationCrossingClass AS away_chanceCross, Away_attr.chanceCreationShootingClass AS away_chanceShoot, Away_attr.chanceCreationPositioningClass AS away_chancePos, Away_attr.defencePressureClass AS away_defPress, Away_attr.defenceAggressionClass AS away_defAgg, Away_attr.defenceTeamWidthClass AS away_defWidth, Away_attr.defenceDefenderLineClass AS away_defLine FROM MATCH JOIN Team_Attributes AS Away_attr ON MATCH.DATE = Away_attr.DATE AND Away_attr.team_api_id = away_team_api_id) AS away_match ON home_match.match_api_id = away_match.match_api_id) AS Data ON Match.match_api_id = Data.match_api_id GROUP BY Match.match_api_id') :
#     result = ''
#     if row[3] > 0 :
#         result = 'W'
#     elif row[3] == 0 :
#         result = 'D'
#     else :
#         result = 'L'
#     if result not in match_prob :
#         match_prob[result] = []
#     if len(match_prob[result]) == 0 :
#         for i in range(0,24) :
#             match_prob[result].append({})
#     home_playSpd = row[4]
#     home_playDrib = row[5]
#     home_playPass = row[6]
#     home_playPos = row[7]
#     home_chancePass = row[8]
#     home_chanceCross = row[9]
#     home_chanceShoot = row[10]
#     home_chancePos = row[11]
#     home_defPress = row[12]
#     home_defAgg = row[13]
#     home_defWidth = row[14]
#     home_defLine = row[15]
#     away_playSpd = row[16]
#     away_playDrib = row[17]
#     away_playPass = row[18]
#     away_playPos = row[19]
#     away_chancePass = row[20]
#     away_chanceCross = row[21]
#     away_chanceShoot = row[22]
#     away_chancePos = row[23]
#     away_defPress = row[24]
#     away_defAgg = row[25]
#     away_defWidth = row[26]
#     away_defLine = row[27]
