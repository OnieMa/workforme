# import pytz
# import datetime
# import csv
#
# # 获取所有的时区
# timezones = pytz.all_timezones
#
# # 打开一个新的csv文件，用于写入数据
# with open('timezones.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Timezone', 'Offset', 'DST']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for timezone in timezones:
#         tz = pytz.timezone(timezone)
#         now = datetime.datetime.now(tz)
#         offset = now.strftime('%z')
#         dst = now.dst()
#
#         # 检查是否有夏令时
#         if dst.seconds != 0:
#             dst = "Yes"
#         else:
#             dst = "No"
#
#         writer.writerow({'Timezone': timezone, 'Offset': offset, 'DST': dst})
#
# print("Data saved in timezones.csv")

import pytz
import datetime
import csv

# 获取所有的时区
timezones = pytz.all_timezones

# 打开一个新的csv文件，用于写入数据
with open('no_timezones.csv', 'w', newline='') as csvfile:
    fieldnames = ['Timezone', 'Offset', 'DST']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for timezone in timezones:
        tz = pytz.timezone(timezone)

        # 获取冬季的时间
        winter = datetime.datetime(datetime.datetime.now().year, 1, 1, tzinfo=tz)
        offset_winter = winter.strftime('%z')
        dst_winter = winter.dst()

        # 检查冬季是否有夏令时
        if dst_winter.seconds != 0:
            dst = "Yes"
        else:
            dst = "No"

        writer.writerow({'Timezone': timezone, 'Offset': offset_winter, 'DST': dst})

print("Data saved in timezones.csv")