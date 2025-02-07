n = int(input())
split_num = input().split(' ')
new_arr_int = []
for i in split_num:
    new_arr_int.append(int(i))
sorted_with_non_duplicated = sorted(set(new_arr_int))
result = sorted_with_non_duplicated[1]
print(split_num,new_arr_int, sorted_with_non_duplicated,result)
