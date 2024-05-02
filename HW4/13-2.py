# 13-2

s = input("파일이름을 입력하세요: ")
f = open(s, "r")
c = f.read()

c_cnt = len(c)
w_cnt = len(c.split())
l_cnt = c.count("\n") + 1
print("문자 {0} 개 \n단어 {1} 개 \n행 {2} 개".format(c_cnt, w_cnt, l_cnt))