from datetime import datetime, timedelta, date
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import SimplestBlogger
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder
import consts

class SignHoroscopeBlogger(SimplestBlogger):
    def __init__(self, sign, tg_chat_id, vk_group_id, sign2):
        builder = PostBuilder(
            message_builder=ContentBuilder(
                generator=DeepSeekTextGenerator(system_prompt='Ты - профессиональный астролог'),
                prompt_builder=IdentityPromptBuilder(f"Составь ответ на вопрос, зачем в жизнь '{sign}' приходит человек со знаком '{sign2}'. Используй структуру: описание пары, что получает первый, что получает второй, опасности и вызовы союза, ключ к успеху")
            )
        )
        processor = TagAdder(['#гороскоп', '#астрология', f"#{sign}"])
        posters = [
            # TelegramPoster(chat_id=tg_chat_id, processor=processor),
            VkPoster(group_id=vk_group_id, processor=processor)
            # VkPoster(group_id=None, processor=processor)
        ]
        super().__init__(builder, posters)

def post_real(sign2):
    bloggers = [
        SignHoroscopeBlogger(sign='рыбы', tg_chat_id=consts.tg_pisces, vk_group_id=consts.vk_pisces, sign2=sign2),
        SignHoroscopeBlogger(sign='овен', tg_chat_id=consts.tg_aries, vk_group_id=consts.vk_aries, sign2=sign2),
        SignHoroscopeBlogger(sign='телец', tg_chat_id=consts.tg_taurus, vk_group_id=consts.vk_taurus, sign2=sign2),
        SignHoroscopeBlogger(sign='близнецы', tg_chat_id=consts.tg_gemini, vk_group_id=consts.vk_gemini, sign2=sign2),
        SignHoroscopeBlogger(sign='рак', tg_chat_id=consts.tg_cancer, vk_group_id=consts.vk_cancer, sign2=sign2),
        SignHoroscopeBlogger(sign='лев', tg_chat_id=consts.tg_leo, vk_group_id=consts.vk_leo, sign2=sign2),
        SignHoroscopeBlogger(sign='дева', tg_chat_id=consts.tg_virgo, vk_group_id=consts.vk_virgo, sign2=sign2),
        SignHoroscopeBlogger(sign='весы', tg_chat_id=consts.tg_libra, vk_group_id=consts.vk_libra, sign2=sign2),
        SignHoroscopeBlogger(sign='скорпион', tg_chat_id=consts.tg_scorpio, vk_group_id=consts.vk_scorpio, sign2=sign2),
        SignHoroscopeBlogger(sign='стрелец', tg_chat_id=consts.tg_sagittarius, vk_group_id=consts.vk_sagittarius, sign2=sign2),
        SignHoroscopeBlogger(sign='козерог', tg_chat_id=consts.tg_capricorn, vk_group_id=consts.vk_capricorn, sign2=sign2),
        SignHoroscopeBlogger(sign='водолей', tg_chat_id=consts.tg_aquarius, vk_group_id=consts.vk_aquarius, sign2=sign2),
    ]

    for blogger in bloggers:
        blogger.post()

def post():
    today = date.today()
    match (today.day, today.month):
        case (19, 2): post_real('рыбы')
        case (21, 3): post_real('овен')
        case (21, 4): post_real('телец')
        case (21, 5): post_real('близнецы')
        case (22, 6): post_real('рак')
        case (23, 7): post_real('лев')
        case (23, 8): post_real('дева')
        case (23, 9): post_real('весы')
        case (23, 10): post_real('скорпион')
        case (23, 11): post_real('стрелец')
        case (22, 12): post_real('козерог')
        case (20, 1): post_real('водолей')

if __name__ == "__main__":
    post()    
