from django.template import Library
from utils import utils

register = Library()

@register.filter
def formata_preco(value):
    return utils.formata_preco_utils(value)

@register.filter
def cart_total_qtd(carrinho):
    return utils.cart_total_qtd(carrinho)