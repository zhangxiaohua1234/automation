#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年05月07日
"""
# for item in items

# serial_list = ["SN100", "SN200", "SN300"]
# for serial in serial_list:
#     print(serial)

# for number in range()
# print(range(10))
# for number in range(1, 11):
#     print(number)

# for + tuple
# positions = (100, 200)
# for position in positions:
#     print(position)

# for + string
# phone_type = "darwin"
# for single_char in phone_type:
#     print(single_char)

# for + dictionary
# items(), keys(), values()
# error_records = {
#     "SN100": {
#         "app_crash": 3,
#         "app_anr": 5
#     },
#     "SN101": {
#         "app_crash": 3,
#         "tombstone": 10
#     }
# }
# for pair in error_records.items():
#     print(pair)
#
# for serial_number, errors in error_records.items():
#     print(serial_number)
#     print(errors)
#
# for serial_number in error_records.keys():
#     print(serial_number)

# for errors in error_records.values():
#     print(errors)



# for + for device_crash_count 循环嵌套语句
# 序列号_crash类型_错误次数
error_records = {
    "SN100": {
        "app_crash": 3,
        "app_anr": 5
    },
    "SN101": {
        "app_crash": 3,
        "tombstone": 10
    }
}

for serial_number, errors in error_records.items():
    # print(serial_number)
    # print(errors)
    for error_type, error_count in errors.items():
        # print(error_type, error_count)
        print("%s_%s_%d" % (serial_number, error_type, error_count))


