#Read file.csv
health = []
with open('/home/shikai/Desktop/codig/health2.csv', 'r', encoding= 'utf-8')as f:
    for person in f:
        if '姓名, 身高' in person:
            continue  #＃如果這字串有存在於這一行的話, 就執行continue, 這一迴圈的下面內容跳過

        name, height = person.strip().split(',') #split(‘,’) 遇到逗號就切割開來
                                      #strip() 會移除首行尾的空白及換行符號
        health.append([name, height])
        print([name])
print(health)
print(health[1][1])
        

#請輸入你的名字
#請輸入你的身高
#使用二維清單並讀取它


health = []
while True:
    name = input('Please input your name or quit: ')
    if name == 'quit':
        break
    height = input('Please input your height(cm): ')
    height = int(height)
    health.append([name, height])

#使用迴圈印出結果
for person in health: #health 大清單 用person 這個變數讀取每一小組清單
    if  person[1] > 180: #Person[0] 表示Health 大清單裡面的所有小清單的第1個, 就是名字
        print('Hi,', person[0], 'Your height is', person[1], '. Do you want to join basketball team?')
    else:
        print('Thanks for your help')


#寫入檔案, 如果是要寫中文, 編碼部份設定為utf-8
with open('/home/shikai/Desktop/codig/health2.csv', 'w', encoding='utf-8') as f: #程式碼離開with 就會自動關閉你建立的文件
    f.write('姓名, 身高\n')
    for person in health:
        f.write(person[0] + ',' + str(person[1]) + '\n') ## 將身高 (person[1]) 轉換成字串 (str()) 才能和其它的字串拼接


