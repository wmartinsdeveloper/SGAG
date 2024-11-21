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

class culturaform(forms.ModelForm):
        
    class Meta:
        model = cultura
        fields = '__all__' 
                
    cultura = forms. CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'ex.: Maracujá', 
                                            'class': 'tex-input'
                                            
                                            }
                                    ),
            label='Nome da Cultura',
            #help_text = ('Nome da cultura detalhada.'),
            error_messages = {'required':'O nome da cultura precisa ser preenchido !',
                              'invalid':'O nome da cultura já existe.'},
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
        form_cleaned = super().clean()
        if cultura.objects.filter(cultura=form_cleaned.get('cultura')).exists():
            raise ValidationError(
                'O nome %(value)s já existe',code='invalid',params={'value':form_cleaned.get('cultura')}
            )
        return form_cleaned
        

 