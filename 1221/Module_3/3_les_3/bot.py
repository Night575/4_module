import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from cb_rf import get_course
from wiki import get_article



token = "vk1.a.3wOVEu4SOrw769Wp2kRh0kfJjxOPesS7sQmqRZSz0vgHCjEuOJzYmi3Pz75cCVyMRRvPq2B19lEEmhGdqTmXAtRoUMq-BjTXEQMgx2ClST56LkwmDgWcSFO0Pp0ILC52konGJ7OKe7tIcYxjLv26Rc7ew_LQPzEGcJ7Ts36LtjwTqLJxaUN7Mq9l0OvW4-ilHQWSY-ysUNbgUZ4vC2v4PQ"


vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        user_id = event.user_id
        if user_message[:2] == '-к':
            response = 'Доллар стоит {0} руб.\nЕвро стоит {1} руб.\nЮань стоит {2} руб.'.format(
                get_course("R01235"), get_course("R01239"), get_course("R01375")
            )
        elif user_message[:2] == '-в':
            article = user_message[2:]
            response = get_article(article)
        else:
            response = 'Такой команды я не знаю'
        vk.messages.send(
            user_id=user_id,
            message=response,
            random_id=random.randint(-10 ** 7, 10 ** 7)

        )