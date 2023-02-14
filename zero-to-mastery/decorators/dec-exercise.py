# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user = {
#     'name': 'Sorna',
#     'valid': False
# }


# def authenticated(fn):
#     def wrapper(*args, **kwargs):
#         print(args[0]['valid'])
#         if args[0]['valid']:
#             return fn(*args, **kwargs)
#         else:
#             print('User not authenticated')
#     return wrapper


# @authenticated
# def message_friends(user):
#     print('message has been sent')


# message_friends(user)


users = {
    'user1': {
        'name': 'Sorna',
        'valid': False
    },
    'user2': {
        'name': 'Anje',
        'valid': True
    }
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['user2']['valid']:
            return fn(*args, **kwargs)
        else:
            print('User not authenticated')
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(users)
