#to understand the meaning of {if __name__ == "__main__":}
# [] why does it exist?
# 즉, 어떤 스크립트 파일이든 파이썬 인터프리터가 최초로 실행한 스크립트 파일의 __name__에는 '__main__'이 들어갑니다.
# 이는 프로그램의 시작점(entry point)이라는 뜻입니다.


import hello

print('main.py __name__:', __name__)
# if __name__=="__main__":
    # main()