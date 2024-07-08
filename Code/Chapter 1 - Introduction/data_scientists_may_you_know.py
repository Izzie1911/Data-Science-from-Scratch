from dump_data import users, interests
from collections import Counter
from collections import defaultdict

def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"]  # for each of user's friends
            for foaf in friend["friends"]]  # get each of _their_ friends

def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user)
        for friend in user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
        for friend in user["friends"]  # for each of my friends
        for foaf in friend["friends"]  # count *their* friends
        if not_the_same(user, foaf)  # who aren't me
        and not_friends(user, foaf))  # and aren't my friends

def data_scientists_who_like(target_interest):
    return [user_id
        for user_id, user_interest in interests
        if user_interest == target_interest]




if __name__ == '__main__':
    print(friends_of_friend_ids(users[3]))  # Counter({0: 2, 5: 1})
    print(data_scientists_who_like("Hadoop"))
    user_ids_by_interest = defaultdict(list)
    for user_id, interest in interests:
        user_ids_by_interest[interest].append(user_id)

    interests_by_user_id = defaultdict(list)
    for user_id, interest in interests:
        interests_by_user_id[user_id].append(interest)
    def most_common_interests_with(user):
        return Counter(interested_user_id
                       for interest in interests_by_user_id[user["id"]]
                       for interested_user_id in user_ids_by_interest[interest]
                       if interested_user_id != user["id"])
    print(most_common_interests_with(users[0]))