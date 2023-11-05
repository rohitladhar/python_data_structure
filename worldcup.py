import random;
teams = ["India","Pakistan","South Africa","Australia","Bangladesh","Sri Lanka","Netherlands","Afghanistan","England","New Zealand"];
teamsLength = len(teams);
teamset = [];
for x in range(0,teamsLength):
    team = teams[x];
    for y in range(0,teamsLength):
        if(team!=teams[y]):
            elem = []
            elem.append(team);
            elem.append(teams[y]);
            teamset.append(sorted(elem));



output = []
for x in teamset:
    if x not in output:
        output.append(x)
random.shuffle(output)

for x in range(0,len(output)):
    result = str(x+1)+" of "+str(len(output))+" Match \n"+output[x][0]+" vs "+output[x][1]+"\n";
    print(result);
