
import pyautogui as pg
import time
import asyncio
import text_cleaner
import find_diff 


flag = True
browser_flag = True

async def log():
    while True:
        print(pg.position())
        await asyncio.sleep(0.5)
    
    #click this position: Point(x=965, y=1059)

def close_browser():
    global browser_flag
    if browser_flag:
        pg.moveTo(965, 1060,0.2)
        pg.click()
        browser_flag = False
    pg.moveTo(1895, 15, 0.2)
    pg.click()

def write_users(name):
    global flag
    pg.moveTo(1295, 1054, 0.2)
    pg.click()
    if name == "followers" and flag:
        pg.moveTo(120, 385, 0.2)
        pg.click()
        flag = False
        
    elif name == "followees" and flag:
        pg.moveTo(120, 360, 0.2)
        pg.click()
        flag = False
    pg.moveTo(600, 250)
    pg.click()
    pg.press('Enter')
    pg.hotkey('ctrl', 'v')
    time.sleep(0.2)
    
    pg.hotkey('ctrl', 's')
    pg.moveTo(965, 1060,0.1)
    pg.click()


def get_users(target, param):

    if target == "followers":
        delta = 0
        start_time = time.time()
        while (delta < param):
            time.sleep(0.1)
            pg.moveTo(735,365, 0.1)
            pg.click()
            pg.rightClick()
            pg.moveTo(813, 833, 0.2)
            pg.click()
            pg.mouseDown(x=790, y=715, button='left')
            time.sleep(0.1)
            pg.mouseUp(x=893, y=395, button='left')
            pg.moveTo(946,432, 0.2)
            pg.click()
            write_users(target)
            pg.moveTo(900,600,0.1)
            pg.scroll(-720)
            end_time = time.time()
            delta = end_time - start_time
            print("time remaining -->" +str(param- delta))
        close_browser()
        return None
    elif target == "followees":
        delta = 0
        start_time = time.time()
        time.sleep(0.1)
        while (delta < param):
            pg.moveTo(735,365, 0.1)
            pg.click()
            pg.rightClick()
            pg.moveTo(813, 833, 0.2)
            pg.click()
            pg.mouseDown(x=863, y=723,  button='left')
            time.sleep(0.1)
            pg.mouseUp(x=790, y=440, button='left')
            pg.moveTo(842,473, 0.2)
            pg.click()
            write_users(target)
            pg.moveTo(900,600,0.1)
            pg.scroll(-600)
            end_time = time.time()
            delta = end_time - start_time
            print("time remaining -->" +str(param- delta))
        close_browser()
        return None
        
    

def click_followers():
    time.sleep(2)
    pg.moveTo(1035, 170)
    time.sleep(0.1)
    pg.click()
    time.sleep(0.5)

def click_followees():
    time.sleep(2)
    pg.moveTo(1150, 170)
    time.sleep(0.1)
    pg.click()
    time.sleep(0.5)

def main(target, param):
    pg.moveTo(965, 1060,0.1)
    pg.click()
    time.sleep(2)
    pg.write("https://instagram.com")
    pg.press("Enter")
    time.sleep(5)
    
    pg.moveTo(1270, 150, 0.1)
    pg.click()
    time.sleep(0.1)
    if target == "followers":
        click_followers()
    elif target == "followees":
        click_followees()
    else:
        print("Wrong target. please try again.")
    get_users(target, param)


param1 = 0
param2 = 0

def menu():
    global param1, param2
    data1 = int(input("Enter your following count:\n"))
    data2 = int(input("Enter your followers count:\n"))
    data1 = data1 * 1.06
    data2 = data2 * 1.06
    total_time = data1 + data2 + 2*(7.6 + 2.6) + 0.8 + 0.2
    print(str(total_time))
    param2 = data2
    param1 = data1
    



def scraping():
    global flag
    print("scraping on following.")
    main(target="followers", param=param1)
    flag = True
    print("scraping on followers.")
    main(target="followees", param=param2)
    

def analysis():
    text_cleaner.start("ytest.txt")
    text_cleaner.start("ztest.txt")
    find_diff.sorting("ztest.txt")
    find_diff.sorting("ytest.txt")
    find_diff.get_my_unfollowers("zztest.txt", "zytest.txt")

def run():
    close_browser()
    menu()
    scraping()
    analysis()

run()
pg.moveTo(1150, 170)
asyncio.run(log())