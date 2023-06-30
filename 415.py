# import sys

# f = sys.stdin.read().splitlines()

# for i in range(1, int(f[0]) + 1):
#     insert_num = int(f[i * 2 - 1].split()[1])
#     return_i = len(f[i * 2])

#     for num_i, num in enumerate(f[i * 2]):
#         if insert_num >= int(num):
#             second_half = f[i * 2][num_i:]
#             half_len = len(second_half)
#             if insert_num == int(second_half[0]):
#                 pass
#             elif insert_num > int(second_half[0]):
#                 return_i = num_i
#                 break
#             else:
#                 break
#             found = False
#             for k, curr_char in enumerate(second_half):
#                 if k == half_len - 1:
#                     if insert_num == int(second_half[k]):
#                         continue
#                     elif insert_num > int(second_half[k]):
#                         return_i = num_i
#                         found = True
#                         break
#                     else:
#                         found = True
#                         break
#                 else:
#                     if second_half[k + 1]  == second_half[k]:
#                         continue
#                     elif int(second_half[k + 1])  > int(second_half[k]):
#                         return_i = num_i
#                         found = True
#                         break
#                     else:
#                         found = True
#                         break
#             if found:
#                 break


#     print(f"{f[i * 2][:return_i]}{insert_num}{f[i * 2][return_i:]}")
#     # different for zeros. 

#     # what if bigger, but the next one is smaller
#     # insert 1 into 12 -> 112 rather than 121

import sys

def main():
    input_data = sys.stdin.read().splitlines()
    t = int(input_data[0].strip())
    idx = 1
    for _ in range(t):
        n, d = map(int, input_data[idx].split())
        idx += 1
        number = input_data[idx].strip()
        idx += 1

        result = ""
        for digit in number:
            while len(result) and int(result[-1]) < d and int(result[-1]) <= int(digit):
                result = result[:-1]
            result += digit
        
        insert_pos = len(result)
        for i, c in enumerate(result):
            if int(c) >= d:
                insert_pos = i
                break
                
        result = result[:insert_pos] + str(d) + result[insert_pos:]
        print(result)

if __name__ == "__main__":
    main()


