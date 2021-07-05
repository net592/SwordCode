s =  ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46',
      'eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
print(s)


# print( s[0], "\n", s[0].split("eth 1/101/"), "\n", s[0].split("eth 1/101/")[1], 
#        int("".join(s[0].split("eth ")[1].split("/"))                ))

#s.sort(key=lambda x:(x.split("eth ")[1].split("/")[2],x.split("eth ")[1].split("/")[3]), reverse= True)
# 'eth 1/101/1/42'把接口切割成 [1/101/1/42]  转成数组[1,101,1,42] 在转成 数字1101142，排序 sort
s.sort(key=lambda x:(int("".join(x.split("eth ")[1].split("/"))) ))
print(s)