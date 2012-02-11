import sys ,socket ,string

HOST = 'irc.freenode.net'
PORT = 6667
NICK = 'clarkbar'
IDENT = 'clarkbar'
REALNAME = 'idclark'
CHANNELINIT = '#archlinux' #or whatever. 
readbuffer=''

s = socket.socket()
s.connect((HOST,PORT))
s.send("NICK %s\r\n" %NICK)
s.send("User %s %s bla :%s\r\n"%(IDENT,HOST, REALNAME))

#

while 1:
#infinite loop - ctrl c to kill it. 
    readbuffer = readbuffer + s.recv(1024)

    tmp = string.split(readbuffer, '\n')
    readbuffer = tmp.pop( )

    for line in tmp:
        line = string.rstrip(line)
        line = string.split(line)

        if(line[0] =='PING'):
            s.send('Pong %s\r\n' %line[1])
            
