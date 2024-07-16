from packages.AI import Model
import streamlit as st


def main():
    model = Model()

    st.title("2024 HAI Summer Project")
    st.markdown("---")

    st.subheader("Google Gemini Api를 이용해 대화 주고받기")
    query = st.text_input('INPUT', "Gemini에게 보낼 메시지 입력")
    response = model(query)

    st.markdown("---")
    st.markdown("### **OUTPUT**")
    st.markdown(response)

if __name__ == "__main__":
    main()
