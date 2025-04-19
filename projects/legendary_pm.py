from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder

class LegendaryPmBlogger(Journalist):
    def _system_prompt(self):
        return f"Ты - проектный менеджер, лидер проекта со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора"
    
    def _prompt_constructor(self, _):
        return "Расскажи про одного рандомного известного проектного менеджера из рандомной компании. Приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов."

    def __init__(self):
        tagadder = TagAdder(['#pm', '#projectmanagement', '#it', '#ит', '#айти', '#проблемы', '#легенды'])
        posters = [
            TelegramPoster(chat_id='@verge_of_breakdown', processor=tagadder),
            VkPoster(group_id='229837997', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post():
    blogger = LegendaryPmBlogger()
    blogger.post()