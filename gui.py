import webview
import threading
import os

def start_streamlit():
    os.system("streamlit run app.py --server.port 8501")

if __name__ == '__main__':
    threading.Thread(target=start_streamlit).start()
    webview.create_window("Grass Detector", "http://localhost:8501", width=1000, height=800)
