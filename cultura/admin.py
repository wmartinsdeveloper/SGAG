from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(cultura)
class CulturaAdmin(admin.ModelAdmin):
    ...
    
# @admin.register(categoria_produto)
# class Categoria_ProdutoAdmin(admin.ModelAdmin):
#     ...
    
# @admin.register(produto)
# class ProdutoAdmin(admin.ModelAdmin):
#     ...
    
# @admin.register(preco_produto)
# class Preco_ProdutoAdmin(admin.ModelAdmin):
#     ...

    
# @admin.register(categoria_servico)
# class Categoria_ServicoAdmin(admin.ModelAdmin):
#     ...
    
# @admin.register(servico)
# class ServicoAdmin(admin.ModelAdmin):
#     ...   
    
# @admin.register(preco_servico)
# class Preco_ServicoAdmin(admin.ModelAdmin):
#     ...

# @admin.register(manejo)
# class ManejoAdmin(admin.ModelAdmin):
#     ...

# @admin.register(manejo_produto)
# class Manejo_ProdutoAdmin(admin.ModelAdmin):
#     ...

# @admin.register(manejo_servico)
# class Manejo_ServicoAdmin(admin.ModelAdmin):
#     ...

# @admin.register(plantio)
# class plantioAdmin(admin.ModelAdmin):
#     ...

# @admin.register(producao)
# class ProducaoAdmin(admin.ModelAdmin):
#     ...

# @admin.register(categoria_receita)
# class Categoria_ReceitaAdmin(admin.ModelAdmin):
#     ...

# @admin.register(receita)
# class ReceitaAdmin(admin.ModelAdmin):
#     ...

# @admin.register(receita_producao)
# class Receita_ProducaoAdmin(admin.ModelAdmin):
#     ...

# @admin.register(receita_produto)
# class Receita_ProdutoAdmin(admin.ModelAdmin):
#     ...

# @admin.register(receita_servico)
# class Receita_ServicoAdmin(admin.ModelAdmin):
#     ...

# @admin.register(categoria_despesa)
# class Categoria_DespesaAdmin(admin.ModelAdmin):
#     ...

# @admin.register(despesa)
# class DespesaAdmin(admin.ModelAdmin):
#     ...

# @admin.register(despesa_producao)
# class Despesa_ProducaoAdmin(admin.ModelAdmin):
#     ...

# @admin.register(despesa_produto)
# class Despesa_ProdutoAdmin(admin.ModelAdmin):
#     ...

# @admin.register(despesa_servico)
# class Despesa_ServicoAdmin(admin.ModelAdmin):
#     ...


