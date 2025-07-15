from simple_blogger.blogger import SimplestBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder

def post():
    processor = TagAdder(['#доча', '#ятебялюблю', '#тысамаялучшая'])

    blogger = SimplestBlogger(
        builder = PostBuilder(
                message_builder=ContentBuilder(
                    generator=DeepSeekTextGenerator(system_prompt='Ты - осознанная мать, ты много раз ошибалась в воспитании детей, но теперь хочешь восстановить хорошие отношения'),
                    prompt_builder=IdentityPromptBuilder(f"Пожелай хорошего дня дочери, используй смайлики, не используй 'Конечно'")
                )
            ),
        posters = [
                TelegramPoster(chat_id='-1002421248289', processor=processor),
                VkPoster(group_id='229995285', processor=processor)
            ]
    )

    blogger.post()