import requests
from bs4 import BeautifulSoup
class Stat:
    def __init__(self):
        pass
    
    @staticmethod
    def vip(): # return (1)ห้องฟ้าสามตัวบน,(2)ห้องม่วงสามตัวบน
        url = requests.get('https://www.huay.com/login')
        data = BeautifulSoup(url.content,'lxml')
        data1 = data.find_all('p',class_="number text-center m-0")
        a = data1[13:193]
        b = data1[193:419]
        a1 = [cat.string.strip() for cat in a]
        b1 = [rat.string.strip() for rat in b]
        a2 = [a1[i] for i in range(len(a1)) if 'x' not in a1[i]]
        blue_top = [i for i in a2 if len(i) == 3] # ห้องฟ้า สามตัวบน
        b2 = [b1[i] for i in range(len(b1)) if 'x' not in b1[i]]
        purple_top = [i for i in b2 if len(i) == 3] # ห้องม่วง สามตัวบน
        return blue_top,purple_top

    @staticmethod
    def vip2(): # return (1)ห้องฟ้าสองตัวบน , (2)ห้องม่วงสองตัวบน
        url = requests.get('https://www.huay.com/login')
        data = BeautifulSoup(url.content,'lxml')
        data1 = data.find_all('p',class_="number text-center m-0")
        a = data1[13:193]
        b = data1[193:419]
        a1 = [cat.string.strip() for cat in a]
        b1 = [rat.string.strip() for rat in b]
        a2 = [a1[i] for i in range(len(a1)) if 'x' not in a1[i]]
        blue_top = [i for i in a2 if len(i) == 3] # ห้องฟ้า สามตัวบน
        blue_2 = [i[1]+i[2] for i in blue_top] # ห้องฟ้า สองตัวบน
        b2 = [b1[i] for i in range(len(b1)) if 'x' not in b1[i]]
        purple_top = [i for i in b2 if len(i) == 3] # ห้องม่วง สามตัวบน
        purple_2 = [i[1]+i[2] for i in purple_top] # ห้องม่วง สองตัวบน
        return blue_2,purple_2

    @staticmethod
    def vip2bottom(): #return (1)ห้องฟ้าสองตัวล่าง ,(2)ห้องม่วงสองตัวล่าง
        url = requests.get('https://www.huay.com/login')
        data = BeautifulSoup(url.content,'lxml')
        data1 = data.find_all('p',class_="number text-center m-0")
        a = data1[13:193]
        b = data1[193:419]
        a1 = [cat.string.strip() for cat in a]
        b1 = [rat.string.strip() for rat in b]
        a2 = [a1[i] for i in range(len(a1)) if 'x' not in a1[i]]
        blue_bottom = [i for i in a2 if len(i) == 2] # ห้องฟ้า สองตัวล่าง
        b2 = [b1[i] for i in range(len(b1)) if 'x' not in b1[i]]
        purple_bottom = [i for i in b2 if len(i) == 2] # ห้องม่วงสองตัวล่าง
        return blue_bottom,purple_bottom    

    @staticmethod
    def maxhuay(huay): # เลขที่มาบ่อยสุดตามลำดับรับค่าเป็น list ที่ได้ web scraping เป็น type list แล้ว
        zero = 0
        one = 0
        two = 0
        tree = 0
        four = 0
        five = 0
        six = 0
        seven = 0
        eight = 0
        night = 0
        for i in huay:
            for j in i:
                if j == '0':
                    zero += 1
                elif j == '1':
                    one += 1
                elif j == '2':
                    two += 1
                elif j == '3':
                    tree += 1
                elif j == '4':
                    four += 1
                elif j == '5':
                    five += 1
                elif j == '6':
                    six += 1
                elif j == '7':
                    seven += 1
                elif j == '8':
                    eight += 1
                elif j == '9':
                    night += 1
                else:
                    continue
        outcome = {'zero':zero,'one':one,'two':two,'tree':tree,'four':four,'five':five,'six':six,'seven':seven,'eight':eight,'night':night}
        return outcome

    @staticmethod
    def timeline(checklist,num): # ตรวจสอบtimelineการออกของเลข checklist=ชุดตัวเลขที่ต้องการตรวจสอบ(type=list) num = เลขที่ต้องการตรวจสอบ(กรอกแค่ตัวเดียว type=int)
        number = str(num)
        line = []
        for i in range(len(checklist)):
            if number in checklist[i]:
                line.append('1')
            else:
                line.append('0')
        return line

    @staticmethod
    def num_repeat(checklist): # เลขเบิ้ล เลขหาม checklist= ชุดเลขสามตัวหรือสองตัว type=list
        if len(checklist[0]) == 3 :
            tree = []
            for i in checklist:
                if i[0] == i[1] or i[0] == i[2] or i[1] == i[2] :
                    tree.append('1')
                else:
                    tree.append('0')
            return tree
        elif len(checklist[0]) == 2 :
            two = []
            for j in checklist:
                if j[0] == j[1] :
                    two.append('1')
                else:
                    two.append('0')
            return two



    
