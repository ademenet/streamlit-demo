import streamlit as st
from transformers import pipeline

@st.cache(allow_output_mutation=True)
def create_gpt2():
    generator = pipeline("text-generation", model="gpt2")
    return generator

if __name__ == "__main__":
    st.markdown("Loading GPT-2 model. Please Wait")
    generator = create_gpt2()
    st.markdown("Loading GPT-2 model. Done")
    st.title("Talk with an AI")
    st.subheader("A GPT-2 X Streamlit showcase")

    """
    Welcome to this experimental application!

    Enter some text into the field and play with GPT-2 text generator.
    """

    text_length = st.slider("Length of the  generated text", min_value=1, max_value=100, value=30, step=1)

    input_text = st.text_area("Put some text lines here...")

    if input_text:
        # response = generator(input_text, max_length=30, num_return_sequences=1)
        response = generator(input_text, max_length=text_length)
        st.markdown(f"{response[0]['generated_text']}")
