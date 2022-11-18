import streamlit as st
from PIL import Image
import string
import random
import pandas as pd
from datetime import date, datetime
import webbrowser
import sqlite3
import time

#Login

#criando senha
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False


#criando banco de dados
conn = sqlite3.connect('Banco.db')
c = conn.cursor()

#Banco de dados 
def create_user():
	c.execute('CREATE TABLE IF NOT EXISTS user(username TEXT, password TEXT)')

def create_gastos():
      c.execute('CREATE TABLE IF NOT EXISTS gastos(categoria TEXT, quantidade INTEGER, valor INTEGER)')         

def add_user(username,password):
	c.execute('INSERT INTO user(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def add_gastos(input_categoria,input_quantidade,input_valor):
      c.execute('INSERT INTO gastos(categoria,quantidade,valor) VALUES (?,?,?)',(input_categoria,input_quantidade,input_valor))
      conn.commit()

def excluir_user(username,password):
	c.execute('DELETE from user WHERE username =? AND password =?',(username,password))
	conn.commit()
	conn.close()

def login_user(username,password):
	c.execute('SELECT * FROM user WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def view_all_user():
	c.execute('SELECT * FROM user')
	data = c.fetchall()
	return data

def view_all_gastos():
      c.execute('SELECT * FROM gastos')
      data = c.fetchall()
      return data



st.title('AutoCust')


#Site area de Login/cadastro

opções = ['Cadastro','Login']

st.sidebar.title('Cadastro/Login:')
all = st.sidebar.selectbox('selecione uma Opção',opções)

if all == 'Cadastro':
      st.sidebar.subheader("Faça parte do grupo AutoCust")
      new_user = st.sidebar.text_input("Nome")
      new_password = st.sidebar.text_input("Senha",type='password')
      if st.sidebar.button("Cadastre-se"):
            create_user()
            add_user(new_user,make_hashes(new_password))
            with st.spinner("Seu cadastro foi realizado com sucesso,Vá para a área de login"):
                   time.sleep(2)            

      st.subheader('soutinho vai me ama')
                  
elif all == 'Login':
      st.sidebar.subheader("Página do Login")
      username = st.sidebar.text_input("Nome")
      password = st.sidebar.text_input("Senha",type='password')
      if st.sidebar.checkbox("Logar"):
            create_user()
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:
                  with st.spinner("Bem vindo {}".format(username)):
                              time.sleep(0.5)

                       
                        


                  



#Pagina Pós Login

                  Menu = ['','Tabela de gastos','Calculadora de Rendimento','Indicadores','Calendário']

                  st.sidebar.title('Serviços')
                  psd = st.sidebar.selectbox('selecione um Serviço',Menu)


            else:
                  st.warning("Nome/Senha incorretos ou acesso negado")





# Area dos Serviços 

      if  psd == '':  
            st.write('O melhor site de todos')
            st.write('Você esta na plataforma do AutoCust ')
            st.write('O melhor lugar para você se organizar, e ainda fazer sobrar aquela graninha ')
 
      elif psd == 'Tabela de gastos':  
            st.title('Tabela de Gastos:')  
            input_categoria = st.selectbox(label='selecione a categoria', options=['combustivel','mecanico','multa','outros']) 
            input_quantidade = st.number_input(label='insira a quantidade',step=0.5) 
            input_valor = st.number_input(label='insira o valor gasto', step=0.5) 
            if st.button("enviar"):
             create_gastos()
             add_gastos(input_categoria,input_quantidade,input_valor)
            st.success("Seu cadastro foi realizado com sucesso")

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
                  input_nome = st.text_input(label='nome do compromisso', max_chars=50)
                  input_button_submit = st.form_submit_button('enviar')
            if input_button_submit:
                  st.write(f'Compromisso: {input_compromisso}')
                  st.write(f'Nome: {input_nome}')
