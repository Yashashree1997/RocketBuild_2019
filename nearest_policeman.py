from haversine import haversine

user = (45.7597, 4.8422) # (lat, lon) of user who reports the incident 
police = [(45.7697, 4.8522), (45.7797, 4.8722), (45.7997, 4.8722), (45.7697, 4.8622)] # (lat ,lon) of all the policemen
    
def nearest_policeman(user, police) :
    distance = []
    for p in police :
        x = haversine(user, p)
        distance.append(x)
    print("Minimum distance :", min(distance), " Police with id :", distance.index(min(distance)), "has to be notified")
    return (min(distance), distance.index(min(distance)))