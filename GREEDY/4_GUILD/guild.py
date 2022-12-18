n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: #공포도를 낮은 것부터 하나씩 확인하며
    count += 1 #현재 그룹에 해당 모험가를 포함시키고
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면 그룹 결성
        result += 1 #총 그룹의 수 증가
        count = 0 #모험가의 수 초기화

print(result)    

# #그룹 멤버
# group_members = []
# #그룹 목표 멤버 수
# group_sum = 0

# for member in data:
#     group_members.append(member)
#     if group_sum < member:
#         group_sum = member
#     if len(group_members) != group_sum:
#         continue
#     else:
#         result += 1
#         group_members = []
#         group_sum = 0
#         continue

# print(result)