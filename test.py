import sqlite3

conn = sqlite3.connect('soccer-train.sqlite')
c = conn.cursor()
team_attributes = {}
for row in c.execute('SELECT team_api_id,buildUpPlaySpeedClass, buildUpPlayDribblingClass, buildUpPlayPassingClass, buildUpPlayPositioningClass, chanceCreationPassingClass, chanceCreationCrossingClass, chanceCreationShootingClass, chanceCreationPositioningClass, defencePressureClass, defenceAggressionClass, defenceTeamWidthClass, defenceDefenderLineClass from Team_Attributes') :
    print (row)
