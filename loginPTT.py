#coding:utf-8
import telnetlib
import sys
import account.Account  #My file. It contains Account.id, Account.password 
# from account.Account import Account
import time
print(account.Account.id)
tn = telnetlib.Telnet('ptt.cc')
time.sleep(1)
content = tn.read_very_eager().decode('big5','ignore').encode('utf-8')
print("Home page...")
if "請輸入代號" in content:
    print("Input account...")
    tn.write((account.Account.id+"\r\n").encode('utf8') )
    time.sleep(1)
    content = tn.read_very_eager().decode('big5','ignore').encode('utf-8')

    print("Input password...")
    tn.write((account.Account.password+"\r\n").encode('big5').encode('utf-8'))
    time.sleep(2)
    content = tn.read_very_eager().decode('big5','ignore').encode('utf-8')
    
    if "密碼不對" in content:
        print("incorrect password or incorrect account. Program End.").encode('utf8')
        sys.exit()
    if "您想刪除其他重複登入的連線嗎" in content:
        print("Do you want del another connect?...")
        tn.write("y\r\n".encode('big5').encode('utf-8') ) 
        time.sleep(7)
        content = tn.read_very_eager().decode('big5','ignore').encode('utf-8')
    #print(content)
    while "任意鍵" in content:
        print("Pass any key to continue...")
        tn.write("\r\n".encode('utf8') )
        time.sleep(2)
        content = tn.read_very_eager().decode('big5','ignore').encode('utf8')
        
    # if "要刪除以上錯誤嘗試" in content:
        # print("發現嘗試登入卻失敗資訊，是否刪除?(Y/N)：",end= "")
        # anser = input("")
        # tn.write((anser+"\r\n").encode('big5') )
        # time.sleep(1)
        # content = tn.read_very_eager().decode('big5','ignore')
    print("----------------------------------------------")
    print("----------- Login it's Done!--------------").encode('utf8')
    print("----------------------------------------------")
    # print(content)

    print("\n\n\n\n\n\n\n")
    print("----------------------------------------------")
    print("------------------- Logout!----------------------").encode('utf8')
    print("----------------------------------------------")
    tn.write("qqqqqqqqqg\r\ny\r\n".encode('utf8') )
    time.sleep(1)
    content = tn.read_very_eager().decode('big5','ignore').encode('utf-8')
    # print(content)
    tn.write("\r\n".encode('utf8') )
        
else:
    print("沒有可輸入帳號的欄位，網站可能掛了").encode('utf-8')