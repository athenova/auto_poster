from datetime import datetime, timedelta
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import SimplestBlogger
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.generator.yandex import YandexTextGenerator
from simple_blogger.generator.openai import OpenAiTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder
from datetime import datetime, timedelta, date
import consts

class HoroscopeBlogger(SimplestBlogger):
    def __init__(self, sign, tg_chat_id, vk_group_id, tag, prompt_template):
        builder = PostBuilder(
            message_builder=ContentBuilder(
                generator=OpenAiTextGenerator(system_prompt=f"Ты - профессиональный астролог"),
                prompt_builder=IdentityPromptBuilder((prompt_template % (sign)) + ". Используй смайлики. Не используй 'Ок','Конечно'" )
            )
        )
        processor = TagAdder(['#гороскоп', '#астрология', tag, f"#{sign}"])
        posters = [
            TelegramPoster(chat_id=tg_chat_id, processor=processor),
            VkPoster(group_id=vk_group_id, processor=processor)
        ]
        super().__init__(builder, posters)

def post(day=None):
    tomorrow = datetime.today() + timedelta(days=1)
    tomorrow_plus_7 = tomorrow + timedelta(days=7)
    tag = None
    prompt_template = None
    match day or tomorrow.weekday() + 1:
        case 1:
            tag = '#гороскопнанеделю'
            prompt_template = f"Составь гороскоп для знака '%s' на неделю {tomorrow.strftime('%Y-%m-%d')} - {tomorrow_plus_7.strftime('%Y-%m-%d')}. Используй структуру: общая энергия, работа и финансы, любовь и отношения, эмоции и здоровье"
        case 2:
            tag = '#пожеланиедня'
            prompt_template = f"Напиши пожелание дня для знака '%s' на {tomorrow.strftime('%Y-%m-%d')}. Используй структуру: пожелание дня, аффирмация дня"
        case 3:
            tag = '#настройдня'
            prompt_template = f"Напиши настрой дня для знака '%s' на {tomorrow.strftime('%Y-%m-%d')}. Используй структуру: настрой дня, аффирмация дня"
        case 4:
            tag = '#главныйвопрос'
            prompt_template = f"Напиши главный вопрос дня для знака '%s' на {tomorrow.strftime('%Y-%m-%d')}. Используй структуру: вопрос дня, как этот вопрос поможет"
        case 5:
            tag = '#посланиедня'
            prompt_template = f"Напиши послание дня для знака '%s' на {tomorrow.strftime('%Y-%m-%d')}. Используй структуру: послание дня, аффирмация дня"
        case 6: 
            tag = "#практикадня"
            prompt_template = f"Напиши практику дня для знака '%s' на {tomorrow.strftime('%Y-%m-%d')}. Используй структуру: практика дня, как выполнять, эффект"
        case 7:
            tag = "#талисмандня"
            prompt_template = f"Напиши, какой талисман дня у знака '%s' на {tomorrow.strftime('%Y-%m-%d')}. Используй следующую структуру: камень дня, растение-талисман, цвет свечи, аффирмация дня"

    # bloggers = [
    #     HoroscopeBlogger(sign='рыбы', tg_chat_id=None, vk_group_id=None, tag=tag, prompt_template=prompt_template),
    # ]
    bloggers = [
        HoroscopeBlogger(sign='рыбы', tg_chat_id=consts.tg_pisces, vk_group_id=consts.vk_pisces, tag=tag, prompt_template=prompt_template),
        HoroscopeBlogger(sign='овен', tg_chat_id=consts.tg_aries, vk_group_id=consts.vk_aries, tag=tag, prompt_template=prompt_template),
        HoroscopeBlogger(sign='телец', tg_chat_id=consts.tg_taurus, vk_group_id=consts.vk_taurus, tag=tag, prompt_template=prompt_template),
        HoroscopeBlogger(sign='близнецы', tg_chat_id=consts.tg_gemini, vk_group_id=consts.vk_gemini, tag=tag, prompt_template=prompt_template),
        HoroscopeBlogger(sign='рак', tg_chat_id=consts.tg_cancer, vk_group_id=consts.vk_cancer, tag=tag, prompt_template=prompt_template),
        HoroscopeBlogger(sign='лев', tg_chat_id=consts.tg_leo, vk_group_id=consts.vk_leo, tag=tag, prompt_template=prompt_template),
        HoroscopeBlogger(sign='дева', tg_chat_id=consts.tg_virgo, vk_group_id=consts.vk_virgo, tag=tag, prompt_template=prompt_template),
        HoroscopeBlogger(sign='весы', tg_chat_id=consts.tg_libra, vk_group_id=consts.vk_libra, tag=tag, prompt_template=prompt_template),
        HoroscopeBlogger(sign='скорпион', tg_chat_id=consts.tg_scorpio, vk_group_id=consts.vk_scorpio, tag=tag, prompt_template=prompt_template),
        HoroscopeBlogger(sign='стрелец', tg_chat_id=consts.tg_sagittarius, vk_group_id=consts.vk_sagittarius, tag=tag, prompt_template=prompt_template),
        HoroscopeBlogger(sign='козерог', tg_chat_id=consts.tg_capricorn, vk_group_id=consts.vk_capricorn, tag=tag, prompt_template=prompt_template),
        HoroscopeBlogger(sign='водолей', tg_chat_id=consts.tg_aquarius, vk_group_id=consts.vk_aquarius, tag=tag, prompt_template=prompt_template),
    ]

    for blogger in bloggers:
        blogger.post()

if __name__ == "__main__":
    post()