with open('userinfo','r') as f:
    user_info=f.readlines()
    print(user_info)
    for line in user_info:
        #print(line)
        username=line.split(',')[0]
        passwd=line.split(',')[1]
        print(username,passwd)