import streamlit as st
import requests

st.set_page_config(page_title="Meeting Notes Generator", page_icon="🎙")
st.title("🎙 Meeting Notes Generator from Voice Memos")
audio_file = st.file_uploader("Upload your meeting audio (.mp3 or .wav)", type=["mp3", "wav"])

if audio_file:
    st.audio(audio_file)

    if st.button("Generate Notes"):
        with st.spinner("Transcribing and summarizing..."):
            #try: 
                res = requests.post(
                    "http://localhost:8000/process/",
                    files={"file": (audio_file.name, audio_file, audio_file.type)}
                )
                res.raise_for_status()
                output = res.json()

                st.subheader("📝 Summary:")
                st.write(output["summary"])

                st.subheader("✅ Action Items:")
                st.write(output["action_items"])

                with st.expander("📄 Full Transcript"):
                    st.text_area("Transcript", value=output["transcript"], height=300)

           # except requests.exceptions.RequestException as e:
               # st.error(f"Failed to connect to backend: {e}")
           # except Exception as e:
                #st.error(f"Something went wrong: {e}")