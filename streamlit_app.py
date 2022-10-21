import streamlit as st
from typing import Callable
from streamlit_gallery import apps

PAGE_PARAM = "p"
CONTENT = {
    "Module 2 : Codex": {
        "Chapter 3 : Data": apps.m2_codex_data,
        "Chapter 4 : SQL": apps.m2_codex_sql,
        "Chapter 5 : First ML Project": apps.m2_codex_text_generation,
    },
    "Module 3 : ML with Codex": {
        "Chapter 2 : Cluster your URLs": apps.m3_cluster_urls,
        #"Chapter 3 : Predict your web traffic": apps.m3_traffic_prediction,
        #"Chapter 4 : Extract keywords": apps.m3_keywords_extraction,
        "Chapter 5 : Make text summaries": apps.m3_make_text_summaries,
    },
    "Module 4 : Automation with Codex": {
        "Chapter 2 : Post generated text in a WP": apps.m4_posting_wordpress,
        "Chapter 3 : Get stats by emails": apps.m4_get_stats_by_email,
        "Chapter 4 : Detect errors by Slack": apps.m4_alert_by_slack,
    },
}


def main():
    query_params = st.experimental_get_query_params()
    page_param = (
        query_params[PAGE_PARAM][0]
        if PAGE_PARAM in query_params
        else "streamlit-gallery"
    )
    page_selected = None

    c30, c32 = st.columns([2.5, 3])

    with c30:
        st.sidebar.image("images/logoNew.png", width=275)
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")
        st.caption("")

        emoji_backhand_index = st.image("courseImage.png")

    with st.sidebar:
        st.caption(
            "Made in 🎈 [Streamlit](https://www.streamlit.io/), by [Vincent Terrasi](https://www.linkedin.com/in/vincent-terrasi/) and [Charly Wargnier](https://www.charlywargnier.com/) for [DatamarketingLabs](https://www.datamarketinglabs.com/)."
        )

        st.title("Course Gallery")

        for category_name, pages in CONTENT.items():
            category_expander = st.sidebar.expander(
                category_name.upper(), expanded=True
            )

            for page_name, page_function in pages.items():
                page_key = page_name.replace(" ", "-").lower()

                st.session_state[page_key] = page_key == page_param

                if category_expander.checkbox(
                    page_name,
                    False,
                    key=page_key,
                    on_change=select_page,
                    args=[page_key],
                ):
                    page_selected = page_function

    # remove emojis if p selected
    if page_param != "streamlit-gallery":
        emoji_backhand_index.empty()

    if isinstance(page_selected, Callable):
        page_selected()


def select_page(page_key):
    if page_key in st.session_state and st.session_state[page_key]:
        query_params = st.experimental_get_query_params()
        query_params[PAGE_PARAM] = page_key

        st.experimental_set_query_params(**query_params)


if __name__ == "__main__":
    st.set_page_config(
        page_title="No Code Gallery with Streamlit & Codex",
        page_icon="🎈",
        layout="wide",
    )
    main()
