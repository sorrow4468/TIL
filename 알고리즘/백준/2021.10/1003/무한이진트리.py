a, b = map(int, input().split()) # 끝노드

# 시작노드에서 왼쪽으로 내려가면 a가 커지고
# 오른쪽으로 내려가면 b가 커진다
# 주어진 (a, b)노드에서 a가 크면 왼쪽으로 내려온 노드
# b가 크면 오른쪽으로 내려온 노드임을 알 수 있다
# 이를 이용해 (a, b)에서 (1, 1)까지 거꾸로 올라간다

l = r = 0 # 올라가면서 체크할 왼쪽 오른쪽 이동 횟수

while a+b != 2: # 루트노드에 도달할 때 까지
    if a > b: # 왼쪽으로 내려왔던 노드이면
        a -= b # 부모노드의 a
        l += 1 # 왼쪽 카운트 +1
    elif a < b: # 오른쪽으로 내려왔던 노드이면
        b -= a # 부모노드의 b
        r += 1 # 오른쪽 카운트 +1

print(l, r) # 출력