from django.core.paginator import Paginator
from . import constants as const


def paginate_page(request, posts):
    paginator = Paginator(posts, const.PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
