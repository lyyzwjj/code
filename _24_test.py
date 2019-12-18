# coding:utf-8
import unittest
from _23_login import app
import json


class LoginTest(unittest.TestCase):
    """构造单元测试案例"""

    def setUp(self):
        """在进行测试之前先被执行"""
        # 设置flask工作在测试模式下
        # app.config["TESTING"] = True
        app.testing = True
        # 创建进行web请求的客户端,使用flask提供的
        self.client = app.test_client()

    def test_empty_user_name_password(self):
        """测试用户名密码不完整的情况"""
        # 创建进行web请求的客户端,使用flask提供的
        # client = app.test_client()
        # 利用client客户端模拟发送web请求
        # 测试用户名和密码都不传
        ret = self.client.post("/login", data={})
        # ret 视图返回的响应对象
        resp = ret.data
        # 因为login视图返回的是json字符串
        # json.load() 是读取文件的
        resp = json.loads(resp)
        # 拿到返回值后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

        # 测试只传用户名
        ret = self.client.post("/login", data={"user_name": "admin"})
        # ret 视图返回的响应对象
        resp = ret.data
        # 因为login视图返回的是json字符串
        # json.load() 是读取文件的
        resp = json.loads(resp)
        # 拿到返回值后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)
        # 测试只传用户名
        ret = self.client.post("/login", data={"password": "python"})
        # ret 视图返回的响应对象
        resp = ret.data
        # 因为login视图返回的是json字符串
        # json.load() 是读取文件的
        resp = json.loads(resp)
        # 拿到返回值后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

    def test_wrong_user_name_password(self):
        """用户名或密码错误"""
        # 测试传错误用户名和密码
        ret = self.client.post("/login", data={"user_name": "itcast", "password": "itcast"})
        # ret 视图返回的响应对象
        resp = ret.data
        # 因为login视图返回的是json字符串
        # json.load() 是读取文件的
        resp = json.loads(resp)
        # 拿到返回值后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 2)


if __name__ == '__main__':
    unittest.main()
