import random, string

line_template="{user}:{password}:{uid}:{gid}:{user} Account:/home/{user}:/bin/bash"

def gen_passwd(n):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(n))

def gen_users(n):
    for i in range(1,n+1):
        yield line_template.format(user='user'+str(i),password=gen_passwd(10),uid=1000+i,gid=1000+i)

priv = open('users_priv.txt','w')
pub = open('users_pub.txt','w')
for user in gen_users(40):
    priv.write(user+'\n')
    pub.write(':'.join(user.split(':')[:2])+'\n')
