import streamlit as st
import pandas as pd

st.title("🧼 Limpeza de Lista de E-mails com Blacklist")

st.write("Envie sua lista de e-mails e a blacklist para remover automaticamente os e-mails bloqueados.")

uploaded_list = st.file_uploader("Envie a lista de e-mails", type=["csv"])
uploaded_blacklist = st.file_uploader("Envie a blacklist", type=["csv"])

if uploaded_list and uploaded_blacklist:
    df_list = pd.read_csv(uploaded_list, header=None, names=["email"])
    df_black = pd.read_csv(uploaded_blacklist, header=None, names=["email"])

    cleaned = df_list[~df_list["email"].isin(df_black["email"])]

    st.success("Lista limpa com sucesso!")

    st.write("### 📄 Lista limpa:")
    st.dataframe(cleaned)

    csv = cleaned.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Baixar lista limpa", csv, "lista_limpa.csv")
