import setting
from setting import IP, HEADERS
from tools.logger import GetLogger


logger = GetLogger().get_logger()
class ApiOrder():
    def __init__(self):
        logger.info('开始获取login的url地址')
        self.url = IP + '/mtx/index.php?s=/index/buy/add.html'
        logger.info('获取login的url地址是{}'.format(self.url))

    def order(self, session):
        '''
        发起下订单的请求
        :param session:
        :return:
        '''
        data = {
            'goods_id': 1,
            'stock': 1,
            'buy_type': 'goods',
            'address_id': 1290,
            'payment_id': 1,
            'spec': '',
        }
        logger.info('准备发起login的请求，请求的参数是{},header是{}'.format(data, HEADERS))
        resp_order = session.post(self.url, data=data, headers=HEADERS)
        logger.info('放在公共区域sitting的JUMP_URL是{}'.format(setting.JUMP_URL))
        setting.JUMP_URL = resp_order.json().get('data').get('jump_url')
        logger.info('获取的响应值是%s' % resp_order)
        return resp_order



