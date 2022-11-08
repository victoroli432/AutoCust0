from os import write
from tabnanny import check
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st



st.title(
    'AutoCust'
    )

st.sidebar.title('Serviços')
psd = st.sidebar.selectbox('selecione uma opção',['Selecione um Serviço ','Tabela de gastos','Calculadora de Rendimento','Indicadores','Calendário' ])

if  psd == 'Selecione um Serviço':
     st.header('Você esta na plataforma do AutoCust ')
     st.write('O melhor lugar para você se organizar, e ainda fazer sobrar aquela graninha ')
elif psd == 'Tabela de gastos':  
        with st.form(key='include categoria'):
           input_categoria = st.selectbox(label='selecione a categoria', options=['combustivel','mecanico','multa','outros']) 
           input_quantidade = st.number_input(label='insira a quantidade',step=0.5) 
           input_valor = st.number_input(label='insira o valor gasto', step=0.5) 
           input_button_submit = st.form_submit_button('enviar')
        if input_button_submit:
            st.write(f'Categoria: {input_categoria}')
            st.write(f'Quantidade: {input_quantidade}')
            st.write(f'Valor: {input_valor}') 
            cliente.categoria = input_categoria
            cliente.quantidade = input_quantidade
            cliente.valor = input_valor

            clientecontroller.incluir(cliente)
elif psd == 'Calculadora de Rendimento':
    st.title('Calculadora de Rendimento:') 
    with st.form(key='include preços'):
           input_combustivel = st.selectbox(label='selecione a categoria', options=['Gasolina','Etanol','outros']) 
           input_litros = st.number_input(label='insira a quantidade em Litros',step=0.5) 
           input_km = st.number_input(label='insira os KM percorridos', step=0.5) 
           input_button_submit = st.form_submit_button('enviar')
    if input_button_submit:
            st.write(f'Categoria: {input_combustivel}')
            st.write(f'Quantidade: {input_litros} Litros')
            st.write(f'QUilometros: {input_km} Km') 
            st.write(f'Redimento: {input_km/input_litros} Km por Litro')    
if psd == 'Indicadores':
    st.title('Indicadores:')
elif psd == 'Calendário':
    st.title('Calendário:')   
    st.header('Adicione um compromisso')
    with st.form(key='calendario'):
           input_compromisso = st.date_input(label='data do compromisso:') 
           input_nome = st.text_input(label='nome do compromisso')
           input_button_submit = st.form_submit_button('enviar')
    if input_button_submit:
            st.write(f'Compromisso: {input_compromisso}')
            st.write(f'Nome: {input_nome}')

       

st.sidebar.title('Minha Conta')
st.sidebar.selectbox('selecione uma opção',['Conta','Informações Pessoais' ])  
        





