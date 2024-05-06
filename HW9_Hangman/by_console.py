import random
import time

words = ["hello", "world", "python", "guitar"]

def setWord():
    result = random.choice(words)
    isopen = [False for _ in range(len(result))]
    return result, isopen

def judge(c, s, p):
    b = False
    for i in range(len(s)):
        if c == s[i]:
            p[i] = True
            b = True

    return s, p, b

def main():
    isPlaying = True
    while isPlaying:
        res, proc = setWord()
        cnt = 0
        stacks = ''
        while True:
            s = ''.join(res[i] if proc[i] else '*' for i in range(len(res)))

            if '*' not in s: # 종료조건
                print("정답은 "+s+"였습니다!")
                print("틀린 횟수:", cnt)
                while True:
                    n = input("다른 단어 맞추기를 하시겠습니까(y/n): ")
                    n.lower()
                    if n != 'n' and n != 'y':
                        print("잘못된 입력입니다.")
                    else: break
                if n == 'n':
                    print("프로그램을 종료합니다.")
                    time.sleep(3)
                    isPlaying = False
                    break
                else:
                    break

            c = input("(추측) 단어 "+s+"에 포함되는 문자를 입력하세요: ")
            c.lower()
            # 예외처리
            if len(c) != 1 or not c.isalpha():
                print("잘못된 입력입니다.")
                continue
            if c in stacks:
                print("이미 포함되어있는 문자입니다.")
            else:
                stacks += c
                res, proc, b = judge(c, res, proc)
                if not b:
                    print("포함되지 않는 문자입니다.")
                    cnt += 1

main()
