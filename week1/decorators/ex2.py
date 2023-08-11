class WithClassDecorate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("****")
        self.func(*args, **kwargs)
        print("****")


def with_decorate(func):
    def wrapper(*args, **kwargs):
        print("****")
        func(*args, **kwargs)
        print("****")

    return wrapper


# function invoke decorator
# @with_decorate
# def print_sth(name):
#     print(name)

# class invoke decorator
@WithClassDecorate
def print_sth(name):
    print(name)


print_sth("hello")
