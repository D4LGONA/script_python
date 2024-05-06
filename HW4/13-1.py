# 13-1

s = input("파일 이름을 입력하세요: ")
f = open(s, "r+")
st = f.read()
d_s = input("제거할 문자열을 입력하세요: ")
n_st = st.replace(d_s, '')
f.seek(0)
f.write(n_st)
f.truncate()
f.close()
