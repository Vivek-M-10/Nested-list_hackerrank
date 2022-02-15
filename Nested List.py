final_lst = []
for i in range(int(input())):
    temp_lst = []
    name = input()
    score = float(input())
    temp_lst.append(name)
    temp_lst.append(score)
    final_lst.append(temp_lst)
print(final_lst)
score_lst = []
for i in range(0, len(final_lst)):
    score_lst.append(final_lst[i][1])
print(score_lst)
temp_lst1 = sorted(list(set(score_lst)))
lowest = temp_lst1[1]
print(lowest)
final_name_lst = []
for i in range(0, len(final_lst)):
    if final_lst[i][1] == lowest:
        final_name_lst.append(final_lst[i][0])
    else:
        continue
print(final_name_lst)
final_name_lst.sort()
print(final_name_lst)
for i in final_name_lst:
    print(i)


