import streamlit as st
import requests
import json


def main():

    text_input_container = st.empty()
    new_password3 = text_input_container.text_input("Enter something")

    if not new_password3:
        st.warning("Please type your password!")
        st.stop()
    elif "M2S5ML" in new_password3:
        text_input_container.empty()
    else:
        st.warning("🚨 Nope, this password doesn't work")
        st.stop()

    """
    Main function
    """
    st.title("First ML Project")

    # Generate text
    with st.form(key="myform"):

        text_example = """Convert the description into google search query.
description: Ski Resorts in the Alps. Looking for ski trips and vacation packages to Europe ski resorts? Check out our Alps map, or discover your ideal Europe ski resort with our Resort Finder tool.\ngoogle: europe ski resorts

description: Switzerland Ski Resort. Looking for ski vacation packages to Switzerland ski resorts? Check out our Resort finder and browse to your favorite ski vacation destination, find deals.\ngoogle: switzerland ski resorts

description: Winter Park, Colorado Ski Vacation Packages. Looking for ski vacation package deals to Winter Park ski resort? Click to book hotels, flights, lift tickets and more!\ngoogle:"""

        text = st.text_area("Text to be generated", text_example, height=250)

        submitted = st.form_submit_button(label="Execute")

        if submitted:

            col1, col2, col3 = st.columns(3)
            with col2:
                gif_runner = st.image("images/mouse.gif")

            api_token = st.secrets["API_TOKEN2"]

            def query(payload="", options={"use_cache": False}):
                API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"
                headers = {"Authorization": f"Bearer {API_TOKEN}"}
                body = {"inputs": payload, "parameters": parameters, "options": options}
                response = requests.request(
                    "POST", API_URL, headers=headers, data=json.dumps(body)
                )
                try:
                    response.raise_for_status()
                except requests.exceptions.HTTPError:
                    return "Error:" + " ".join(response.json()["error"])
                else:
                    return response.json()[0]["generated_text"]

            parameters = {
                "max_new_tokens": 20,  # number of generated tokens
                "temperature": 0.4,  # controlling the randomness of generations
                "end_sequence": "description:",  # stopping sequence for generation
            }

            response = query(text, parameters)

            gif_runner.empty()

            # Display the text
            st.markdown(response)

            full_code = """# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")    
       
# Load the model
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")  
           
# Encode the text
text = tokenizer.encode(text, return_tensors="pt")
       
# Generate the text
output = model.generate(text, max_length=50, do_sample=True)
       
# Decode the text
output = tokenizer.decode(output[0], skip_special_tokens=True)"""

            st.header("Full code:")
            # st.markdown(full_code)
            st.code(full_code, language="python")


if __name__ == "__main__":
    main()
