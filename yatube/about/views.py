from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['just_title'] = 'Об авторе'
        context['just_text'] = ('Добрый день! '
                                'Я студент факультета Бэкенд. Когорта 51. '
                                'Мои поекты можно посмотреть здесь '
                                'https://github.com/DemusActavius'
                                )
        return context


class AboutTechView(TemplateView):
    template_name = 'about/tech.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['just_title'] = 'Технологии'
        context['just_text'] = ('Для создания этой страницы мною были '
                                'использованы следующие инструменты:'
                                '1. IDE Visual Studio Cod. '
                                '2. Framework Django.'
                                '3. И куча бессонных ночей...'
                                )
        return context
