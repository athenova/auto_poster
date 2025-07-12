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
    def __init__(self, sign, tg_chat_id, vk_group_id):
        tomorrow = datetime.today() + timedelta(days=1)
        builder = PostBuilder(
            message_builder=ContentBuilder(
                generator=OpenAiTextGenerator(system_prompt=f"Ты - профессиональный таролог"),
                prompt_builder=IdentityPromptBuilder(f"Какое настроение дня у знака '{sign}' на {tomorrow.strftime('%Y-%m-%d')}. Используй следующую структуру: Карта дня, что чувствуют, с чем связано, что поможет. Используй смайлики. Не используй 'Ок','Конечно'")
            )
        )
        processor = TagAdder(['#таро', '#настроениедня', f"#{sign}"])
        posters = [
            TelegramPoster(chat_id=tg_chat_id, processor=processor),
            VkPoster(group_id=vk_group_id, processor=processor)
        ]
        super().__init__(builder, posters)

def post():
    # bloggers = [
    #     TarotBlogger(sign='рыбы', tg_chat_id=None, vk_group_id=None),
    # ]
    bloggers = [
        TarotBlogger(sign='рыбы', tg_chat_id=consts.tg_pisces, vk_group_id=consts.vk_pisces),
        TarotBlogger(sign='овен', tg_chat_id=consts.tg_aries, vk_group_id=consts.vk_aries),
        TarotBlogger(sign='телец', tg_chat_id=consts.tg_taurus, vk_group_id=consts.vk_taurus),
        TarotBlogger(sign='близнецы', tg_chat_id=consts.tg_gemini, vk_group_id=consts.vk_gemini),
        TarotBlogger(sign='рак', tg_chat_id=consts.tg_cancer, vk_group_id=consts.vk_cancer),
        TarotBlogger(sign='лев', tg_chat_id=consts.tg_leo, vk_group_id=consts.vk_leo),
        TarotBlogger(sign='дева', tg_chat_id=consts.tg_virgo, vk_group_id=consts.tg_virgo),
        TarotBlogger(sign='весы', tg_chat_id=consts.tg_libra, vk_group_id=consts.vk_libra),
        TarotBlogger(sign='скорпион', tg_chat_id=consts.tg_scorpio, vk_group_id=consts.vk_scorpio),
        TarotBlogger(sign='стрелец', tg_chat_id=consts.tg_sagittarius, vk_group_id=consts.vk_sagittarius),
        TarotBlogger(sign='козерог', tg_chat_id=consts.tg_capricorn, vk_group_id=consts.vk_capricorn),
        TarotBlogger(sign='водолей', tg_chat_id=consts.tg_aquarius, vk_group_id=consts.vk_aquarius),
    ]

    for blogger in bloggers:
        blogger.post()

if __name__ == "__main__":
    post()