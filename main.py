import streamlit as st
import os

st.header("Calculator App")

def download_file(file_path):
    with open(file_path, "rb") as f:
        binary_data = f.read()
    return binary_data

exe_path = 'calculator.exe'

if os.path.exists(exe_path):
    if st.button("Download My EXE"):
        file_data = download_file(exe_path)
        st.download_button(label="Download", data=file_data, file_name=os.path.basename(exe_path))
else:
    st.error("Executable file not found.")