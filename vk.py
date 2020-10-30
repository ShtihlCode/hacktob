import vk
from getpass import getpass


APP_ID = 6034630


def get_user_login():
    user_login = input('Enter your login: ')
    return user_login


def get_user_password():
    user_password = getpass('Enter your password: ')
    return user_password


def create_session(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    return api


def get_friends_info(session):
    friends_ids = session.friends.getOnline()
    friends_info = session.users.get(user_ids=friends_ids)
    return friends_info


def output_friends_to_console(friends_info):
    print('Now online:\n')
    for friends in friends_info:
        print('{} {}'.format(friends['first_name'], friends['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    vk_session = create_session(login, password)
    user_friends_info = get_friends_info(vk_session)
    output_friends_to_console(user_friends_info)