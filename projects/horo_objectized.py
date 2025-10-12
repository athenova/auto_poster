from simple_blogger.poster.telegram import TelegramPoster
# from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.yandex import YandexImageGenerator
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
import datetime, consts, time

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
        HoroBlogger(objects[index], sign='рыбы', tg_chat_id=consts.tg_pisces, vk_group_id=consts.vk_pisces),
        HoroBlogger(objects[index], sign='овен', tg_chat_id=consts.tg_aries, vk_group_id=consts.vk_aries),
        HoroBlogger(objects[index], sign='телец', tg_chat_id=consts.tg_taurus, vk_group_id=consts.vk_taurus),
        HoroBlogger(objects[index], sign='близнецы', tg_chat_id=consts.tg_gemini, vk_group_id=consts.vk_gemini),
        HoroBlogger(objects[index], sign='рак', tg_chat_id=consts.tg_cancer, vk_group_id=consts.vk_cancer),
        HoroBlogger(objects[index], sign='лев', tg_chat_id=consts.tg_leo, vk_group_id=consts.vk_leo),
        HoroBlogger(objects[index], sign='дева', tg_chat_id=consts.tg_virgo, vk_group_id=consts.vk_virgo),
        HoroBlogger(objects[index], sign='весы', tg_chat_id=consts.tg_libra, vk_group_id=consts.vk_libra),
        HoroBlogger(objects[index], sign='скорпион', tg_chat_id=consts.tg_scorpio, vk_group_id=consts.vk_scorpio),
        HoroBlogger(objects[index], sign='стрелец', tg_chat_id=consts.tg_sagittarius, vk_group_id=consts.vk_sagittarius),
        HoroBlogger(objects[index], sign='козерог', tg_chat_id=consts.tg_capricorn, vk_group_id=consts.vk_capricorn),
        HoroBlogger(objects[index], sign='водолей', tg_chat_id=consts.tg_aquarius, vk_group_id=consts.vk_aquarius),
    ]

    for blogger in bloggers:
        blogger.post()
        time.sleep(30)

if __name__ == "__main__":
    post()