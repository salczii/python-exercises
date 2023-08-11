# from functools import wraps

def logged(funct):
    # @wraps(func)
    def with_logging(*args, **kwargs):
        args_string = ",".join(map(str, args))
        print(f"you called {funct.__name__}({args_string}) it returned {str(funct(*args, **kwargs))}")
        return funct(*args, **kwargs)

    return with_logging


@logged
def func(*args):
    return 3 + len(args)


func(4, 4, 4)
