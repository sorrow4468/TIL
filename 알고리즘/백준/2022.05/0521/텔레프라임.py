num, new = map(int, input().split())
new_num = int(str(new)+str(num))
n = new_num+2                    # 소수를 찾을 범위
a = [False,False] + [True]*(n-1)    # 0 ~ n 까지의 숫자 리스트
primes=[]                           # 소수 집합
for i in range(2,n+1):              # 2 ~ n까지 반복
  if a[i]:                          # 2부터 시작, 해당 숫자가 지워지지 않고 남아있는 소수라면 
    primes.append(i)                # 소수 리스트에 추가
    for j in range(2*i, n+1, i):    # 해당 소수의 배수들을 
        a[j] = False                # 리스트에서 전부 False로 만들기
if num in primes and new_num in primes:
    print('Yes')
else:
    print('No')