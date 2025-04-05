from datetime import datetime, timedelta
from simple_blogger.poster.TelegramPoster import TelegramPoster
from simple_blogger.poster.VkPoster import VkPoster
from simple_blogger.blogger.basic import SimplestBlogger
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder

class HoroscopeBlogger(SimplestBlogger):
    def __init__(self, sign, tg_chat_id, vk_group_id):
        tomorrow = datetime.today() + timedelta(days=1)
        builder = PostBuilder(
            message_builder=ContentBuilder(
                generator=DeepSeekTextGenerator(system_prompt='Ты - профессиональный астролог'),
                prompt_builder=IdentityPromptBuilder(f"Составь гороскоп на {tomorrow.strftime('%Y-%m-%d')} для знака '{sign}', используй смайлики, используй не более 300 слов")
            )
        )
        processor = TagAdder(['#гороскоп', '#астрология', '#гороскопназавтра', f"#{sign}"])
        posters = [
            TelegramPoster(chat_id=tg_chat_id, processor=processor),
            VkPoster(group_id=vk_group_id, processor=processor)
        ]
        super().__init__(builder, posters, True)

def handle():
    bloggers = [
        HoroscopeBlogger(sign='рыбы', tg_chat_id='@pisces_the', vk_group_id='229837683'),
        HoroscopeBlogger(sign='овен', tg_chat_id='@aries_the', vk_group_id='229837854'),
        HoroscopeBlogger(sign='телец', tg_chat_id='@ai_tarot', vk_group_id='229860740'),
        HoroscopeBlogger(sign='близнецы', tg_chat_id='@gemini_the', vk_group_id='229837895'),
        HoroscopeBlogger(sign='рак', tg_chat_id='@ai_tarot', vk_group_id='229860780'),
        HoroscopeBlogger(sign='лев', tg_chat_id='@ai_tarot', vk_group_id='229860665'),
        HoroscopeBlogger(sign='дева', tg_chat_id='@ai_tarot', vk_group_id='229860810'),
        HoroscopeBlogger(sign='весы', tg_chat_id='@ai_tarot', vk_group_id='229860834'),
        HoroscopeBlogger(sign='скорпион', tg_chat_id='@ai_tarot', vk_group_id='229860866'),
        HoroscopeBlogger(sign='стрелец', tg_chat_id='@ai_tarot', vk_group_id='229860894'),
        HoroscopeBlogger(sign='козерог', tg_chat_id='@capricorn_the', vk_group_id='229837876'),
        HoroscopeBlogger(sign='водолей', tg_chat_id='@aquarius_the', vk_group_id='229837930'),
    ]

    for blogger in bloggers:
        blogger.post()