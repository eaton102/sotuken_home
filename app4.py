import streamlit as st

st.title("予定生成AI")

user_input01 = st.text_input("お名前")
chat1 = f"{user_input01}さんですね。よろしくお願いします"
st.markdown(f"<font color='green'>{chat1}</font>", unsafe_allow_html=True)

chat2 = "年齢は何十代ですか？"
st.markdown(f"<font color='green'>{chat2}</font>", unsafe_allow_html=True)
user_input02 = st.text_input("年齢")

chat3 = "性別は何ですか"
st.markdown(f"<font color='green'>{chat3}</font>", unsafe_allow_html=True)
user_input03 = st.text_input("性別")

chat4 = "ご職業はなにですか"
st.markdown(f"<font color='green'>{chat4}</font>", unsafe_allow_html=True)
user_input04 = st.text_input("ご職業")

chat5 = "では、最後の質問です。趣味は何ですか"
st.markdown(f"<font color='green'>{chat5}</font>", unsafe_allow_html=True)
user_input05 = st.text_input("ご趣味")

chat6 = "完了ボタンを押してください。"
st.markdown(f"<font color='green'>{chat6}</font>", unsafe_allow_html=True)

# ボタンが押されたときの処理
if st.button("設定完了"):
    redirect_url = "https://sotsuken8-k7iaxt8qjkgbzrltuffwfu.streamlit.app/"
    st.markdown(f'<a href="{redirect_url}" target="_blank">次のページへ進む</a>', unsafe_allow_html=True)
