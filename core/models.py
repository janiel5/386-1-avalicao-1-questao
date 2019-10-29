from django.db import models


# Create your models here.
class Despesa(models.Model):

    data_criacao = models.DateField("data da criação")
    CHOICE_TIPO_DESPESA = [("remedio", "Remédio"),
                           ("roupas",'Roupas'),
                           ("alimentacao","Alimentação"),
                           ("educacao", "Educação"),
                           ("transporte","Transporte"),
                           ("outros","Outros")]
    tipo_despesa = models.CharField("tipo de despesa",choices=CHOICE_TIPO_DESPESA, max_length=15)
    descricao = models.TextField("descrição")
    CHOICE_FORMA_PAGAMENTO = [("dinheiro","Dinheiro"),
                              ("cartao_credito","cartão de crédito"),
                              ("cartao_debito","cartão de débito"),
                              ("cartao_crediario","cartão  crediário"),
                              ("cheque","cheque")]
    forma_pagamento = models.CharField("forma de pagamento",choices=CHOICE_FORMA_PAGAMENTO, max_length=15)
    vencimento = models.DateField()
    quitado = models.BooleanField()

    ordering = ('forma_pagamento', 'vencimento')

    def __str__(self):
        return self.descricao
