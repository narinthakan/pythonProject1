import numpy as np
import pandas as pd
import streamlit as st
df = pd.read_csv('book2.csv')
print(df)
GF, GE = st.columns(2)
with GF:
    mm = st.selectbox('เมนู', 'กาแฟอาราบิก้า', 'กาแฟโรบัสต้า', 'กาแฟลิเบอริกา', 'กาแฟเอ็กซ์เซลซา')
with GE:
    MM = st.number_input('ชนิดที่ควรดื่ม')

if Pred:
    model = load_model()
    Pred_data = ()
    Pred_data_array = np.asarray(Pred_data)
    Pred_data_array_re = Pred_data_array.reshape(1,-1)
    predict_Heart = model.predict(Pred_data_array_re)
    result = predict_Heart[0]




