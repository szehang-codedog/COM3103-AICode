nominated = {
    2013: ["Tony Leung Ka-fai", "Nick Cheung", "Chapman To", "Sean Lau", "Tony Leung Chiu-Wai"],
    2014: ["Nick Cheung", "Tony Leung Chiu-Wai", "Louis Koo", "Sean Lau", "Anthony Wong"],
    2015: ["Sean Lau", "Eddie Peng", "Sean Lau", "Huang Bo", "Daniel Wu"],
    2016: ["Aaron Kwok", "Andy Lau", "Nick Cheung", "Tony Leung Ka-fai", "Jacky Cheung"],
    2017: ["Gordon Lam", "Shawn Yue", "Francis Ng", "Richie Jen", "Tony Leung Ka-fai"]}

actor_freq={}
most_nom_actor = []
for nomin_year in nominated:
    for count in nominated[nomin_year]:
        if count not in actor_freq:
            actor_freq[count] = 1
        else:
            actor_freq[count] +=1

max = 0
for i in actor_freq:
    print("{} : {}".format(i, actor_freq[i]))
    if actor_freq[i] > max:
        max = actor_freq[i]
        
for actor in actor_freq:
    if actor_freq[actor] == max:
        most_nom_actor.append(actor)

print("most_nom_actor = {}".format(most_nom_actor))
input()
