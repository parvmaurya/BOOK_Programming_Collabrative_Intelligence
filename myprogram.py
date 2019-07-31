from recommendations import critics
from math import sqrt

def sim_distance(critics, person1, person2):
    dic_person1 = critics[person1]
    dic_person2 = critics[person2]
    names_common_movies = list(set(dic_person1.keys()) & set(dic_person2.keys()))
    #names_common_movies = intersection(dic_person1.keys(), dic_person2.keys())
    #print(dic_person1)
    #print(names_common_movies)
    #print(critics[person1][names_common_movies]-critics[person2][names_common_movies])
    
    score_list = [pow(abs(critics[person1][x]-critics[person2][x]),2) for x in names_common_movies]
    print(1/(1+sum(score_list)))
    
names_critics = critics.keys()
names_movies = critics[critics.keys()[0]].keys()

#print(critics.keys())
#print(critics[critics.keys()[0]].keys())

sim_distance(critics, 'Lisa Rose', 'Gene Seymour')

