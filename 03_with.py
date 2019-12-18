# coding:utf-8
"""
f = open("./1.txt", "wb")
try:
    # print("hello flask".encode("utf-8", errors='strict'))
    # print("hello flask你好".encode("gbk", errors='strict'))
    f.write("hello flask你好".encode("utf-8", errors='strict'))
except Exception:
    pass
finally:
    f.close()
"""


# with 上下文管理器   类似于一个管家  在with语句执行的时候 with可以做一些铺垫操作 铺垫操作是enter 自己操作的  收尾操作是exit 也是自己操作的
# with open("./1.txt", "wb") as f:
#     f.write("hello flask你好".encode("utf-8", errors='strict'))


class Foo(object):
    def __enter__(self):
        """进入with语句的时候被with调用"""
        print("enter called")

    # 离开可能遇到异常  异常类型 异常值 异常追踪 信息
    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开with语句的时候被with调用"""
        print("exc_type: %s" % exc_type)
        print("exc_val: %s" % exc_val)
        print("exc_tb: %s" % exc_tb)


with Foo() as foo:
    i = 1 / 0
    print("hello python")
