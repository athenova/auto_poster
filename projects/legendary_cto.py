from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder

class LegendaryCtoBlogger(Journalist):
    def _system_prompt(self):
        return f"Ты - технический директор, лидер команды со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора"
    
    def _prompt_constructor(self, _):
        return "Расскажи про одного рандомного известного CTO из рандомной компании. Приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов."

    def __init__(self):
        tagadder = TagAdder(['#cto', '#it', '#ит', '#айти', '#легенды'])
        posters = [
            TelegramPoster(chat_id='@cto_in_fire', processor=tagadder),
            VkPoster(group_id='229837981', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post():
    blogger = LegendaryCtoBlogger()
    blogger.post()
