import streamlit as st

st.cache(suppress_st_warning=True)
def app():
    st.title('Homepage')

    st.subheader('Problem statement')

    st.write('Our goal is to build a model to analyze and model the change in economic trends over the past couple of years in India due to the outbreak of Covid and correlate various factors that contribute to the rise and fall of the economy in India. The NLP-based model could then be used to predict the change in future trends in the economy based on these factors. The sentiment of people is modeled from the historical data which could then be used to predict the real-time sentiment and the factors contributing to that sentiment when a potential third wave or a new outbreak in the society happens. Other objectives include building computer vision models to early detect the presence of covid through X-ray images or CT scans and classify the severity of Covid-19.')
    st.write('The project will be made open-source and the results obtained can help create awareness about the spread of Covid19 and its impact on the Indian economy. The final tracker and the dashboard made can be used as a tool to track vaccine availability across various states.')
    
    st.subheader('Here you can browse the sidebar for using various tools such as')
    st.markdown('1. Detecting presence of Covid-19 from CT scan images')
    st.image("apps/images/ct scan", caption="image source: Mikael Häggström, High-resolution computed tomograph of a normal thorax, coronal plane (37), CC0 1.0")
    st.write("On uploading CT scan images in jpg format, the model predicts the presence of Covid19 with a certain confidence threshold")
    st.write("")
    
    st.markdown('2. Live Sentiment in twitter/Historical Sentiment for 2021')
    st.image("apps/images/sentiment", caption="image source: bensonruan.com")
    st.write('Depening on the tracker terms selected, sentiment graph for live tweets is displayed. Additionally, user can view historical sentiment tweets for the year 2021')
    st.write("")
    
    st.markdown('3. Covid-19 predictor from symptoms')
    st.image("apps/images/symptoms", caption="image source: https://www.sharp.com/health-news/the-top-5-symptoms-of-covid-19.cfm")
    st.write('Based on the symptoms experienced, model can predict the presence of Covid19 with a certain confidence threshold')
    st.write("")
    
    st.markdown('4. Economic Forecast for the previous months')
    st.image("apps/images/forecastn")
    st.write("Time Series models like Arima have been used to analyse the impact on economy due to Covid 19. Users can toggle between dates and types of economic indicators")
    st.write("")
    
    st.markdown('## Acknowledgements')
    st.write('Thanks to Omdena and Omdena India Chapter for providing the oppurtunity and guidance to successfully complete the project.')
