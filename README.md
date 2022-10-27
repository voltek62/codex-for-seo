## Welcome to our `Codex for SEO` Gallery!

- You can test here : https://codex-for-seo.streamlitapp.com/
- La formation en Français : https://www.datamarketinglabs.com/data-science-seo-sans-savoir-coder

### 2 authors
- Charly Wargnier : https://twitter.com/DataChaz
- Vincent Terrasi : https://twitter.com/VincentTerrasi

### First, you need 
- API Key from OPENAI : https://beta.openai.com/account/api-keys
- Optional : API Key form Hugginface
- Access to code-davinci

### How to run

1. Clone codex-for-seo
2. Install streamlit
3. Install libs
4. Configure streamlit
5. Run streamlit

## Install streamlit

```bash
pip install streamlit
```

## Install required libraries

```bash
pip install -r requirements.txt
```

## Configure streamlit

 ~/.streamlit/secrets.toml by default the file doesn’t exist, you have to create it if you want to overrite default config.
 
 - Open .streamlit/secrets.toml, and add this two following lines
 
 ---
 
 API_TOKEN = "YOUROPENAPIKEY"
 
 API_TOKEN2 = "YOUROPENHUGGINGFACEKEY"
 
 ---

## Run streamlit

```bash
streamlit run streamlit_app.py
```

## References

- [Streamlit](https://www.streamlit.io/)

