import streamlit as st

st.title('Autocust')


st.sidebar.title('Menu')
paginaselecionada = st.sidebar.selectbox('selecione a pagina que deseja',['pagina 1','pagina 2'])

if paginaselecionada == 'pagina 1':
    opçãoselecionada = st.selectbox('selecione uma opção',['opção 1','opção 2'])
    if opçãoselecionada == 'opção 1':
    st.write('vinicião meu pau na sua mão')
elif opçãoselecionada == 'opção 2':
    st.select_slider('escolhe um ai',['victor','vinicius','soutinho da galera'])

elif paginaselecionada == 'pagina 2':
    st.write('Souto você é o bambambam')

