import streamlit as st
from coingecko.api import get_token_history

doge_coin_df = get_token_history(
    id='dogecoin',
    date_list=["24-02-2022","25-02-2022","26-02-2022","27-02-2022"]
)

st.title("$DOGE Analysis")

st.subheader("Practice Streamlit project to analyze $DOGE market behavior.")

# d = st.date_input(
#      "When's your birthday",
#      datetime.date(2019, 7, 6))

st.write(doge_coin_df)




