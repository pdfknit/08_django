MENU_LINKS = {'домой': '', 'продукты': 'products', 'контакты': 'contact'}


def menu_links(request):
    return { 'menu_links': MENU_LINKS,}
