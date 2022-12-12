# ••• Build a Streamlit app to calculate profit and loss percentage when input of selling
# price and cost price is given

import streamlit as st
st.markdown('''
    <h1 
    style='background-color:#DCDCDC;
    text-align:center;
    color:#1A5276;'>
    PERCENT RANGE CALCULATOR
    </h1>
    ''', unsafe_allow_html=True)
st.markdown('''

''')

cost_price = st.number_input("Please enter the cost price of the item: ", min_value=1.0,step=1.0)
selling_price = st.number_input("Please enter the selling price of the item: ", min_value=1.0,step=1.0)
diff_cost_selling = selling_price - cost_price
percentage_change = (diff_cost_selling/cost_price)*100
if percentage_change > 0 and st.button("Calculate percentage change"):
    st.success(f"The profit is {percentage_change:.2f}%.")
elif percentage_change < 0 and st.button("Calculate percentage change"):
    st.error(f"The loss is {percentage_change:.2f}%.")

