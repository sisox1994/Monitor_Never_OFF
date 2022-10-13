import pyautogui
import time
import random
import keyboard
import threading

def AutoDoSomthingToAvoidMonitorSleep():
    
    #pyautogui.click(clicks=1,interval=0.5,button='left')  # 自動按鈕
    #move_to_x = random.randint(1,100)
    #move_to_y = random.randint(1,100)
    #pyautogui.moveTo(now_mouse_pos_x,now_mouse_pos_y + y_diff ,duration=0.5)   # 隨機移動 鼠標
    pyautogui.press('esc')

    pass

def Sub():

    global Key_Detect_flag    
    Key_Detect_flag = False


    while True:
        if keyboard.get_hotkey_name():            
            Key_Detect_flag = True
            pass
        



if __name__ == '__main__':


    global Key_Detect_flag   

    t2 = threading.Thread(target=Sub)
    t2.setDaemon(True)
    t2.start()

    mouse_pos_x_compare = 0
    mouse_pos_y_compare = 0

    rolling = 0
    mouse_no_moving_cnt = 0
    y_diff = 1

    

    while(1):        
        # 取得現在 滑鼠座標 (X,Y)
        now_mouse_pos_x = pyautogui.position().x
        now_mouse_pos_y = pyautogui.position().y

        
        # 判斷鍵盤有沒有在操作

        if Key_Detect_flag == True:
            Key_Detect_flag = False
            
            mouse_no_moving_cnt = 0
            print("Clear Cnt")


        # 判斷滑鼠有沒有移動

        if( (mouse_pos_x_compare != now_mouse_pos_x) or (mouse_pos_y_compare != now_mouse_pos_y)):  #滑鼠 有移動

            mouse_pos_x_compare = now_mouse_pos_x
            mouse_pos_y_compare = now_mouse_pos_y
            mouse_no_moving_cnt = 0

            rolling += 1
            print("Clear Cnt")
            pass
 
        else:      # 滑鼠 沒有移動
            
           
            if(mouse_no_moving_cnt < 60 ): 
                mouse_no_moving_cnt += 1
                print("mouse no moving cnt:" + str(mouse_no_moving_cnt))
            else:
                 # 滑鼠 4分鐘 沒任何移動 
                mouse_no_moving_cnt = 0
                AutoDoSomthingToAvoidMonitorSleep()

                print("Auto Do Somthing To Avoid MonitorSleep!!")


        time.sleep(1.0)
        


