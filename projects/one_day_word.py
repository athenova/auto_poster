from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import SimplestBlogger
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.task import ITaskBuilder
from simple_blogger.builder.prompt import TaskPromptBuilder, ContentBuilderPromptBuilder
from simple_blogger.builder.content import CachedContentBuilder, ContentBuilder
from simple_blogger.cache.file_system import FileCache
import tempfile,uuid

class IdentityTaskBuilder(ITaskBuilder):
    def __init__(self, task):
        self.task = task

    def build(self):
        return self.task

class WordBlogger(SimplestBlogger):
    def _system_prompt(self):
        return 'Ты - знаток русского языка, интересуешься новыми словами, знаешь значения старомодных слов, их этимологию и интересные факты, связанные со словами'
    
    def _prompt_constructor(self, task):
        return "Выбери одно рандомное слово из рандомной области. Объясни его значение, приведи пример использования и интересный факт, связанный с этим словом. Используй смайлики и не более 150 слов."

    def __init__(self):
        task_builder = IdentityTaskBuilder('.')
        file_suffix = str(uuid.uuid4())
        message_builder=CachedContentBuilder(
            task_builder=task_builder,
            path_constructor=lambda task:'.',
            builder=ContentBuilder(
                generator=self._message_generator(),
                prompt_builder=TaskPromptBuilder(
                        task_builder=task_builder,
                        prompt_constructor=self._prompt_constructor
                    )
            ),
            force_rebuild=False,
            cache=FileCache(root_folder=tempfile.gettempdir(), is_binary=False),
            filename=f"text_{file_suffix}"
        )
        image_builder=ContentBuilder(
            generator=self._image_generator(), 
            prompt_builder=ContentBuilderPromptBuilder(
                content_builder=message_builder
            )
        )
        builder = PostBuilder(
            message_builder=message_builder,
            media_builder=image_builder
        )
        tagadder = TagAdder(['#новыеслова', '#развитие'])
        posters = [
            TelegramPoster(chat_id='@one_day_word', processor=tagadder),
            VkPoster(group_id='230174990', processor=tagadder)
        ]
        super().__init__(builder, posters)


def handle():
    blogger = WordBlogger()
    blogger.post()
