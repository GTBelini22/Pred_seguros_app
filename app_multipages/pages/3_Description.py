import pickle
import pandas as pd
import streamlit as st

# Page config
st.set_page_config(
    page_title = "Predição de seguro de saúde",
    page_icon = "img\stethoscope.png"
)
st.sidebar.header('Descrição Projeto')

# Titulo da página
st.title('Sobre o Projeto e como funciona')

st.markdown(
    """
    # 1 - Sobre \nEste projeto foi realizado como um desafio da formação em Dados da escola DNC,
    cujo objetivo era criar um modelo de aprendizado de máquina (Machine Learning)
    capaz de prever o valor do seguro a partir de dados de uma pessoa.
    Essa predição deveria ser feita com base em dados passados da seguradora.
     """
    )


st.markdown(
    """
        # 2 - Modelagem \nPara abordar este problema, primeiramente criamos um arquivo no Google Colab para montar o modelo.
    Utilizamos a metodologia CRISP-DM, que define os passos a seguir até a conclusão.
    Começamos compreendendo a base de dados, em seguida realizamos a limpeza dos dados,
    preparamos os dados, desenvolvemos o modelo, avaliamos as métricas e, por fim, implementamos o modelo gerado.
    """
)


st.markdown(
    """
    # 3 - Métodos aplicados
    Os Métodos usados para a criação do modelo foram:
    - Linear Regression
    - LassoCV RidgeCV
    - Random Forest Regressor
    - Gradient Boost Regressor
    
    Entretanto, ao gerar as metricas de cada modelo,
    foi visto que o Gradient Boost Regressor performou melhor que todos e sendo esse o escolhido para o tunning,
    que é um modo de tentar encontrar ainda melhores parametros dentro desse método, ao final o modelo conseguiu um R2 de 86%.
    
    """
)