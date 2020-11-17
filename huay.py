import requests
from bs4 import BeautifulSoup
import time
def vip():
    url = requests.get('https://www.huay.com/login')
    data = BeautifulSoup(url.content,'lxml')
    data1 = data.find_all('p',class_="number text-center m-0")
    a = data1[13:189]
    b = data1[189:415]
    a1 = [cat.string.strip() for cat in a]
    b1 = [rat.string.strip() for rat in b]
    a2 = [a1[i] for i in range(len(a1)) if 'x' not in a1[i]]
    a2t = [i for i in a2 if len(i) == 3]
    a2b = [i for i in a2 if len(i) == 2]
    b2 = [b1[i] for i in range(len(b1)) if 'x' not in b1[i]]
    b2t = [i for i in b2 if len(i) == 3]
    b2b = [i for i in b2 if len(i) == 2]
    return a2t,a2b,b2t,b2b
def score(m,n,s,t):
    s_line = ''
    s_line += '\n--------------------------\nผลหวยยี่กี่ : ห้องฟ้า\n--------------------------\n'
    if 0 < len(m) < 10 :
        for i in range(len(m)):
            s_line += str('รอบ {} บน : {}  ล่าง : {}\n'.format((i+1),m[i],n[i]))
        s_line += str('--------------------------\nผลหวยยี่กี่ VIP  : ห้องม่วง\n--------------------------\n')
        for i in range(len(s)):
            s_line += str('รอบ {} บน : {}  ล่าง : {}\n'.format((i + 1), s[i], t[i]))
    elif 9 < len(m) < 89:
        r = len(m)
        q = m[-10:]
        v = n[-10:]
        for j in range(10):
            s_line += str('รอบ {}  บน : {}  ล่าง : {}\n'.format(r-(9-j),q[j],v[j]))
        s_line += str('--------------------------\nผลหวยยี่กี่ VIP  : ห้องม่วง\n--------------------------\n')
        rt = len(s)
        qt = s[-10:]
        vt = t[-10:]
        for j in range(10):
            s_line += str('รอบ {}  บน : {}  ล่าง : {}\n'.format(rt-(9-j),qt[j],vt[j]))
    return s_line
def wait():
    wt = '------------------------\n  หมดเวลารอผลอีก 3 นาที    \n         ------------------------'
    return wt
def r_time():
    tm = time.localtime()
    hour = tm.tm_hour
    min = tm.tm_min
    sec = tm.tm_sec
    return hour,min,sec
def send(max):
    url = 'https://notify-api.line.me/api/notify'
    token = 'pjVpf1rLdsxIzhh4hyVHp293fhJcjGd9OnaFe6f7PM8'
    headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}
    msg = max
    r = requests.post(url, headers=headers, data={'message': msg})
    print(r.text)

if __name__ == '__main__':
    t_h = [0,1,2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    t_m = [15,30,45,0]
    while(True):
        h,m,s = r_time()
        if h in t_h :
            if m in t_m :
                w = wait()
                send(w)
                time.sleep(210)
                m, n, s, t = vip()
                q = score(m, n, s, t)
                send(q)
        else:
            time.sleep(20)
            continue
