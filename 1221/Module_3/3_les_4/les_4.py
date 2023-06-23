# import time
#
# start = time.time()
# my_list = (time.sleep(x) for x in range(1, 3))
# #my_list = [time.sleep(x) for x in range(1, 3)]

# for i in my_list:
#     print(i)
#
# print(time.time() - start)
#
# for i in my_list:
#     print(i)

#print(time.time() - start)


# print(type(my_list))
# t = (1, 2, 3)
# print(type(t))

# def my_lazy_func():
#     for i in range(1, 11):
#         print('До', i)
#         yield i
#         print('После', i)
#
# for i in my_lazy_func():
#     print(i)

# def my_lazy_func(items):
# #     for i in items:
# #         yield i ** 2
#
#     yield from (i ** 2 for i in items)
#
# for i in my_lazy_func():
#     print(i)

