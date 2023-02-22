import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

st.title("เราควรดื่มกาแฟปริมาณไหนดี?")
st.write("ในเครื่องดื่มแต่ละชนิดจะมีปริมาณคาเฟอีนที่ต่างกัน กาแฟเป็นเครื่องดื่มที่มีปริมาณคาเฟอีนสูง เมื่อเที่ยบกับเครื่องดื่มประเภทอื่น เช่น ชาค่าปกติปริมาณคาเฟอีนในกาแฟจะอยู่ที่ 40 มก./100 กรัม ส่วนชาจะอยู่ที่ 11 มก./100 กรัม ซึ่งความแตกต่างในเรื่องนี้ไม่ได้เกิดขึ้นเพราะธรรมชาติของตัวเมล็ดกาแฟ หรือใบชา แต่เกิดจากวิธีการชงกาแฟใช้น้ำที่มีอุณหภูมิสูงกว่า รวมถึงขั้นตอนการชงยังใช้ปริมาณเม็ดกาแฟมากกว่าใบชาด้วย ทำให้มีการสกัดคาเฟอีนออกมาได้มากกว่า กาแฟจึงช่วยต่อสู้กับความง่วงได้ดีกว่า")
option = st.selectbox(
    '',
    ('เมนู','กาแฟอาราบิก้า','กาแฟโรบัสต้า','กาแฟลิเบอริกา','กาแฟเอ็กซ์เซลซา'))
st.write("Menu")
st.write('You selected:', option)
st.number_input('ปริมาณที่ควรใส่น้ำ',min_value=0, max_value=100)
ss =st.button('ganarad')
if ss:
    st.markdown('')

st.markdown(
    f"""
       <style>
       .stApp {{
           background-image: url("https://images.pexels.com/photos/2836945/pexels-photo-2836945.jpeg?auto=compress&cs=tinysrgb&w=600");
           background-attachment: fixed;
           background-size: cover;
           /* opacity: 0.3; */
       }}
       </style>
       """,
    unsafe_allow_html=True
)

left, right = st.columns(2)
left.markdown("ปริมาณน้ำที่ควรชง?")
left.markdown("กรอกปริมาณน้ำที่ต้องการ")

def coffee_data():
    rng = np.random.RandomState(0)
    n = 1.25
    x = np.round(400*rng.rand(n), -1).astype(np.int16) # 'พื้นที่(ตรว)'
    y = np.round(40000*x + 20000 + 200000*rng.rand(n), -4).astype(np.int32) # ราคา(บาท)
    df = pd.DataFrame({
        'x': x,
        'y': y
    })
    df.to_excel('house.xlsx')