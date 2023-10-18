from pytrends.request import TrendReq
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate
from langchain.schema.messages import SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
pytrends = TrendReq(hl='en-US', tz=360)
df = pytrends.realtime_trending_searches(pn='US') 

# droping 2 column and converting topics to list
trends = df.iloc[:, 0].values.tolist()

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You are an world class trending topic analyst.\
                You are asked to analyze the current trending list from Google Trends from most search to least ,\
                and based on the data and what people are searching you are going to analize and find the top 3\
                most trending topics/categories to write about in an email that should focus on what is trendy today based on the data.\    "
               
            )
        ),
        HumanMessagePromptTemplate.from_template("{list}"),
    ]
)

llm = ChatOpenAI(openai_api_key=st.secrets['OPENAI_API_KEY'],streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0,model='gpt-4')
response = llm(chat_template.format_messages(list=trends))


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



# @st.cache_resource()
# def auth_x():
#     auth = tweepy.OAuthHandler(st.secrets['TWITTER_CONSUMER_KEY'], st.secrets['TWITTER_CONSUMER_SECRET'])
#     auth.set_access_token(st.secrets["TWITTER_ACCESS_TOKEN"], st.secrets["TWITTER_ACCESS_SECRET"])
#     return tweepy.API(auth)