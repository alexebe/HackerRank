import itertools

# Complete the acmTeam function below.
def acmTeam(n, topic):
    max_topic = 0
    nb_team_with_max_knowledge = 0
    couples = list(itertools.combinations(range(n), 2))
    for c in couples:
        total_knowledge = int(topic[c[0]]) + int(topic[c[1]])
        str_total_knowledge = str(total_knowledge).replace("0","")
        if(len(str_total_knowledge) > max_topic):
            max_topic = len(str_total_knowledge)
            nb_team_with_max_knowledge = 1
        elif(len(str_total_knowledge) == max_topic):    
            nb_team_with_max_knowledge += 1
        
    return max_topic, nb_team_with_max_knowledge
