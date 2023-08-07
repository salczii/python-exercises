arg = 5


def arg_check(arg):
    def check(old_func):
        def new_func(*args, **kwargs):
            def check_type(decorator_param, function_param):
                if not isinstance(decorator_param, type(function_param)):
                    raise Exception("Type mismatch error")

            try:
                check_type(arg, args[0])
            except Exception as e:
                print("An error occurred:", str(e))
            old_func(*args, **kwargs)

        return new_func

    return check


@arg_check(arg)
def examp(num):
    return num


examp("hello")
