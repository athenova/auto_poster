from datetime import datetime, timedelta
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger.basic import SimplestBlogger
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder
import ephem

class FullMoonTarotBlogger(SimplestBlogger):
    def __init__(self, sign, tg_chat_id, vk_group_id):
        today = datetime.now().date()
        full_moon_date = ephem.next_full_moon(today).datetime()
        builder = PostBuilder(
            message_builder=ContentBuilder(
                generator=DeepSeekTextGenerator(system_prompt='Ты - профессиональный таролог'),
                prompt_builder=IdentityPromptBuilder(f"Составь таро-гороскоп на полнолуние {full_moon_date.strftime('%Y-%m-%d')} для знака '{sign}', используй смайлики, используй не более 300 слов")
            )
        )
        processor = TagAdder(['#гороскоп', '#таро', '#таронаполнолуние', f"#{sign}"])
        posters = [
            TelegramPoster(chat_id=tg_chat_id, processor=processor),
            VkPoster(group_id=vk_group_id, processor=processor)
        ]
        super().__init__(builder, posters)

def handle():
    today = datetime.now().date()
    check_date = today + timedelta(days=2)   
    full_moon_date = ephem.next_full_moon(today).datetime().date()
    if full_moon_date == check_date:
        bloggers = [
            FullMoonTarotBlogger(sign='рыбы', tg_chat_id='@pisces_the', vk_group_id='229837683'),
            FullMoonTarotBlogger(sign='овен', tg_chat_id='@aries_the', vk_group_id='229837854'),
            FullMoonTarotBlogger(sign='телец', tg_chat_id='@ai_tarot', vk_group_id='229860740'),
            FullMoonTarotBlogger(sign='близнецы', tg_chat_id='@gemini_the', vk_group_id='229837895'),
            FullMoonTarotBlogger(sign='рак', tg_chat_id='@ai_tarot', vk_group_id='229860780'),
            FullMoonTarotBlogger(sign='лев', tg_chat_id='@ai_tarot', vk_group_id='229860665'),
            FullMoonTarotBlogger(sign='дева', tg_chat_id='@ai_tarot', vk_group_id='229860810'),
            FullMoonTarotBlogger(sign='весы', tg_chat_id='@ai_tarot', vk_group_id='229860834'),
            FullMoonTarotBlogger(sign='скорпион', tg_chat_id='@ai_tarot', vk_group_id='229860866'),
            FullMoonTarotBlogger(sign='стрелец', tg_chat_id='@ai_tarot', vk_group_id='229860894'),
            FullMoonTarotBlogger(sign='козерог', tg_chat_id='@capricorn_the', vk_group_id='229837876'),
            FullMoonTarotBlogger(sign='водолей', tg_chat_id='@aquarius_the', vk_group_id='229837930'),
        ]
        for blogger in bloggers:
            blogger.post()