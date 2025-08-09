from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import SimplestBlogger
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.generator.openai import OpenAiTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder
import consts, json
from datetime import date

class HoroscopeBlogger(SimplestBlogger):
    def __init__(self, sign, tg_chat_id, vk_group_id, task):
        builder = PostBuilder(
            message_builder=ContentBuilder(
                generator=DeepSeekTextGenerator(system_prompt='Ты - профессиональный астролог. Я буду давать тебе знак зодиака, категорию человеческой жизни и аспект из этой категории. Расскажи, как знаку зодиака развить этот аспект жизни. Используй смайлики, используй не более 350 слов'),
                prompt_builder=IdentityPromptBuilder(f"{sign}, {task['category']}, {task['aspect']}")
            )
        )
        processor = TagAdder(['#гороскоп', '#астрология', '#развитие', f"#{sign}"])
        posters = [
            TelegramPoster(chat_id=tg_chat_id, processor=processor),
            VkPoster(group_id=vk_group_id, processor=processor),
            # TelegramPoster()
        ]
        super().__init__(builder, posters)

def post(offset=0):
    tasks = json.load(open("./files/life_aspect.json", "rt", encoding="UTF-8"))
    start_date = date(2025, 8, 11)
    today = date.today()
    index = ((today - start_date).days // 7 + offset) % len(tasks)
    task = tasks[index]
    bloggers = [
        HoroscopeBlogger(sign='рыбы', tg_chat_id=consts.tg_pisces, vk_group_id=consts.vk_pisces, task=task),
        HoroscopeBlogger(sign='овен', tg_chat_id=consts.tg_aries, vk_group_id=consts.vk_aries, task=task),
        HoroscopeBlogger(sign='телец', tg_chat_id=consts.tg_taurus, vk_group_id=consts.vk_taurus, task=task),
        HoroscopeBlogger(sign='близнецы', tg_chat_id=consts.tg_gemini, vk_group_id=consts.vk_gemini, task=task),
        HoroscopeBlogger(sign='рак', tg_chat_id=consts.tg_cancer, vk_group_id=consts.vk_cancer, task=task),
        HoroscopeBlogger(sign='лев', tg_chat_id=consts.tg_leo, vk_group_id=consts.vk_leo, task=task),
        HoroscopeBlogger(sign='дева', tg_chat_id=consts.tg_virgo, vk_group_id=consts.vk_virgo, task=task),
        HoroscopeBlogger(sign='весы', tg_chat_id=consts.tg_libra, vk_group_id=consts.vk_libra, task=task),
        HoroscopeBlogger(sign='скорпион', tg_chat_id=consts.tg_scorpio, vk_group_id=consts.vk_scorpio, task=task),
        HoroscopeBlogger(sign='стрелец', tg_chat_id=consts.tg_sagittarius, vk_group_id=consts.vk_sagittarius, task=task),
        HoroscopeBlogger(sign='козерог', tg_chat_id=consts.tg_capricorn, vk_group_id=consts.vk_capricorn, task=task),
        HoroscopeBlogger(sign='водолей', tg_chat_id=consts.tg_aquarius, vk_group_id=consts.vk_aquarius, task=task),
    ]

    for blogger in bloggers:
        blogger.post()

if __name__ == "__main__":
    post()