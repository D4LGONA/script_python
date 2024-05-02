# 3-8

name = input("사원 이름을 입력하세요: ")
time = eval(input("주 당 근무시간을 입력하세요: "))
wage = eval(input("시간 당 급여를 입력하세요: "))
taxr_1 = eval(input("원천징수세율을 입력하세요: "))
taxr_2 = eval(input("지방세율을 입력하세요: "))

print("사원이름:", name)
print("주당 근무시간:", time)
print("임금:", wage)
print("총 급여:", time * wage)
print("공제:")
print("  원천징수세(", taxr_1*100,"%):", (time*wage)*(taxr_1))
print("  주민세(",taxr_2*100,"%):", (time*wage)*(taxr_2))
print("  총 공제:",(time*wage)*(1/5)+(time*wage)*(9/100))
print("공제 후 급여:", time * wage - ((time*wage)*(1/5)+(time*wage)*(9/100)))
