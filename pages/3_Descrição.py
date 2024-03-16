import pickle
import pandas as pd
import streamlit as st

# Page config
st.set_page_config(
    page_title = "Predição de seguro de saúde",
    page_icon = "img\stethoscope.png"
)
# st.sidebar.header('Descrição Projeto')

# Titulo da página
st.title('Sobre o Projeto e como funciona')

st.markdown(
    """
    # 1 - Sobre \nEste projeto foi concebido como um desafio da Formação em dados da escola DNC, 
    com o propósito de desenvolver um modelo de aprendizado de máquina que pudesse estimar o valor do seguro com base nos dados individuais.
    O modelo deveria ser treinado com informações históricas da seguradora do ramo de saúde.
     """
    )


st.markdown(
    """
        # 2 - Modelagem \nPara solucionar este problema, primeiramente foi estabelecido um arquivo no Google Colab para a construção do modelo. 
         Seguiu-se a metodologia CRISP-DM, que delineia os passos até a conclusão do projeto. Inicialmente, 
         houve a análise do conjunto de dados; posteriormente, a limpeza e a preparação dos mesmos; em seguida, o desenvolvimento do modelo; 
         a avaliação das métricas de desempenho; e, por último, a implementação do modelo desenvolvido.
    """
)


st.markdown(
    """
    # 3 - Métodos aplicados
    Os Métodos de machine learning usados para a criação do modelo foram:
    - Linear Regression
    - LassoCV RidgeCV
    - Random Forest Regressor
    - Gradient Boost Regressor
    
    Durante a avaliação das métricas de desempenho dos modelos, 
    observou-se que o **Gradient Boosting Regressor** apresentou a melhor performance entre todos. 
    Por isso, foi selecionado para o processo de tuning, que consiste em ajustar e otimizar os parâmetros para aprimorar ainda mais o método. 
    Após essa etapa, o modelo alcançou um coeficiente de determinação (R²) de **86%**, indicando uma alta precisão nas previsões.
    
    """
)

st.markdown(
    """
    # 4 - Deploy
    Para implementar este modelo, recorremos ao uso de Pipelines, 
    que são conjuntos de etapas sequenciais para processamento automático de dados. Com isso, 
    foi possível exportar o modelo por meio da biblioteca Pickle do Python e integrá-lo a um site criado utilizando o Streamlit, 
    uma ferramenta que permite criar aplicações web em Python e oferece sua própria hospedagem.
    """
)


st.markdown(
    """
    # 4 - Links
    Autor: https://www.linkedin.com/in/gustavo-belini2200224055/
    \n
    Git Hub: https://github.com/GTBelini22

    """
)
