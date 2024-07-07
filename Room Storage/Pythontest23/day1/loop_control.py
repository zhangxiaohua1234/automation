#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年05月07日
"""
# break 用来终止最深层的循环，并开始下一行代码。
# phone_list = [("darwin", 5), ("delta", 10), ("Ocean", 8), ("Trident", 20)]
# for phone_info in phone_list:
#     if phone_info[0] == "delta":
#         break
#     print(phone_info)

# continue 仅跳出本次循环，而不是终止整个循环
# phone_list = [("darwin", 5), ("delta", 10), ("Ocean", 8), ("Trident", 20)]
# for phone_info in phone_list:
#     if phone_info[0] == "delta":
#         continue
#     print(phone_info)

# pass 不做任何事情，作为一个占位
phone_list = [("darwin", 5), ("delta", 10), ("Ocean", 8), ("Trident", 20)]
for phone_info in phone_list:
    if phone_info[0] == "delta":
        pass
    print(phone_info)
