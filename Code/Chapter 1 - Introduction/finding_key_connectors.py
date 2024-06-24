from __future__ import division  # use in case python 2.x

from dump_data import users


def number_of_friends(user):
    return len(user["friends"])


total_connections = sum(number_of_friends(user)
                        for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

sorted_number_friends_by_id = sorted(num_friends_by_id,
                                     key=lambda x: x[1],
                                     reverse=True)
if __name__ == '__main__':
    print(sorted_number_friends_by_id)
