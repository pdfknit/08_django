from django import template

register = template.Library()

@register.simple_tag
def sample(string):
    return f'sample {string}'

@register.filter(name="sample_filter")
def sample(string):
    return f'filter {string}'

@register.filter(name="phone_number")
def phone_number(string):
    if len(string) == 7:
        return f'{string[0:3]}-{string[3:5]}-{string[5:7]}'

    if string[0] == '8' and len(string) == 11:
        return f'+7-{string[1:4]}-{string[4:7]}-{string[7:9]}-{string[9:11]}'

    if string[0] == '+' and len(string) == 12:
        return f'+7-{string[1:4]}-{string[4:7]}-{string[7:9]}-{string[9:11]}'

@register.filter(name="price_filter")
def price_filter(string):
    without_coins = str(string).split('.')[0]
    if len(without_coins) >= 5:
        without_coins = f'{without_coins[0:len(without_coins)-3]} {without_coins[len(without_coins)-3:len(without_coins)]}'
    return without_coins