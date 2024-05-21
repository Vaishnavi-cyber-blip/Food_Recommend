import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool, AgentType, initialize_agent, load_tools
from dotenv import load_dotenv
import streamlit as st
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
from langchain.agents import tool

load_dotenv()
# groq_api_key = os.environ["GROQ_API_KEY"]
groq_api_key = "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"
# tavily_api_key = os.environ["TAVILY_API_KEY"]
tavily_api_key ="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"

llm=ChatGroq(api_key=groq_api_key, model="llama3-8b-8192")


@tool('TavilySearch')
def travily_search(search_query: str):
    """Useful to search the internet about a given topic and return relevant results."""
    # Initialize the API wrapper with the API key
    api_wrapper = TavilySearchAPIWrapper(tavily_api_key=tavily_api_key)
    # Pass the initialized API wrapper to TavilySearchResults
    tavily_tool = TavilySearchResults(api_wrapper=api_wrapper)
    return tavily_tool.run(search_query)

# add the buget feature
#agent1: food expert , nutritionist, recipe explainer, homemade cook, food influencer, foodies



def create_crewai_setup(mausam, mood, type, category, location, diet):
    food_expert = Agent(
        role="Food Expert",
        goal=f""" Suggest the food for {type} type of person in {category} category also 
                  analyse {mausam} weather, {mood} mood of person to make personalized suggestions.""",
        backstory=f""" A food expert who can suggest the perfect dish based on current weather, 
                       persons mood and personality. Skilled in recommending food for people to enjoy 
                       delightful meal that suits the occasion """,
        verbose=True,
        llm=llm,
        allow_delegation=True,
        tools=[travily_search],
    )

    food_influencer = Agent(
        role="Food Influencer",
        goal=f""" Suggest the good food and restaurants to explore in the {location} place""",
        backstory=f"""You are a popular food influenceer who is usually invited to 
                      prestigious culinary event. You know about the latest viral food and recipes of the various places. 
                      You suggest people with the dish that captured your attention. """,
        verbose=True,
        llm=llm,
        allow_delegation=True,
        tools=[travily_search],
    )

    nutritionist = Agent(
        role="Nutritionist",
        goal=f""" Provide nutrition recommendation if the person is on {diet} diet and provide recommendations for a healthy lifestyle.""",
        backstory=f""" Medical professional experienced in assessing overall health and 
                       well-being. Offers recommendations for a healthy lifestyle 
                       considering age, gender, and disease factors.""",
        verbose=True,
        llm=llm,
        allow_delegation=True,
        tools=[travily_search],
    )

    task1 = Task(
        description=f"""Plan a meal for person based on their {mood} mood, the {mausam} weather, {category} and the {type} of attitude towards food.""",
        input_data={
            "location": location,
            "mood": mood,
            "diet": diet,
            "type": type,
            "category": category,
            "mausam": mausam,
        },
        expected_output="Expected output: Name of dish recommended, detailed recipe, list of ingredients, step-by-step instructions to prepare the meal",
        agent=food_expert,
        llm=llm
    )

    task2 = Task(
        description=f"""Recommend food based on this {location} place. Give the detailing of what you liked about about the food. """,
        expected_output="Expected output: Name and location of the recommended restaurant, name of the dish, details about why the dish is recommended",
        agent=food_influencer,
        llm=llm
    )

    task3 = Task(
        description=f"""Recommend food based on this {diet} diet of person. Give the detailing of why recommendation is beneficial for the person """,
        expected_output="Expected output: Name of the recommended food item, nutritional benefits of the recommended food item, explanation of why the food item is compatible with the diet",
        agent=nutritionist,
        llm=llm
    )

    if diet.lower() == "yes":
        food_crew = Crew(
            agents=[food_expert, food_influencer, nutritionist],
            tasks=[task1, task2, task3],
            verbose=2,
            process=Process.sequential,
        )
        crew_result = food_crew.kickoff()
        return crew_result
    else:
        food_crew = Crew(
            agents=[food_expert, food_influencer],
            tasks=[task1, task2],
            verbose=2,
            process=Process.sequential,
        )
        crew_result = food_crew.kickoff()
        return crew_result


def main():
  
    st.set_page_config(page_title="ZOMA", page_icon="🍙", layout="centered")

    st.markdown("""      
                <style>
                /* General styling for the page */
                body {
                    background-color: #f4f4f2; /* White background color */
                    color: #333333;
                    font-family: 'Arial', sans-serif;
                }

                h1, h2 {
                    color: #FFFFFF; /* Zomato red color for headers */
                    text-align: center;
                }

                /* Styling for select boxes and text input to match the design of col2 */
                .stSelectbox div[data-baseweb="select"], .stTextInput input {
                    background-color: #F4F4F2;  /* Light gray background color */
                    color: #333333;  /* Softer gray text color */
                    border: 1px solid #cccccc; /* Light gray border */
                    border-radius: 4px;
                    padding: 8px;
                    font-size: 14px;
                    width: 100%;
                }

                .stSelectbox div[data-baseweb="select"] {
                    color: #333333;  /* Softer gray text color for dropdown options */
                }

                .stSelectbox div[data-baseweb="select"] ul {
                    background-color: #F4F4F2;  /* Light gray background color for dropdown */
                    border: 1px solid #cccccc; /* Light gray border */
                }

                .stSelectbox div[data-baseweb="select"] ul > li {
                    color: #333333;  /* Softer gray text color for dropdown options */
                    background-color: #F4F4F2;  /* Light gray background */
                    padding: 5px 10px;
                    font-size: 14px;
                }

                .stSelectbox div[data-baseweb="select"] ul > li:hover {
                    background-color: #e0e0e0;  /* Darker gray hover background */
                }

                /* Styling for buttons to match the design of col2 */
                .stButton button {
                    background-color: #F4F4F2; /* Light gray background color */
                    color: #333333; /* Softer gray font color */
                    border: 2px solid #E23744; /* Zomato red border */
                    border-radius: 4px;
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                    transition: background-color 0.3s ease, color 0.3s ease;
                    display: block;
                    margin: 20px auto; /* Center the button */
                }

                .stButton button:hover {
                    background-color: #E23744; /* Zomato red background on hover */
                    color: white; /* White font color on hover */
                }

                /* Centering the content */
                .css-1cpxqw2 {
                    max-width: 600px;
                    margin: auto;
                    text-align: center;
                }
                </style>
                """, unsafe_allow_html=True)
    
    container = st.container()

    col1, col2, col3 = container.columns(3)
    with col1:
        mausam = st.selectbox(
            'Weather in your area:',
            ('Sunny', 'Warm', 'Cold', 'Rainy', 'Cloudy', 'Cool')
        )

    with col2:
        location = st.text_input(
            'City you are currently in:'
        )
    with col3:
        mood = st.selectbox(
            'Your current mood:',
            ('Happy', 'Sad', 'Neutral', 'Romantic', 'Excited', 'Calm')
        )

    container2 = st.container()
    col4, col5, col6 = container2.columns(3)

    with col4:
        diet = st.selectbox(
            'Are you on diet:',
            ('Yes', 'No')
        )

    with col5:
        type = st.selectbox(
            'What kind of person you are:',
            ('Food lover', 'Casual eater')
        )

    with col6:
        category = st.selectbox(
            'Veg or non-veg:',
            ('Veg', 'non-veg')
        )


    if st.button('Find My Perfect Meal'):
        st.write('Loading...')
        crew_result=create_crewai_setup(mausam, location ,mood, diet, type, category)
        st.write(crew_result)
        
if __name__ == "__main__":
    main()
    