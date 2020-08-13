# Login
class LoginException(Exception):
    def __init__(self, message) -> None:
        self.message = message

    def __str__(self) -> str:
        return '錯誤原因:' + self.message

users = [
    {'name':'john', 'password':'1234'},
    {'name':'admin', 'password':'4321'},
]

def loginCheck(u, p):
    # 先確認是否有找到帳號
    check = None
    for user in users:
        if user['name'] == u:
            check = True

    if not check:
        e = LoginException('查無此帳號')
        raise e  # 將錯誤物件拋出

    # 密碼是否正確
    check = None
    for user in users:
        if user['name'] == u and user['passwoud'] == p:
            check = True

    if not check:
        e = LoginException('密碼錯誤')
        raise e

    return check

if __name__ == '__main__':
    try:  # e被拋置這裡
        result = loginCheck('admin', '4321')
    except LoginException as e:
        print(e)
    else:
        print(result)