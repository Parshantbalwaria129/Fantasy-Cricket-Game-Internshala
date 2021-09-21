import sqlite3

crick = sqlite3.connect("final4.db")
curcrick = crick.cursor()
curcrick.execute("SELECT * FROM match;")
row  = curcrick.fetchall()

def calculate(row):
    points = 0.0
    runs = row[1]
    faced = row[2]
    four = row[3]
    six = row[4]
    bowled = row[5]
    maiden = row[6]
    given = row[7]
    wkts = row[8]
    catches = row[9]
    stumping = row[10]
    ro = row[11]
    try:
        strick_rate = float((runs/faced)*100)
    except:
        strick_rate = 0
    try:
        eco_rate = float(given/(bowled/6))
    except:
        eco_rate = 0

    #batsman points
    if strick_rate > 100:
        points += 4
    elif strick_rate >= 80:
        points += 2
    if runs >= 100:
        points += 10
    if runs >= 50:
        points += 5
    points = points + (int(four)*1) + (int(six)*2) + (float(runs)/2)

    #bowlers points
    if wkts >= 3:
        points += 5
    if wkts >= 5:
        points += 10
    if eco_rate <= 2:
        points +=10
    elif eco_rate <= 3.5:
        points += 7
    elif eco_rate <= 4.5:
        points += 4
    points += (wkts*10)

    #fielding
    points += ((catches+stumping+ro)*10)

    return points

players_and_points = {}
for i in row:
    players_and_points[i[0]] = calculate(i)
