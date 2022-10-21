from os import write
from tabnanny import check
import pandas as pd
import streamlit as st



st.title(
    'AutoCust'
    )

st.sidebar.title('Serviços')
psd = st.sidebar.selectbox('selecione uma opção',[' ','Tabela de gastos','Calculadora de Rendimento','Preços','Calendário' ])

if  psd == ' ':
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
    with st.form(key='Rendimento'):
             input_litros = st.number_input(label='insira a quantidade de litros',step=0.5)
             input_km = st.number_input(label='insira a kilometragem percorrida',step=0.5)
             calculo = ((input_litros)/(input_km))
             botao = form.form_submit_button("calcular")
             
    if botão:
            st.write(f'Litros: {input_litros}')
            st.write(f'Kilometragem percorrida: {input_km}')
            st.write(f'Rendimento: {calculo}')
            cliente.litors = input_litors
            cliente.km = input_km
            cliente.calculo = calculo
            
if psd == 'Preços':
    st.title('Preços:')
elif psd == 'Calendário':
    st.title('Calendário:')   


       

st.sidebar.title('Minha Conta')
st.sidebar.selectbox('selecione uma opção',['Conta','Informações Pessoais' ])  
        





