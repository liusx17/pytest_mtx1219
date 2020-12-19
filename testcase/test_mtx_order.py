import requests

from api.apiLogin import ApiLogin
from api.apiOrder import ApiOrder

class TestOrder():
    def setup_class(self):
        # 获取session对象
        self.session = requests.Session()
        #创建order对象
        self.order_object = ApiOrder()
        #调用成功的登录接口
        ApiLogin().login_success(self.session)

    def test_order(self):
        resp_order = self.order_object.order(self.session).json()
        # 做断言
        assert resp_order.get('msg') == '提交成功'


