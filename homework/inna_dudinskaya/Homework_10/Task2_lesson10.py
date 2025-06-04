def repeat_number(count):
    def repeat_me(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return repeat_me


@repeat_number(count=2)
def example(text):
    print(text)


example('print me')
