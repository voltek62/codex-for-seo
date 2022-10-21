"""
Python version 3.8
Write a Python script for summarizing a text with the Hugging-Face module
Load the pipeline with BART
"""
import streamlit as st
import torch
from transformers import BartTokenizer, BartForConditionalGeneration

# @st.experimental_memo
@st.cache(allow_output_mutation=True)
def load_modelBartTokenizer():
    return BartTokenizer.from_pretrained("facebook/bart-large-cnn")


# @st.experimental_memo
@st.cache(allow_output_mutation=True)
def load_model_conditional_generation():
    return BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")


def get_summary(text):

    col1, col2, col3 = st.columns(3)
    with col2:
        gif_runner = st.image("images/mouse.gif")

    model = load_model_conditional_generation()

    tokenizer = load_modelBartTokenizer()

    summary_ids = model.generate(
        torch.tensor(tokenizer.encode(text)).unsqueeze(0),
        max_length=1024,
        min_length=30,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True,
    )

    gif_runner.empty()

    # Print the summary
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)


def main():

    text_input_container = st.empty()
    new_password10 = text_input_container.text_input("")

    if not new_password10:
        st.warning("Please type your password!")
        st.stop()
    elif "M3S5SUMMARY" in new_password10:
        text_input_container.empty()
    else:
        st.warning("🚨 Nope, this password doesn't work")
        st.stop()

    """
    Main function.
    """
    st.title("Text Summarization")

    with st.form(key="myform"):

        text = """The US has "passed the peak" on new coronavirus cases, President Donald Trump said and predicted that some states would reopen this month.
The US has over 637,000 confirmed Covid-19 cases and over 30,826 deaths, the highest for any country in the world.
At the daily White House coronavirus briefing on Wednesday, Trump said new guidelines to reopen the country would be announced on Thursday after he speaks to governors.
"We'll be the comeback kids, all of us," he said. "We want to get our country back."
The Trump administration has previously fixed May 1 as a possible date to reopen the world's largest economy, but the president said some states may be able to return to normalcy earlier than that.
"""
        sentence = st.text_area("Enter a sentence", text, height=210)

        submitted = st.form_submit_button(label="Execute")

        if submitted:
            result = get_summary(sentence)
            st.success(result)
            st.title("Full code")

            code = """model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    
summary_ids = model.generate(torch.tensor(tokenizer.encode(text)).unsqueeze(0),
                                 max_length=1024,
                                 min_length=30,
                                 length_penalty=2.0,
                                 num_beams=4,
                                 early_stopping=True)
    
# Print the summary
print(tokenizer.decode(summary_ids[0], skip_special_tokens=True))   
            """

            st.code('text="""' + text + '"""\n\n' + code)


if __name__ == "__main__":
    main()