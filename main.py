from requests import get
from json import loads,dumps
import threading

namelist = []

def get_nickname(user_id):
    try:
        nickname = loads(get(f'https://api.codemao.cn/creation-tools/v1/user/center/honor?user_id={user_id}').text)['nickname']
        namelist.append(nickname)
        print(nickname+' '+str(user_id))
    except:
        pass

i = 10000
while i <= 19135000:
    threads = []
    for _ in range(100):
        thread = threading.Thread(target=get_nickname, args=(i,))
        threads.append(thread)
        thread.start()
        i += 1
    for thread in threads:
        thread.join()

# 保存到文件
with open('nickname.txt', 'w', encoding='utf-8') as f:
    f.write(dumps(namelist, ensure_ascii=False))
