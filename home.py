import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt


add_selectbox = st.sidebar.selectbox(
    "목차",
    ("체질량 계산기", "갭마인더", "마이페이지")
)

if add_selectbox == "체질량 계산기":
    #체질량 지수 구하는 앱
    #몸무게, 키 입력 받기
    #Home/Streamlit library/API reference/Status elements

    st.write('#체질량 계산기')
    st.success('체질량지수는 자신의 몸무게를 키의 제곱으로 나눈 값입니다.')

    height = st.number_input('키를 입력하세요', value = 160, step = 5)
    st.write('입력하신 키 : ', height, 'cm')

    weight = st.number_input('몸무게를 입력하세요', value = 50, step = 5)
    st.write('입력하신 몸무게 : ', weight, 'kg')

    bmi = weight/((height/100)**2)

    def bmi_range(bmi):
        if bmi >= 25:
            st.error('비만 입니다.')
        elif bmi >= 23:
            st.warning('과체중 입니다.')
        elif bmi >= 18.5:
            st.success('정상 입니다.')
        else:
            st.warning('저체중 입니다.')
        
    if st.button('값'):
        st.write('당신의 체질량 지수는 ', round(bmi, 2), '입니다.')
        bmi_range(bmi)
        st.balloons()

    #Home/Streamlit library/API reference/Media elements/st.image


    image = Image.open('cake0605.jpg')

    st.image(image, caption='Take care of yourself.')
    

elif add_selectbox == "갭마인더":
    st.write("# 여기는 갭마인더 페이지 입니다.")
    
    data = pd.read_csv('gapminder.csv')
    st.write(data)
    
    colors = []
    for x in data['continent']:
        if x == 'Asia':
            colors.append('tomato')
        elif x == 'Europe':
            colors.append('blue')
        elif x == 'Africa':
            colors.append('olive')
        elif x == 'Americas':
            colors.append('green')
        else:
            colors.append('orange')
            
    data['colors'] = colors
    
    year = st.slider('년도를 선택하세요', 1952, 2007, 1952, step = 5)
    st.write('## ', year, '년')
    
    data = data[data['year'] == year]
    
    fig, ax = plt.subplots()
    ax.scatter(data['gdpPercap'], data['lifeExp'], s = data['pop']*0.000002, color = data['colors'])
    ax.set_title('How Does Gdp per Capital relate to Life Expectancy?')
    ax.set_xlabel('Gdp per Capital')
    ax.set_ylabel('Life Expectancy')

    st.pyplot(fig)
    
  

else:
    st.write("# 여기는 마이페이지 입니다.")