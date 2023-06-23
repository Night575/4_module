import vk_api
import random
from cb_rf import get_dollar_course


token = "vk1.a.3wOVEu4SOrw769Wp2kRh0kfJjxOPesS7sQmqRZSz0vgHCjEuOJzYmi3Pz75cCVyMRRvPq2B19lEEmhGdqTmXAtRoUMq-BjTXEQMgx2ClST56LkwmDgWcSFO0Pp0ILC52konGJ7OKe7tIcYxjLv26Rc7ew_LQPzEGcJ7Ts36LtjwTqLJxaUN7Mq9l0OvW4-ilHQWSY-ysUNbgUZ4vC2v4PQ"

vk = vk_api.VkApi(token=token)

while True:
    messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
    if messages['count'] > 0:
        message_text = messages['items'][0]['last_message']['text']
        if message_text == "курс":
            ans = f"Курс доллара на сегодня составляет {get_dollar_course()} руб."
        else:
            ans = "Неизвестная команда"
        user_id = messages['items'][0]['last_message']['from_id']
        random_id = random.randint(-10 ** 7, 10 ** 7)

        vk.method("messages.send", {
            "user_id": user_id,
            "random_id": random_id,
            "message": ans,
        })