
import google.generativeai as genai
import os
import streamlit as st


api_key_path = ""


if os.path.exists(api_key_path):
    with open(api_key_path,'r') as f:
        api_key = f.read().strip()
    genai.configure(api_key=api_key)
    print("Api found successfully") # key found sucessfully
else:
    print("key not found")

try:
    model = genai.GenerativeModel("models/gemini-1.5-flash")
except:
    print("model not found")


st.title("AI chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    st.chat_message(msg['role']).write(msg['content'])

user_input = st.chat_input("Ask something Ask something about Data Science and AI")

if user_input:
    st.chat_message("user").write(user_input)

    response = model.generate_content(
          [user_input],
          generation_config=genai.types.GenerationConfig(
            temperature=0.9,
            max_output_tokens=500
        )
    )

  bot_reply = response.text
  st.chat_message("assistant").write(bot_reply)
