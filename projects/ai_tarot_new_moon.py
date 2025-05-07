from datetime import datetime, timedelta
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import SimplestBlogger
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder
import ephem

class NewMoonTarotBlogger(SimplestBlogger):
    def __init__(self, sign, tg_chat_id, vk_group_id):
        today = datetime.now().date()
        next_new_moon = ephem.next_new_moon(today).datetime()
        builder = PostBuilder(
            message_builder=ContentBuilder(
                generator=DeepSeekTextGenerator(system_prompt='Ты - профессиональный таролог'),
                prompt_builder=IdentityPromptBuilder(f"Составь таро-гороскоп на новолуние {next_new_moon.strftime('%Y-%m-%d')} для знака '{sign}', используй смайлики, используй не более 300 слов")
            )
        )
        processor = TagAdder(['#гороскоп', '#таро', '#таронановолуние', f"#{sign}"])
        posters = [
            TelegramPoster(chat_id=tg_chat_id, processor=processor),
            VkPoster(group_id=vk_group_id, processor=processor)
        ]
        super().__init__(builder, posters)

def post():
    today = datetime.now().date()
    check_date = today + timedelta(days=2)   
    new_moon_date = ephem.next_new_moon(today).datetime().date()
    if new_moon_date == check_date:
        bloggers = [
            NewMoonTarotBlogger(sign='рыбы', tg_chat_id='@pisces_the', vk_group_id='229837683'),
            NewMoonTarotBlogger(sign='овен', tg_chat_id='@aries_the', vk_group_id='229837854'),
            NewMoonTarotBlogger(sign='телец', tg_chat_id='@ai_tarot', vk_group_id='229860740'),
            NewMoonTarotBlogger(sign='близнецы', tg_chat_id='@gemini_the', vk_group_id='229837895'),
            NewMoonTarotBlogger(sign='рак', tg_chat_id='@ai_tarot', vk_group_id='229860780'),
            NewMoonTarotBlogger(sign='лев', tg_chat_id='@ai_tarot', vk_group_id='229860665'),
            NewMoonTarotBlogger(sign='дева', tg_chat_id='@ai_tarot', vk_group_id='229860810'),
            NewMoonTarotBlogger(sign='весы', tg_chat_id='@ai_tarot', vk_group_id='229860834'),
            NewMoonTarotBlogger(sign='скорпион', tg_chat_id='@ai_tarot', vk_group_id='229860866'),
            NewMoonTarotBlogger(sign='стрелец', tg_chat_id='@ai_tarot', vk_group_id='229860894'),
            NewMoonTarotBlogger(sign='козерог', tg_chat_id='@capricorn_the', vk_group_id='229837876'),
            NewMoonTarotBlogger(sign='водолей', tg_chat_id='@aquarius_the', vk_group_id='229837930'),
        ]
        for blogger in bloggers:
            blogger.post()