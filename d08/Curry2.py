# admin 可得到指定100元
# hacker 可得到因登入失敗而得到0元
def login(alf):
    def sucess(mon):
        return 100 if mon > 100 else mon
    def fail(mon):
        return 0
    return sucess if alf == 'admin' else fail

print(login('admin')(100))
print(login('hacker')(100))