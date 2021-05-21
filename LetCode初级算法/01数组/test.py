IP = "192.168.1.0/22"
ipAdd, mask = IP.split("/")[0] ,IP.split("/")[1]
print(IP.split("/"))

def ch1(num):
        s = []
             for i in range(4):
                  s.append(str(num %256))
                  num /= 256
        return '.'.join(s[::-1])