def wjj(params):
    def decorator(func):
        def inner(xiaoxiao_param):
            print(params)
            func(xiaoxiao_param)

        return inner

    return decorator


# 方式一
# @wjj("haha")
def xiaoxiao(xiaoxiao_param):
    print(xiaoxiao_param)


# 方式二
wjj("haha")(xiaoxiao)

xiaoxiao("211")
