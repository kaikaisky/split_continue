import  os



#Read file
def read_file(filename):
    health = []
    with open(filename, 'r', encoding= 'utf-8')as f:
        for person in f:
            if '姓名, 身高' in person:
                continue  #＃如果這字串有存在於這一行的話, 就執行continue, 這一迴圈的下面內容跳過

            name, height = person.strip().split(',') #split(‘,’) 遇到逗號就切割開來
                                            #strip() 會移除首行尾的空白及換行符號
            height = int(height)
            health.append([name, height])
            print([name], [height])
    return health 

#請輸入你的名字
#請輸入你的身高
#使用二維清單並讀取它

def user_input(health):
    while True:
        name = input('Please input your name or quit: ')
        if name == 'quit':
            break
        height = input('Please input your height(cm): ')
        height = int(height)
        health.append([name, height])
    return health

def print_health(health):
    #使用迴圈印出結果
    for person in health: #health 大清單 用person 這個變數讀取每一小組清單
        if  person[1] > 180: #Person[0] 表示Health 大清單裡面的所有小清單的第1個, 就是名字
            print('Hi,', person[0], 'Your height is', person[1], '. Do you want to join basketball team?')
        else:
                print('Hi,', person[0], 'Thanks for your help')


def write_file(filename, health):
    #寫入檔案, 如果是要寫中文, 編碼部份設定為utf-8
    with open(filename, 'w', encoding='utf-8') as f: #程式碼離開with 就會自動關閉你建立的文件
        f.write('姓名, 身高\n')
        for person in health:
            f.write(person[0] + ',' + str(person[1]) + '\n') ## 將身高 (person[1]) 轉換成字串 (str()) 才能和其它的字串拼接

def main(): 
    PROJECT_DIT = '/home/shikai/Desktop/codig/'
    os.chdir(PROJECT_DIT)

    filename = 'health2.csv'
    all_health = []
    if  os.path.isfile(filename): #＃os這個模組的path 模組的 isfile 功能,檢查檔案存在與否
        print('Get file')
        all_health = read_file(filename)
        #print(health)
        #print(health[1][1])
    else:
        print('File is not found')

    all_health = user_input(all_health)
    print_health(all_health)
    write_file('health2.csv', all_health)

main()


