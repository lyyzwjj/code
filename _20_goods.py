# coding:utf-8

# from _18_main import app


def route(params):
    def decorator(func):
        def inner():
            print(params)
            func()

        return inner

    return decorator


# 用法一 @route("/get_goods")  = decorator(itcast)


def itcast(func):
    def inner():
        func()

    return inner


# 用法二 装饰器函数带两个参数  不行
# route("/itcast")(itcast)

# 装饰器用法二
# itcast(get_goods)

# 装饰器用法一
# @itcast
# @app.route('/get_goods')
def get_goods():
    return "get_goods page"
