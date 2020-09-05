# coding:utf-8
import unittest

from _16_author_book import Author, db, app


class DatabaseTest(unittest.TestCase):
    """测试"""

    def setUp(self):
        app.testing = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Wzzst310@163.com@129.204.35.106:3306/author_book_py_test"
        db.create_all()

    def test_add_author(self):
        author = Author(name="wjj", email="wzzst310@163.com", mobile="18684954312", addr="Shanghai TangTown")
        db.session.add(author)
        db.session.commit()
        result_author = Author.query.filter_by(name="wjj").first()
        self.assertIsNotNone(result_author)

    def tearDown(self):
        """在所有测试之后,执行,通常用来进行清理操作"""
        db.session.remove()
        import time
        time.sleep(20)
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
