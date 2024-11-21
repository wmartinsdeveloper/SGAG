from django.db import models

# Create your models here.
class UnidadeTempo:
    Tempo = (
        ("Dia(s)", "Dia(s)"),
        ("Semana(s)", "Semana(s)"),
        ("Mês(s)", "Mês(s)"),
        ("Ano(s)", "Ano(s)")
    ) 


class cultura(models.Model):
    cultura = models.TextField(primary_key=True)
    ciclovida = models.IntegerField(default=0)
    unidadeciclovida = models.CharField(choices=UnidadeTempo().Tempo, default='Dia(s)',max_length=10)
    inicioproducao = models.IntegerField(default=0)
    unidadeinicioproducao = models.CharField(choices=UnidadeTempo().Tempo, default='Dia(s)',max_length=10)
    cicloproducao = models.IntegerField(default=0)
    unidadecicloproducao = models.CharField(choices=UnidadeTempo().Tempo, default='Dia(s)',max_length=10)
    quantidadesafra = models.IntegerField(default=0)
    entressafra = models.IntegerField(default=0)
    unidadeentressafra = models.CharField(choices=UnidadeTempo().Tempo, default='Dia(s)',max_length=10)
    intervalocolheita = models.IntegerField(default=0)
    unidadeintervalocolheita = models.CharField(choices=UnidadeTempo().Tempo, default='Dia(s)',max_length=10)
    embalagem = models.CharField(max_length=50, blank=False)
    pesovenda = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    safraunica = models.BooleanField(default=False)   
     
    def __str__(self):
        return self.nome
    
    
# #==============================================================================================================================================  
# # Modelos de dados para Produtos    

# class categoria_produto(models.Model):
#     nome = models.CharField(max_length=255, primary_key=True)
#     descricao = models.TextField()       
#     def __str__(self):
#         return self.nome     
        
# class produto(models.Model):
#     nome = models.CharField(max_length=255, primary_key=True)
#     descricao = models.TextField()
#     categoriaproduto = models.ForeignKey( categoria_produto, on_delete=models.SET_NULL, null=True, related_name='produto_categoria')
#     peso = models.DecimalField(max_digits=10, decimal_places=2,default=0)
#     unidadepeso = models.CharField(max_length=10)
#     revenda = models.BooleanField(default=False)
#     def __str__(self):
#         return self.nome 

# class preco_produto(models.Model):
#     id = models.AutoField(primary_key=True)
#     data =  models.DateField()
#     preco =  models.DecimalField(max_digits=10, decimal_places=2,default=0) 
#     produto = models.ForeignKey( produto, on_delete=models.CASCADE, null=True, related_name='preco_produto')              
#     def __str__(self):
#         return self.data
# #==============================================================================================================================================  
# # Modelos de dados para Atividade e Serviços      

# class categoria_servico(models.Model):
#     nome = models.CharField(max_length=255, primary_key=True)
#     descricao = models.TextField()    
#     def __str__(self):
#         return self.nome
   
# class servico(models.Model):
#     nome = models.CharField(max_length=255, primary_key=True)
#     descricao = models.TextField(default="")
#     categoriaproduto = models.ForeignKey( categoria_servico, on_delete=models.SET_NULL, null=True, related_name='servico_categoria')
#     def __str__(self):
#         return self.nome
       
# class preco_servico(models.Model):
#     id = models.AutoField(primary_key=True)
#     data =  models.DateField()
#     preco =  models.DecimalField(max_digits=10, decimal_places=2,default=0) 
#     produto = models.ForeignKey( servico, on_delete=models.CASCADE, null=True, related_name='preco_servico')     
#     def __str__(self):
#         return self.data      
 


      
# #==============================================================================================================================================  
# # Modelos de dados para Manejo
        
# class manejo(models.Model):
#     nome = models.CharField(max_length=255, primary_key=True)
#     data = models.DateField() 
#     descricao = models.TextField(default="") 
#     cultura = models.ForeignKey(cultura, on_delete=models.SET_NULL, null=True, related_name='cultura')
#     produto = models.ManyToManyField(produto, related_name='manejo', through="manejo_produto")
#     servico = models.ManyToManyField(servico, related_name='servico', through="manejo_servico")
#     def __str__(self):
#         return self.nome    
    
# class manejo_produto(models.Model):
#     id = models.AutoField(primary_key=True)
#     data = models.DateField(blank=True) 
#     manejo = models.ForeignKey(manejo,  on_delete=models.CASCADE, related_name='manejo_produto_manejo')
#     produto = models.ForeignKey(produto, on_delete=models.CASCADE, related_name='manejo_produto')
#     reinvestimento = models.BooleanField(default=False) 
#     descricao = models.TextField(default="") 
#     utilizacao = models.TextField(default="") 
#     def __str__(self):
#        return self.id  
   
# class manejo_servico(models.Model):
#     id = models.AutoField(primary_key=True)
#     data = models.DateField(blank=True) 
#     manejo = models.ForeignKey(manejo,  on_delete=models.CASCADE, related_name='manejo_servico_manejo')
#     servico = models.ForeignKey(servico, on_delete=models.CASCADE, related_name='manejo_servico')
#     descricao = models.TextField(default="") 
#     utilizacao = models.TextField(default="") 
#     def __str__(self):
#         return self.id
 

      
# class plantio(models.Model):
#     nome = models.CharField(max_length=255, primary_key=True)
#     datainicio = models.DateField(blank=True) 
#     datafim = models.DateField(blank=True) 
#     medidaarea = models.CharField(max_length=100)
#     descricao = models.TextField(default="") 
#     quantidadeplanta = models.IntegerField()
#     manejo = models.ForeignKey(manejo,  on_delete=models.SET_NULL, related_name='plantio_manejo',null=True)    
#     def __str__(self):
#         return self.nome
        
