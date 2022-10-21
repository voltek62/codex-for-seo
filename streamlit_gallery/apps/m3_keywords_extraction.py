from keybert import KeyBERT
import streamlit as st
from pathlib import Path


def main():

    text_input_container = st.empty()
    new_password7 = text_input_container.text_input("")

    if not new_password7:
        st.warning("Please type your password!")
        st.stop()
    elif "M3S4KEYWORDS" in new_password7:
        text_input_container.empty()
    else:
        st.warning("🚨 Nope, this password doesn't work")
        st.stop()

    st.title("Extract keywords with KeyBERT")

    doc = """
             Supervised learning is the machine learning task of learning a function that
             maps an input to an output based on example input-output pairs. It infers a
             function from labeled training data consisting of a set of training examples.
             In supervised learning, each example is a pair consisting of an input object
             (typically a vector) and a desired output value (also called the supervisory signal). 
             A supervised learning algorithm analyzes the training data and produces an inferred function, 
             which can be used for mapping new examples. An optimal scenario will allow for the 
             algorithm to correctly determine the class labels for unseen instances. This requires 
             the learning algorithm to generalize from the training data to unseen situations in a 
             'reasonable' way (see inductive bias).
          """

    with st.form(key="myform"):
        # Text to extract keywords
        text = st.text_area("Text to extract keywords", doc, height=300)

        # Choose the model
        # model = st.selectbox("Choose the model", ["all-MiniLM-L6-v2", "roberta-base"])

        lang = st.selectbox("Choose the language", ["english", "french"])

        submitted = st.form_submit_button(label="Execute")

        if submitted:

            col1, col2, col3 = st.columns(3)
            with col2:
                gif_runner = st.image("images/mouse.gif")

            ###################################

            @st.cache(allow_output_mutation=True)
            def load_model():
                return KeyBERT("distilbert-base-nli-mean-tokens")

            kw_model = load_model()

            # keywords = kw_model.extract_keywords(

            ###################################

            # st.cache
            # kw_model = KeyBERT()

            # Extract keywords
            keywords = kw_model.extract_keywords(
                text,
                keyphrase_ngram_range=(2, 4),
                stop_words=lang,
                use_mmr=True,
                diversity=0.2,
                top_n=5,
            )

            gif_runner.empty()

            # Show the keywords
            st.write(keywords)

            st.title("Full code")

            code = """
kw_model = KeyBERT()
                
# Extract keywords
keywords = kw_model.extract_keywords(
    text,
    keyphrase_ngram_range=(2, 4),
    stop_words=lang,
    use_mmr=True,
    diversity=0.2,
    top_n=5,
)"""

            st.code("lang='" + lang + '\'\ntext="""' + text + '"""\n\n' + code)


if __name__ == "__main__":
    main()