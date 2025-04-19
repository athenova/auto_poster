from datetime import datetime, timedelta
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import SimplestBlogger
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder
import locale

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
            TelegramPoster(chat_id=tg_chat_id, processor=processor),
            VkPoster(group_id=vk_group_id, processor=processor)
        ]
        super().__init__(builder, posters)

def post():
    bloggers = [
        MonthHoroscopeBlogger(sign='рыбы', tg_chat_id='@pisces_the', vk_group_id='229837683'),
        MonthHoroscopeBlogger(sign='овен', tg_chat_id='@aries_the', vk_group_id='229837854'),
        MonthHoroscopeBlogger(sign='телец', tg_chat_id='@ai_tarot', vk_group_id='229860740'),
        MonthHoroscopeBlogger(sign='близнецы', tg_chat_id='@gemini_the', vk_group_id='229837895'),
        MonthHoroscopeBlogger(sign='рак', tg_chat_id='@ai_tarot', vk_group_id='229860780'),
        MonthHoroscopeBlogger(sign='лев', tg_chat_id='@ai_tarot', vk_group_id='229860665'),
        MonthHoroscopeBlogger(sign='дева', tg_chat_id='@ai_tarot', vk_group_id='229860810'),
        MonthHoroscopeBlogger(sign='весы', tg_chat_id='@ai_tarot', vk_group_id='229860834'),
        MonthHoroscopeBlogger(sign='скорпион', tg_chat_id='@ai_tarot', vk_group_id='229860866'),
        MonthHoroscopeBlogger(sign='стрелец', tg_chat_id='@ai_tarot', vk_group_id='229860894'),
        MonthHoroscopeBlogger(sign='козерог', tg_chat_id='@capricorn_the', vk_group_id='229837876'),
        MonthHoroscopeBlogger(sign='водолей', tg_chat_id='@aquarius_the', vk_group_id='229837930'),
    ]

    for blogger in bloggers:
        blogger.post()