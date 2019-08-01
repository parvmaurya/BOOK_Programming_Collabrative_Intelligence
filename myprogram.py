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
    return (1/(1+sum(score_list)))

def pearson_distance(critics, person1, person2):
    dic_person1 = critics[person1]
    dic_person2 = critics[person2]
    names_common_movies = list(set(dic_person1.keys()) & set(dic_person2.keys()))
    sum1 = sum([critics[person1][x] for x in names_common_movies])
    sum2 = sum([critics[person2][x] for x in names_common_movies])

    sum1_sqr = sum([pow(critics[person1][x],2) for x in names_common_movies])
    sum2_sqr = sum([pow(critics[person2][x],2) for x in names_common_movies])

    sum_prod = sum([critics[person1][x]*critics[person2][x] for x in names_common_movies])
    n = len(names_common_movies)
    num = sum_prod-((sum1*sum2)/n)
    den = sqrt((sum1_sqr-pow(sum1,2)/n) * (sum2_sqr-pow(sum2,2)/n))
    if den==0: return 0
    r = num/den
    return r

def top_matches(critics, person):
    scores = [(pearson_distance(critics,person,x),x) for x in critics.keys() if x!=person]
    scores.sort()
    scores.reverse()
    return scores
    
names_critics = critics.keys()
names_movies = critics[critics.keys()[0]].keys()

#print(critics.keys())
#print(critics[critics.keys()[0]].keys())

print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))
print(pearson_distance(critics, 'Lisa Rose', 'Gene Seymour'))
print(top_matches(critics, 'Toby'))

