def check_access(func):
    def wrapper(obj, *args, **kwargs):
        if obj.has_access():
            return func(obj, *args, **kwargs)
        raise Exception('You dont have access to this action.')

    return wrapper
