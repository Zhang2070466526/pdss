from django.test import TestCase

# Create your tests here.
# import arrow
#
# timestamps = ['2023-06-06 16:22:36', '2023-06-06 16:24:45', '2023-06-06 16:24:47','2023-06-06 16:27:37','2023-06-06 16:30:06']
# arrow_objects = [arrow.get(timestamp) for timestamp in timestamps]
# sorted_arrow_objects = sorted(arrow_objects)
# print(sorted_arrow_objects)
# # for arrow_object in sorted_arrow_objects:
# #     print(arrow_object)
# # consecutive_count = 0
# #
# # for i in range(1, len(sorted_arrow_objects)):
# #     time_difference = (sorted_arrow_objects[i] - sorted_arrow_objects[i-1]).total_seconds()
# #     if time_difference == 60:
# #         consecutive_count += 1
# # print(consecutive_count)
#
#
#
# import pandas as pd
#
# # dates = [<Arrow [2023-06-06T16:22:36+00:00]>, <Arrow [2023-06-06T16:24:45+00:00]>, <Arrow [2023-06-06T16:24:47+00:00]>, <Arrow [2023-06-06T16:27:37+00:00]>, <Arrow [2023-06-06T16:30:06+00:00]>]


import arrow

timestamps = ['2023-06-06 16:22:36', '2023-06-06 16:24:45', '2023-06-06 16:24:47','2023-06-06 16:27:37','2023-06-06 16:30:06']
arrow_objects = [arrow.get(timestamp) for timestamp in timestamps]
sorted_arrow_objects = sorted(arrow_objects)
print(sorted_arrow_objects)
dates=sorted_arrow_objects
count = 0
previous_date = None

for date in dates:
    if previous_date is not None:
        minute_difference = (date - previous_date).total_seconds() / 60
        print(date,previous_date,)
        if minute_difference >= 1:
            count += 1
    previous_date = date
print(count)





