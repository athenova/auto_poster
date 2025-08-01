from simple_blogger.blogger import SimplestBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder

def post():
    processor = TagAdder(['#мама', '#ятебялюблю', '#тысамаялучшая'])

    blogger = SimplestBlogger(
        builder = PostBuilder(
                message_builder=ContentBuilder(
                    generator=DeepSeekTextGenerator(system_prompt='Ты - осознанная дочь, у тебя большая обида на мать за ошибки, совершённые в детстве, но ты хочешь восстановить хорошие отношения'),
                    prompt_builder=IdentityPromptBuilder(f"Пожелай хорошего дня матери, используй смайлики, не используй 'Конечно'")
                )
            ),
        posters = [
                TelegramPoster(chat_id='-1002400088805', processor=processor),
                VkPoster(group_id='229995349', processor=processor)
            ]
    )

    blogger.post()