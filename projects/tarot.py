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

class TarotBlogger(SimplestBlogger):
    def __init__(self, sign, tg_chat_id, vk_group_id, tag, prompt_template):
        builder = PostBuilder(
            message_builder=ContentBuilder(
                generator=OpenAiTextGenerator(system_prompt=f"Ты - профессиональный таролог"),
                prompt_builder=IdentityPromptBuilder((prompt_template % (sign)) + ". Используй смайлики. Не используй 'Ок','Конечно'")
            )
        )
        processor = TagAdder(['#таро', tag, f"#{sign}"])
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
            tag = '#таронанеделю'
            prompt_template = f"Составь тароскоп для знака '%s' на неделю {tomorrow.strftime('%Y-%m-%d')} - {tomorrow_plus_7.strftime('%Y-%m-%d')}. Используй структуру: Энергия недели, Вызов, Подсказка или ресурс"
        case 2:
            tag = '#советдня'
            prompt_template = f"Дай совет дня для знака '%s' на {tomorrow.strftime('%Y-%m-%d')}. Используй следующую структуру: Карта дня, послание, совет, предупреждение"
        case 3:
            tag = '#цветдня'
            prompt_template = f"Какой цвет дня для знака '%s' на {tomorrow.strftime('%Y-%m-%d')}. Используй следующую структуру: Карта дня, цвет дня, почему, как использовать"
        case 4:
            tag = '#энергиядня'
            prompt_template = f"Какая энергия дня для знака '%s' на {tomorrow.strftime('%Y-%m-%d')}. Используй следующую структуру: Карта дня, общая характеристика, энергия" 
        case 5:
            tag = '#настроениедня'
            prompt_template = f"Какое настроение дня у знака '%s' на {tomorrow.strftime('%Y-%m-%d')}. Используй следующую структуру: Карта дня, что чувствуют, с чем связано, что поможет"
        case 6:
            tag = '#аркандня'
            prompt_template = f"Какой аркан дня для знака '%s' на {tomorrow.strftime('%Y-%m-%d')}. Используй следующую структуру: значение, что несёт, совет"
        case 7:
            tag = '#ритуалдня'
            prompt_template = f"Какой ритуал дня для знака '%s' на {tomorrow.strftime('%Y-%m-%d')}. Используй следующую структуру: ритуал, что понадобится, как провести, что даёт"


    # bloggers = [
    #     TarotBlogger(sign='рыбы', tg_chat_id=None, vk_group_id=None, tag=tag, prompt_template=prompt_template),
    # ]
    bloggers = [
        TarotBlogger(sign='рыбы', tg_chat_id=consts.tg_pisces, vk_group_id=consts.vk_pisces, tag=tag, prompt_template=prompt_template),
        TarotBlogger(sign='овен', tg_chat_id=consts.tg_aries, vk_group_id=consts.vk_aries, tag=tag, prompt_template=prompt_template),
        TarotBlogger(sign='телец', tg_chat_id=consts.tg_taurus, vk_group_id=consts.vk_taurus, tag=tag, prompt_template=prompt_template),
        TarotBlogger(sign='близнецы', tg_chat_id=consts.tg_gemini, vk_group_id=consts.vk_gemini, tag=tag, prompt_template=prompt_template),
        TarotBlogger(sign='рак', tg_chat_id=consts.tg_cancer, vk_group_id=consts.vk_cancer, tag=tag, prompt_template=prompt_template),
        TarotBlogger(sign='лев', tg_chat_id=consts.tg_leo, vk_group_id=consts.vk_leo, tag=tag, prompt_template=prompt_template),
        TarotBlogger(sign='дева', tg_chat_id=consts.tg_virgo, vk_group_id=consts.vk_virgo, tag=tag, prompt_template=prompt_template),
        TarotBlogger(sign='весы', tg_chat_id=consts.tg_libra, vk_group_id=consts.vk_libra, tag=tag, prompt_template=prompt_template),
        TarotBlogger(sign='скорпион', tg_chat_id=consts.tg_scorpio, vk_group_id=consts.vk_scorpio, tag=tag, prompt_template=prompt_template),
        TarotBlogger(sign='стрелец', tg_chat_id=consts.tg_sagittarius, vk_group_id=consts.vk_sagittarius, tag=tag, prompt_template=prompt_template),
        TarotBlogger(sign='козерог', tg_chat_id=consts.tg_capricorn, vk_group_id=consts.vk_capricorn, tag=tag, prompt_template=prompt_template),
        TarotBlogger(sign='водолей', tg_chat_id=consts.tg_aquarius, vk_group_id=consts.vk_aquarius, tag=tag, prompt_template=prompt_template),
    ]

    for blogger in bloggers:
        blogger.post()

if __name__ == "__main__":
    post()