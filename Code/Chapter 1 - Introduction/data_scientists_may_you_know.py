from dump_data import users


def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"]  # for each of user's friends
            for foaf in friend["friends"]]  # get each of _their_ friends


if __name__ == '__main__':
    print(friends_of_friend_ids_bad(users[0]))
