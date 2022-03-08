import telnetlib
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
with telnetlib.Telnet(host=TCP_IP, port=TCP_PORT) as t:
    t.mt_interact()
    t.write(b"exit\n")
