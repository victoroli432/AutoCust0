st.selectbox('selecione uma opção',['opção 1','opção 2'])

st.sidebar.title('Menu')
paginaselecionada=st.sidebar.selectbox('selecione a pagina que deseja',['pagina 1','pagina 2'])

if paginaselecionada == 'pagina 1':
    st.title('Autocust')
elif paginaselecionada == 'pagina 2':
    st.title('Autocust')
st.write('Souto você é o bambambam')

