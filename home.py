import streamlit as st
from PIL import Image

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