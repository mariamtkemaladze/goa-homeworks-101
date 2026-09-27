# def number(lines):
#     arr = []
#     count = 1
    
#     for i in lines:
#         new = str(count) + ": " + i
#         arr.append(new)
#         count += 1
        
#     return arr




# def merge_arrays(arr1, arr2):
#     arr = arr1 + arr2
#     arr = list(set(arr))
#     arr.sort()
#     return arr


# def capitalize(s):
#     even = ""
#     odd = ""

#     for i in range(len(s)):
#         if i % 2 == 0:
#             even += s[i].upper()
#             odd += s[i]
#         else:
#             even += s[i]
#             odd += s[i].upper()

#     return [even, odd]



# def reverse_number(n):
    
#     if n < 0:
#         n = -n
#         n = int(str(n)[::-1])
#         return -n
#     else:
#         n = int(str(n)[::-1])
#         return n
