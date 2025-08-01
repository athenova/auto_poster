from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import SimplestBlogger
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder

def post():
    processor = TagAdder(['#хорошегоднявсем'])

    blogger = SimplestBlogger(
        builder = PostBuilder(
                message_builder=ContentBuilder(
                    generator=DeepSeekTextGenerator(system_prompt='Ты - самый оптимистичный в мире человек'),
                    prompt_builder=IdentityPromptBuilder(f"Пожелай отличного дня всему миру, используй смайлики, не используй 'Конечно'")
                )
            ),
        posters = [
                TelegramPoster(chat_id='-1002360046037', processor=processor),
                VkPoster(group_id='229838092', processor=processor)
            ]
    )

    blogger.post()