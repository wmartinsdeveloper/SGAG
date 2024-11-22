from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from .models import cultura



UnidadeTempo = (
                    ("Dia(s)", "Dia(s)"),
                    ("Semana(s)", "Semana(s)"),
                    ("Mês(s)", "Mês(s)"),
                    ("Ano(s)", "Ano(s)")
                ) 

def cultura_existis(nome_cultura):
    if cultura.objects.filter(cultura=nome_cultura).exists():
        raise ValidationError(
            'O nome da cultura "%(value)s" já foi cadastrada.',
            code='invalid',
            params={'value': nome_cultura}
            )




class culturaform(forms.ModelForm):
        
    class Meta:
        model = cultura
        fields = '__all__' 
                
    cultura = forms.CharField (
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'ex.: Maracujá', 
                                            'class': 'tex-input',
                                            'required': True, 
                                            # 'maxlength': 400,                                                                                
                                            }
                                    ),
            label='Nome da Cultura',
            help_text = ('Nome da cultura detalhada.'),
            error_messages = {'required':'O nome da cultura precisa ser preenchido !', },
            required=True,
            max_length=100,
            min_length=5,
            validators=[cultura_existis]
        )
    ciclovida = forms.IntegerField(
        widget=forms.NumberInput(
                                attrs={
                                        'class': 'tex-input',
                                        'value':'0'
                                        }
                                ),
        label='Ciclo de Vida',
        #help_text = ('Tempo em que a cultura é cultivada'),
        error_messages = {'required':'É preciso informar o ciclo de vida da cultura !'},
        required=False,
        )  
    unidadeciclovida = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'tex-input'}),
        choices=UnidadeTempo,
        label='Unidade de Tempo',
        help_text = ('Medida de Tempo'),
        error_messages = {'required':'Selecione uma unidade de tempo'},
        required=False,
        )
  
    inicioproducao = forms.IntegerField(
        widget=forms.NumberInput(
                                attrs={
                                        'class': 'tex-input',
                                        'value':'0'
                                        }
                                ),
        label='Inicio Produção',
        help_text = ('Tempo em que a cultura inicia a produção'),
        error_messages = {'required':'É preciso informar o tempo de inicio da produção da cultura !'},
        required=False,
        )  
    unidadeinicioproducao = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'tex-input'}),
        choices=UnidadeTempo,
        label='Unidade de Tempo',
        help_text = ('Medida de Tempo'),
        error_messages = {'required':'Selecione uma unidade de tempo'},
        required=False,
        ) 
  
  
    cicloproducao = forms.IntegerField(
        widget=forms.NumberInput(
                                attrs={
                                        'class': 'tex-input',
                                        'value':'0'
                                        }
                                ),
        label='Ciclo Produtivo',
        help_text = ('Tempo de produção da cultura.'),
        error_messages = {'required':'É preciso informar o tempo de produção da cultura !'},
        required=False,
        ) 
   
    unidadecicloproducao = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'tex-input'}),
        choices=UnidadeTempo,
        label='Unidade de Tempo',
        help_text = ('Medida de Tempo'),
        error_messages = {'required':'Selecione uma unidade de tempo'},
        required=False,
        )  
    
    quantidadesafra = forms.IntegerField(
        widget=forms.NumberInput(
                                attrs={
                                        'class': 'tex-input',
                                        'value':'0'
                                        }
                                ),
        label='Quantidade de Safras',
        help_text = ('Quantidade Total de Safra.'),
        error_messages = {'required':'É preciso informar a quantidade de safras !'},
        required=False,
        )    
    
    entressafra = forms.IntegerField(
        widget=forms.NumberInput(
                                attrs={
                                        'class': 'tex-input',
                                        'value':'0'
                                        }
                                ),
        label='Periodo de Entressafra',
        help_text = ('Tempo de entressafra.'),
        error_messages = {'required':'É preciso informar o tempo da entressafra !'},
        required=False
        )    

    unidadeentressafra = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'tex-input'}),
        choices=UnidadeTempo,
        label='Unidade de Tempo',
        help_text = ('Medida de Tempo'),
        error_messages = {'required':'Selecione uma unidade de tempo'},
        required=False,
        )  

    intervalocolheita = forms.IntegerField(
        widget=forms.NumberInput(
                                attrs={
                                        'class': 'tex-input',
                                        'value':'0'
                                        }
                                ),
        label='Intervalo de Colheita',
        help_text = ('Intervalo de colheita da cultura.'),
        error_messages = {'required':'É preciso informar o intervalo da colheita da cultura !'},
        required=False,
        )  
    
    unidadeintervalocolheita = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'tex-input'}),
        choices=UnidadeTempo,
        label='Unidade de Tempo',
        help_text = ('Medida de Tempo'),
        error_messages = {'required':'Selecione uma unidade de tempo'},
        required=False,
        )      
 
    embalagem = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'ex.: Tela verde, caixa 15kg, saco 15kg', 
                                            'class': 'tex-input'
                                            }
                                    ),
            label='Embalagem',
            help_text = ('Embalagem de venda do produto'),
            error_messages = {'required':'O nome da cultura precisa ser preenchido !'},
            required=False,
        ) 
 
    pesovenda = forms.IntegerField(
        widget=forms.NumberInput(
                                attrs={
                                        'class': 'tex-input',
                                        'value':'0'
                                        }
                                ),
        label='Peso de Venda',
        help_text = ('Intervalo de colheita da cultura.'),
        error_messages = {'required':'É preciso informar o intervalo da colheita da cultura !'},
        required=False,
        ) 
    
    safraunica = forms.BooleanField(    
        widget=forms.CheckboxInput(attrs={'class':'tex-input'}),
        label='Safra Única',
        help_text = ('Medida de Tempo'),
        error_messages = {'required':'Selecione uma unidade de tempo'},
        required=False,
        )      
    


         
    def clean(self):
        form_cleaned = self.cleaned_data

        # Aplica strip() a todos os campos do formulário
        for key, value in form_cleaned.items():
            if isinstance(value, str):  # Verifica se o valor é uma string
                form_cleaned[key] = value.strip()  # Remove espaços em branco
        return form_cleaned
  
  
    #  Versão Final
    #   def clean(self):
    #     clutura_cleaned = self.cleaned_data.get('cultura','').strip()
    #     if cultura.objects.filter(cultura=clutura_cleaned).exists():
    #         raise ValidationError(
    #             'O nome da cultura "%(value)s" já foi cadastrada.',
    #             code='invalid',
    #             params={'value': clutura_cleaned}
    #             )
    #     else:
    #         form_cleaned = self.cleaned_data
    
    #         # Aplica strip() a todos os campos do formulário
    #         for key, value in form_cleaned.items():
    #             if isinstance(value, str):  # Verifica se o valor é uma string
    #                 form_cleaned[key] = value.strip()  # Remove espaços em branco
    #         return form_cleaned
  
  
  
  
    # def clean_cultura(self):
    #     form_cleaned = self.cleaned_data['cultura']
    #     if cultura.objects.filter(cultura=form_cleaned).exists():
    #         raise ValidationError(
    #             'O nome da cultura "%(value)s" já foi cadastrada.',
    #             code='invalid',
    #             params={'value': form_cleaned.get('cultura')}
    #             )
 
    #     return form_cleaned
    
    
        # def clean_cultura(self):
        # clutura_cleaned = self.cleaned_data.get('cultura','').strip()
        # if cultura.objects.filter(cultura=clutura_cleaned).exists():
        #     raise ValidationError(
        #         'O nome da cultura "%(value)s" já foi cadastrada.',
        #         code='invalid',
        #         params={'value': clutura_cleaned}
        #         )
        # else:
        #     form_cleaned = self.cleaned_data
    
        #     # Aplica strip() a todos os campos do formulário
        #     for key, value in form_cleaned.items():
        #         if isinstance(value, str):  # Verifica se o valor é uma string
        #             form_cleaned[key] = value.strip()  # Remove espaços em branco
        #     return clutura_cleaned