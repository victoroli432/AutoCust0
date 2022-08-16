from imaplib import _Authenticator
import streamlit as st
import _Authenticator as stauth

st.title('Autocust')


st.sidebar.title('Menu')

names = ['victor oliveira','vinicius oliveira']
usernames = ['victoroli','viniciusoli']
passwords = ['123a','4567']

hashed_passwords = stauth.hasher(passwords).generate()
authenticator = stauth.authenticate(names,usernames,hashed_passwords,'cookie_name', 'signature_key',cookie_expiry_days=30)
name, authentication_status = authenticator.login('Login','sidebar')
if authentication_status:
 st.write(‘Welcome *%s*’ % (name))
 # your application
elif authentication_status == False:
 st.error(‘Username/password is incorrect’)
elif authentication_status == None:
 st.warning(‘Please enter your username and password’)
 

paginaselecionada = st.sidebar.selectbox('selecione a pagina que deseja',['pagina 1','pagina 2'])

if paginaselecionada == 'pagina 1':
    opçãoselecionada = st.selectbox('selecione uma opção',['opção 1','opção 2'])
    if opçãoselecionada == 'opção 1':
     st.write('vinicião meu pau na sua mão')
    elif opçãoselecionada == 'opção 2':
     st.select_slider('escolhe um ai',['victor','vinicius','soutinho da galera'])

elif paginaselecionada == 'pagina 2':
    st.write('Souto você é o bambambam')


