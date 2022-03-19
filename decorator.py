# def check_access(access_status):
#     def inner_decorator(func):
#         def check_func(*args, **kwargs):
#             if access_status:
#                 func(*args, **kwargs)
#             else:
#                 print("You dont access to run this function.")
#
#         return check_func
#
#     return inner_decorator


def check_access(func):
    def inner(self, *args, **kwargs):
        if self.has_access():
            func(*args, **kwargs)
        else:
            print("You dont access to run this function.")

    return inner
