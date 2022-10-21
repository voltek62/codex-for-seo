import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import plotly.offline as py

# Plot data
def plot_data(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['ds'], y=df["y"], name="Metric"))
    fig.update_layout(title="Metric", xaxis_title="Date", yaxis_title="Metric")
    st.plotly_chart(fig)


# Plot forecast
def plot_forecast(df, forecast):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['ds'], y=df["y"], name="Metric"))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast["yhat"], name="Forecast"))
    fig.update_layout(title="Metric", xaxis_title="Date", yaxis_title="Metric")
    st.plotly_chart(fig)



# Main
def main():

    text_input_container = st.empty()
    new_password8 = text_input_container.text_input("")

    if not new_password8:
        st.warning("Please type your password!")
        st.stop()
    elif "M3S3PREDICTION" in new_password8:
        text_input_container.empty()
    else:
        st.warning("🚨 Nope, this password doesn't work")
        st.stop()

    st.title("Facebook Prophet")

    with st.form(key="myform"):

        st.markdown(
            "This is a webapp with Streamlit to predict next 30 following days with Facebook Prophet."
        )

        str_now = datetime.now().strftime("%Y%m%d%H%M%S")

        uploaded_file = st.file_uploader("Choose a CSV file with 2 columns names : ds & y", type="CSV")

        if uploaded_file is not None:

            try:
                with open(os.path.join("temp/",str_now+uploaded_file.name),"wb") as f:
                    f.write(uploaded_file.getbuffer())
            except  Exception:
                st.warning("Sorry file was not temporarily stored for upload.Please re-run the process.")

        submitted = st.form_submit_button(label="Execute")

        if submitted:
            col1, col2, col3 = st.columns(3)
            with col2:
                gif_runner = st.image("images/mouse.gif")

            # Load data
            # by default
            if uploaded_file is None:
                datapath = "examples/m3_traffic_prediction.csv"
            else:
                datapath = os.path.join("temp/",str_now+uploaded_file.name)

            df = pd.read_csv(datapath, sep=",")
            df["ds"] = pd.to_datetime(df["ds"])

            st.write("## Data")
            st.dataframe(df)

            # Plot data
            st.write("## Plot data")
            plot_data(df)

            # Fit model
            #st.write("## Fit model")
            model = Prophet()

            gif_runner.empty()

            #df_prophet = df.rename(columns={'Date': 'ds', 'Metric': 'y'})
            #st.dataframe(df_prophet)
            model.fit(df)

            # Forecast
            st.write("## Forecast")
            future = model.make_future_dataframe(periods=3)
            forecast = model.predict(future)
            st.dataframe(forecast)
            plot_forecast(df, forecast)

            st.title("Full code")

            code1 = "df = pd.read_csv(\""+datapath+"\", sep=\",\")"

            code2 = """df["ds"] = pd.to_datetime(df["ds"])

            st.write("## Data")
            st.dataframe(df)
            
            # Plot data
            st.write("## Plot data")
            plot_data(df)
            
            model = Prophet()
            model.fit(df)
            
            # Forecast
            st.write("## Forecast")
            future = model.make_future_dataframe(periods=3)
            forecast = model.predict(future)
            st.dataframe(forecast)
            plot_forecast(df, forecast)"""

            st.code(code1)
            st.code(code2)


if __name__ == "__main__":
    main()