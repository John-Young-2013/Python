#!/usr/bin/evn python

USER_FILE = 'user'
def lock(user,isture):
    write_list = []
    with open(USER_FILE, 'r') as f:
        for line in f:
            usr,pas,lock = line.split('\n')[0].split(',')
            if isture == True and usr == user and lock == 'UNLOCKED':
                lock = 'LOCKED'
                write_list.append('%s,%s,%s\n' % (usr,pas,lock))
                continue
            elif isture == False and usr == user and lock == 'LOCKED':
                lock = 'UNLOCKED'
                write_list.append('%s,%s,%s\n' % (usr,pas,lock))
                continue
            write_list.append('%s,%s,%s\n' % (usr,pas,lock))

    with open(USER_FILE,'w') as f:
        for line in write_list:
            f.write(line)


#lock('user1',False)
lock('user1',True)

