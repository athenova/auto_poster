import json
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from datetime import date, timedelta
import consts

class LegendaryHoroBlogger(Journalist):
    def _message_generator(self):
        return DeepSeekTextGenerator(f"Ты - профессиональный астролог. Я дам тебе имя известного человека, родившегося под знаком {self.sign}. Приведи отличительную черту {self.sign}, связанный с ним. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'")
    
    def _prompt_constructor(self, _):
        return f"{self.task['person']}({self.task['profession']})"

    def __init__(self, task, sign, tg_chat_id, vk_group_id):
        self.task = task
        self.sign = sign
        tagadder = TagAdder(['#гороскоп', '#астрология', '#знаменитые', f"#{self.sign}"])
        posters = [
            # TelegramPoster(chat_id=tg_chat_id, processor=tagadder),
            # VkPoster(group_id=vk_group_id, processor=tagadder)
            TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    for sign in range(1,12):
        tasks = []
        match sign:
            case  1: tasks = json.load(open("./files/legendary/legendary_pisces.json", "rt", encoding="UTF-8")), 'рыбы', consts.tg_pisces, consts.vk_pisces
            case  2: tasks = json.load(open("./files/legendary/legendary_aries.json", "rt", encoding="UTF-8")), 'овен',consts.tg_aries, consts.vk_aries
            case  3: tasks = json.load(open("./files/legendary/legendary_taurus.json", "rt", encoding="UTF-8")), 'телец',consts.tg_taurus, consts.vk_taurus
            case  4: tasks = json.load(open("./files/legendary/legendary_gemini.json", "rt", encoding="UTF-8")), 'близнецы',consts.tg_gemini, consts.vk_gemini
            case  5: tasks = json.load(open("./files/legendary/legendary_cancer.json", "rt", encoding="UTF-8")), 'рак',consts.tg_cancer, consts.vk_cancer
            case  6: tasks = json.load(open("./files/legendary/legendary_leo.json", "rt", encoding="UTF-8")), 'лев',consts.tg_leo, consts.vk_leo
            case  7: tasks = json.load(open("./files/legendary/legendary_virgo.json", "rt", encoding="UTF-8")), 'дева', consts.tg_virgo, consts.vk_virgo
            case  8: tasks = json.load(open("./files/legendary/legendary_libra.json", "rt", encoding="UTF-8")), 'весы',consts.tg_libra, consts.vk_libra
            case  9: tasks = json.load(open("./files/legendary/legendary_scorpio.json", "rt", encoding="UTF-8")), 'скорпион',consts.tg_scorpio, consts.vk_scorpio
            case 10: tasks = json.load(open("./files/legendary/legendary_sagittarius.json", "rt", encoding="UTF-8")), 'стрелец',consts.tg_sagittarius, consts.vk_sagittarius
            case 11: tasks = json.load(open("./files/legendary/legendary_capricorn.json", "rt", encoding="UTF-8")), 'козерог',consts.tg_capricorn, consts.vk_capricorn
            case 12: tasks = json.load(open("./files/legendary/legendary_aquarius.json", "rt", encoding="UTF-8")), 'водолей',consts.tg_aquarius, consts.vk_aquarius
        start_date = date(2025, 10, 17)-timedelta(days=offset)
        today = date.today()
        index = ((today - start_date).days // 7 + offset) % len(tasks[0])
        blogger = LegendaryHoroBlogger(tasks[0][index], tasks[1], tasks[2], tasks[3])
        blogger.post()

if __name__ == "__main__":
    post()