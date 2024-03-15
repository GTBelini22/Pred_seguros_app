import pickle
import pandas as pd
import streamlit as st

# Page config
st.set_page_config(
    page_title = "Predição de seguro de saúde",
    page_icon = "img\stethoscope.png"
)
# st.sidebar.header('Calcular o Seguro')

# Titulo da página
st.title('Predição de seguro de saúde')

st.markdown("Métricas Necessárias para a predição:")

# Parametros
# Esses valores de máximos e minimo são referentes ao dataset que foi feita a analise 
var_age= st.number_input(label='Idade', value=18, min_value=18, max_value=120)
var_bmi = st.number_input(label='IMC', value=30.0)
var_children = st.slider(label='Número filhos', min_value=0, max_value=5)
var_smoker = st.selectbox(label='Fumante', options=['Sim', 'Não'])

# modelo de dados
# Impotando o Pickle do nosso projeto
# models\model.pkl 
caminho_arq = 'models/model.pkl'
with open(caminho_arq, 'rb') as model_file:
    model = pickle.load(model_file)
    
    
def prediction():
    df_input = pd.DataFrame([{
        'age': var_age,
        'bmi': var_bmi,
        'children': var_children,
        'smoker': var_smoker
    }])
    
    # Vai ser retornado um array np
    prediction = model.predict(df_input)[0]
    return prediction

df_input = pd.DataFrame([{
    'age': var_age,
    'bmi': var_bmi,
    'children': var_children,
    'smoker': var_smoker
}])


st.write('data Frame recebido', df_input)

if st.button('Predição'):
    try:
        insurance_cost = prediction()
        st.success(f'**Custo previsto do seguro de vida:**: ${insurance_cost: ,.2f}')
    except Exception as error:
        st.error(f'Não foi possível prever o valor do seguro. O seguinte erro ocorreu: \n\n{error}')