# class producao(models.Model):
#     id = models.AutoField(primary_key=True)
#     data = models.DateField(blank=True) 
#     quantidade = models.IntegerField()
#     unidadeproducao = models.CharField(max_length=50)
#     precovenda = models.DecimalField(max_digits=10, decimal_places=2,default=0)
#     plantio = models.ForeignKey(plantio,  on_delete=models.SET_NULL, related_name='plantio',null=True) 
#     def __str__(self):
#         return self.id   
    
# #==============================================================================================================================================  
# # Modelos de dados para Financeiro - Receita

# class categoria_receita(models.Model):
#     nome = models.CharField(max_length=255, primary_key=True)
#     descricao = models.TextField()  
#     def __str__(self):
#         return self.nome
    
# class receita(models.Model):
#     id = models.IntegerField(primary_key=True)
#     data = models.DateField()
#     categoriareceita = models.ForeignKey( categoria_receita, on_delete=models.SET_NULL, null=True, related_name='receita_categoria') 
#     producao = models.ManyToManyField(producao, related_name='receita_producao', through="receita_producao")   
#     produto = models.ManyToManyField(produto, related_name='receita_produto', through="receita_produto")   
#     servico = models.ManyToManyField(servico, related_name='receita_servico', through="receita_servico")   
#     def __str__(self):
#         return self.id
 
   
# class receita_producao(models.Model):
#     id = models.IntegerField(primary_key=True)
#     data = models.DateField()    
#     receita = models.ForeignKey( receita, on_delete=models.SET_NULL, null=True, related_name='receita_producao_receita')
#     valor = models.DecimalField(max_digits=10, decimal_places=2,default=0) 
#     producao = models.ForeignKey(producao, on_delete=models.SET_NULL, null=True, related_name='receita_producao_producao')
#     def __str__(self):
#         return self.id    

# class receita_produto(models.Model):
#     id = models.IntegerField(primary_key=True)
#     data = models.DateField()    
#     receita = models.ForeignKey( receita, on_delete=models.SET_NULL, null=True, related_name='receita_produto_receita')
#     valor = models.DecimalField(max_digits=10, decimal_places=2,default=0) 
#     produto = models.ForeignKey(produto, on_delete=models.SET_NULL, null=True, related_name='receita_produto_produto')
#     def __str__(self):
#         return self.id    
    
# class receita_servico(models.Model):
#     id = models.IntegerField(primary_key=True)
#     data = models.DateField()    
#     receita = models.ForeignKey( receita, on_delete=models.SET_NULL, null=True, related_name='receita_servico_receita')
#     valor = models.DecimalField(max_digits=10, decimal_places=2,default=0) 
#     servico = models.ForeignKey(servico, on_delete=models.SET_NULL, null=True, related_name='receita_servico_servico')
#     def __str__(self):
#         return self.id
        
# #==============================================================================================================================================  
# # Modelos de dados para Financeiro - Despesas



# class categoria_despesa(models.Model):
#     nome = models.CharField(max_length=255, primary_key=True)
#     descricao = models.TextField()  
#     def __str__(self):
#         return self.nome
    
# class despesa(models.Model):
#     id = models.IntegerField(primary_key=True)
#     data = models.DateField()
#     categoriadespesa = models.ForeignKey( categoria_despesa, on_delete=models.SET_NULL, null=True, related_name='despesa_categoria') 
#     producao = models.ManyToManyField(producao, related_name='despesa_producao', through="despesa_producao")   
#     produto = models.ManyToManyField(produto, related_name='despesa_produto', through="despesa_produto")   
#     servico = models.ManyToManyField(servico, related_name='despesa_servico', through="despesa_servico")   
#     def __str__(self):
#         return self.id
    
# class despesa_producao(models.Model):
#     id = models.IntegerField(primary_key=True)
#     data = models.DateField()    
#     despesa = models.ForeignKey( despesa, on_delete=models.SET_NULL, null=True, related_name='despesa_producao_despesa')
#     valor = models.DecimalField(max_digits=10, decimal_places=2,default=0) 
#     producao = models.ForeignKey(producao, on_delete=models.SET_NULL, null=True, related_name='despesa_producao_producao')
#     def __str__(self):
#         return self.id    

# class despesa_produto(models.Model):
#     id = models.IntegerField(primary_key=True)
#     data = models.DateField()    
#     despesa = models.ForeignKey( despesa, on_delete=models.SET_NULL, null=True, related_name='despesa_produto_despesa')
#     valor = models.DecimalField(max_digits=10, decimal_places=2,default=0) 
#     produto = models.ForeignKey(produto, on_delete=models.SET_NULL, null=True, related_name='despesa_produto_produto')
#     def __str__(self):
#         return self.id    
    
# class despesa_servico(models.Model):
#     id = models.IntegerField(primary_key=True)
#     data = models.DateField()    
#     despesa = models.ForeignKey( despesa, on_delete=models.SET_NULL, null=True, related_name='despesa_servico_despesa')
#     valor = models.DecimalField(max_digits=10, decimal_places=2,default=0) 
#     servico = models.ForeignKey(servico, on_delete=models.SET_NULL, null=True, related_name='despesa_servico_servico')
#     def __str__(self):
#         return self.id  