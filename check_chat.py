import streamlit as st
import hashlib

def check_text(text, person):
    targets = ['8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4']
    text = text.split()
    text_hash = list()
    for word in text:
        bytes_word = bytes(word, "utf-8")
        word_hash = hashlib.sha256(bytes_word).hexdigest()
        text_hash.append(word_hash)

    for word in text_hash:
        if word in targets:
            st.session_state.Violation = person
            return False
    st.session_state.Violation = ''
    return True
        
def UI(chat):
    if "Violation" not in st.session_state:
        st.session_state.Violation = ''
        
    st.set_page_config(page_title="کاربرد هش ها")
    st.write("<div style='text-align: center'> <h1>کاربرد هش<h1> </div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        p1_text = st.text_input(label=":علی")
        if st.button(label="ارسال", key="p1"):
            security = check_text(p1_text, "علی")
            if security:
                chat = chat + "علی:" + p1_text 
        if st.session_state.Violation == 'علی':
            st.write(F"""تخلف نوشتاری از سمت {st.session_state.Violation}""")
                
    with col3:
        p2_text = st.text_input(label=":امیر محمد")
        if st.button(label="ارسال", key="p2"):
            security = check_text(p2_text, "امیر محمد")
            if security:
                chat = chat + "امیر محمد:" + p2_text 
        if st.session_state.Violation == 'امیر محمد':
            st.write(F"""تخلف نوشتاری از سمت {st.session_state.Violation}""")
    
    with col2:
        text = ""
        text += chat
        st.write(text)
    
    
    
def main():
    UI(chat)
    
chat = """"""
main()