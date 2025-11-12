from datetime import datetime, timedelta
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import SimplestBlogger
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder
import locale, consts

class MonthHoroscopeBlogger(SimplestBlogger):
    def __init__(self, sign, tg_chat_id, vk_group_id):
        locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
        date = datetime.now() + timedelta(days=10)
        month = date.strftime('%B')
        year = date.year
        builder = PostBuilder(
            message_builder=ContentBuilder(
                generator=DeepSeekTextGenerator(system_prompt='Ты - профессиональный астролог'),
                prompt_builder=IdentityPromptBuilder(f"Составь гороскоп на {month} {year} для знака '{sign}', используй смайлики, используй не более 300 слов")
            )
        )
        processor = TagAdder(['#гороскоп', '#астрология', '#гороскопнамесяц', f"#{sign}"])
        posters = [
            # TelegramPoster(chat_id=tg_chat_id, processor=processor),
            VkPoster(group_id=vk_group_id, processor=processor)
        ]
        super().__init__(builder, posters)

def post():
    bloggers = [
        MonthHoroscopeBlogger(sign='рыбы', tg_chat_id=consts.tg_pisces, vk_group_id=consts.vk_pisces),
        MonthHoroscopeBlogger(sign='овен', tg_chat_id=consts.tg_aries, vk_group_id=consts.vk_aries),
        MonthHoroscopeBlogger(sign='телец', tg_chat_id=consts.tg_taurus, vk_group_id=consts.vk_taurus),
        MonthHoroscopeBlogger(sign='близнецы', tg_chat_id=consts.tg_gemini, vk_group_id=consts.vk_gemini),
        MonthHoroscopeBlogger(sign='рак', tg_chat_id=consts.tg_cancer, vk_group_id=consts.vk_cancer),
        MonthHoroscopeBlogger(sign='лев', tg_chat_id=consts.tg_leo, vk_group_id=consts.vk_leo),
        MonthHoroscopeBlogger(sign='дева', tg_chat_id=consts.tg_virgo, vk_group_id=consts.vk_virgo),
        MonthHoroscopeBlogger(sign='весы', tg_chat_id=consts.tg_libra, vk_group_id=consts.vk_libra),
        MonthHoroscopeBlogger(sign='скорпион', tg_chat_id=consts.tg_scorpio, vk_group_id=consts.vk_scorpio),
        MonthHoroscopeBlogger(sign='стрелец', tg_chat_id=consts.tg_sagittarius, vk_group_id=consts.vk_sagittarius),
        MonthHoroscopeBlogger(sign='козерог', tg_chat_id=consts.tg_capricorn, vk_group_id=consts.vk_capricorn),
        MonthHoroscopeBlogger(sign='водолей', tg_chat_id=consts.tg_aquarius, vk_group_id=consts.vk_aquarius),
    ]

    for blogger in bloggers:
        blogger.post()