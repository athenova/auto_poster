from simple_blogger.poster.telegram import TelegramPoster
# from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.yandex import YandexImageGenerator
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
import datetime

class HoroBlogger(Journalist):
    def _message_generator(self):
        return DeepSeekTextGenerator('Ты - профессиональный астролог. Я дам тебе знак зодиака и категорию. Расскажи каким объектом из категории ты бы был, если бы бы этим знаком зодика. Объясни, почему. Используй не более 150 слов. Используй смайлики, не используй "Конечно" и "Окей"')
    
    def _image_generator(self):
        return YandexImageGenerator(system_prompt="Нарисуй, как бы выглядел знак зодиака по описанию")

    def _prompt_constructor(self, _):
        return f"{self.sign}, {self.object}"

    def __init__(self, object, sign, tg_chat_id, vk_group_id):
        self.object = object
        self.sign = sign
        tagadder = TagAdder(['#гороскоп', '#иллюстрации', '#ктоты', f"#{sign}"])
        posters = [
            TelegramPoster(chat_id=tg_chat_id, processor=tagadder),
            VkPoster(group_id=vk_group_id, processor=tagadder),
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    start_date = datetime.date(2025, 6, 29)
    today = datetime.date.today()
    objects = [
        "цветок",
        "известный философ",
        "животное",
        "марка автомобиля",
        "фрукт",
        "известный писатель",
        "насекомое",
        "известный художник",
        "дерево",
        "известный химик",
        "овощ",
        "известный изобретатель",
        "скульптура",
        "известный физик",
        "картина",
        "химический элемент",
    ]
    index = ((today - start_date).days // 7 + offset) % len(objects)
    bloggers = [
        HoroBlogger(objects[index], sign='рыбы', tg_chat_id='@pisces_the', vk_group_id='229837683'),
        HoroBlogger(objects[index], sign='овен', tg_chat_id='@aries_the', vk_group_id='229837854'),
        HoroBlogger(objects[index], sign='телец', tg_chat_id='@horo_ai', vk_group_id='229860740'),
        HoroBlogger(objects[index], sign='близнецы', tg_chat_id='@gemini_the', vk_group_id='229837895'),
        HoroBlogger(objects[index], sign='рак', tg_chat_id='@horo_ai', vk_group_id='229860780'),
        HoroBlogger(objects[index], sign='лев', tg_chat_id='@horo_ai', vk_group_id='229860665'),
        HoroBlogger(objects[index], sign='дева', tg_chat_id='@horo_ai', vk_group_id='229860810'),
        HoroBlogger(objects[index], sign='весы', tg_chat_id='@horo_ai', vk_group_id='229860834'),
        HoroBlogger(objects[index], sign='скорпион', tg_chat_id='@horo_ai', vk_group_id='229860866'),
        HoroBlogger(objects[index], sign='стрелец', tg_chat_id='@horo_ai', vk_group_id='229860894'),
        HoroBlogger(objects[index], sign='козерог', tg_chat_id='@capricorn_the', vk_group_id='229837876'),
        HoroBlogger(objects[index], sign='водолей', tg_chat_id='@aquarius_the', vk_group_id='229837930'),
    ]

    for blogger in bloggers:
        blogger.post()

if __name__ == "__main__":
    post()