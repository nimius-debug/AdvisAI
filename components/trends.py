from pytrends.request import TrendReq
import requests
import pandas as pd
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate
from langchain.schema.messages import SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler



@st.cache_resource(ttl=60*60*2)
def get_x_trends():
    url = "https://twitter-trends5.p.rapidapi.com/twitter/request.php"

    payload = { "woeid": "23424977" }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "29fc5bae72mshc0e953d0a746bbfp14b410jsnba34753e5409",
        "X-RapidAPI-Host": "twitter-trends5.p.rapidapi.com"
    }
    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()  # This will raise HTTPError for bad responses (4xx and 5xx)
    except requests.RequestException as e:
        st.error(f"Failed to retrieve trends: {e}")
        return []  # Return an empty list as a fallback
    # Extracting required data from each trend
    trends_data = response.json()
    extracted_trends = []
    for key, trend in trends_data.get('trends', {}).items():
        name = trend.get('name')
        volume_short = trend.get('volumeShort')
        domain_context = trend.get('domainContext')
        extracted_trends.append({'Name': name, 'Volume Short': volume_short, 'Domain Context': domain_context})

    # Convert the list of dictionaries to a DataFrame
    df_trends = pd.DataFrame(extracted_trends)
    return df_trends


@st.cache_data(ttl=60*30)
def get_realtime_trends() -> list:
    pytrends = TrendReq(hl='en-US', tz=360)
    df = pytrends.realtime_trending_searches(pn='US') 
    # droping 2 column and converting topics to list
    trends = df.iloc[:, 0].values.tolist()
    return trends




# chat_template = ChatPromptTemplate.from_messages(
#     [
#         SystemMessage(
#             content=(
#                 "You are an world class trending topic analyst.\
#                 You are asked to analyze the current trending list from Google Trends from most search to least ,\
#                 and based on the data and what people are searching you are going to analize and find the top 3\
#                 most trending topics/categories to write about in an email that should focus on what is trendy today based on the data.\    "
               
#             )
#         ),
#         HumanMessagePromptTemplate.from_template("{list}"),
#     ]
# )

# llm = ChatOpenAI(openai_api_key=st.secrets['OPENAI_API_KEY'],streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0,model='gpt-4')
# response = llm(chat_template.format_messages(list=trends))


# Fetch trending topics


# # Define the prompt template
# prompt_template = ChatPromptTemplate.from_template(
#     "Analyze the current trending list from Google Trends: {trends} and based on the data and what people are serching \
#     recomend the top 3 trending topic to write "
# )

# # Define the LLM (assuming ChatOpenAI maps to a model like GPT-4)
# model = ChatOpenAI(openai_api_key=st.secrets['OPENAI_API_KEY'])

# # Define the output parser
# output_parser = StrOutputParser()

# # Create the pipeline
# chain = prompt_template | model | output_parser

# # Iterate through the top 3 topics and invoke the chain
# for topic in top_3_topics:
#     result = chain.invoke({"topic": topic})
#     print(result)  # This should now print a string analysis of the topic
