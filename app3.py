import os
import functools
from crewai import Agent, Task, Crew, Process
from langchain.agents import tool
from dotenv import load_dotenv
import streamlit as st
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
# groq_api_key = os.environ["GROQ_API_KEY"]
# tavily_api_key = os.environ["TAVILY_API_KEY"]

groq_api_key = "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"
tavily_api_key = "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"

# Initialize LLM once
llm = ChatGroq(api_key=groq_api_key, model="llama3-8b-8192")

# Cache Tavily search results
@functools.lru_cache(maxsize=128)
def cached_tavily_search(search_query: str):
    """Cache the results of TavilySearch to optimize repeated queries."""
    api_wrapper = TavilySearchAPIWrapper(tavily_api_key=tavily_api_key)
    tavily_tool = TavilySearchResults(api_wrapper=api_wrapper)
    return tavily_tool.run(search_query)

@tool('TavilySearch')
def tavily_search(search_query: str):
    """Wrapper for cached TavilySearch."""
    return cached_tavily_search(search_query)

def create_agent(role, goal, backstory, tools):
    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        verbose=True,
        llm=llm,
        allow_delegation=True,
        tools=tools,
    )

def create_task(description, expected_output, agent, input_data=None):
    return Task(
        description=description,
        input_data=input_data or {},
        expected_output=expected_output,
        agent=agent,
        llm=llm
    )

def create_crewai_setup(mausam, mood, type, category, location, diet):
    # Define agent roles and goals
    agents = [
        create_agent(
            "Food Expert",
            f"Suggest the {category} food for {type} type of person also consider {mausam} weather and {mood} mood for personalized suggestions.",
            "A food expert who recommends dishes based on current weather, mood, and persona of a person.",
            [tavily_search],
        ),
        create_agent(
            "Food Influencer",
            f"Suggest {category} food and restaurants to explore in {location}.",
            "A popular food influencer knowledgeable about the latest viral foods and recipes.",
            [tavily_search],
        ),
    ]

    if diet.lower() == "yes":
        agents.append(
            create_agent(
                "Nutritionist",
                f"Provide {category} nutrition recommendations for a person on a {diet} diet and suggest a healthy lifestyle.",
                "A medical professional offering health and nutrition advice tailored to individual needs.",
                [tavily_search],
            )
        )

    # Define tasks
    tasks = [
        create_task(
            f"Plan a meal based on {mood} mood, {mausam} weather, {category} category, and {type} type.",
            "Expected output: Name of dish recommended and the reason to recommend it.",
            agents[0],
            {
                "location": location,
                "mood": mood,
                "diet": diet,
                "type": type,
                "category": category,
                "mausam": mausam,
            }
        ),
        create_task(
            f"Recommend {category} food based on {location} location and detail what you liked about the food.",
            "Expected output: Name and location of the recommended restaurant, name of the dish, and details about why the dish is recommended.",
            agents[1]
        ),
    ]

    if diet.lower() == "yes":
        tasks.append(
            create_task(
                f"Recommend {category} food for a person on a {diet} diet and explain why the recommendation is beneficial.",
                "Expected output: Name of the recommended food item, nutritional benefits, and explanation of compatibility with the diet.",
                agents[2]
            )
        )

    # Create and kick off the crew
    food_crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=2,
        process=Process.sequential,
    )
    return food_crew.kickoff()

def main():
    st.set_page_config(page_title="ZOMA", page_icon="🍙", layout="centered")
    
    st.markdown(
        """
        <style>
    .centered-header {
            text-align: center;
            color: white;
        }
    .result-box {

            background-color: #f0f0f0;
            
        </style>
        """,
        unsafe_allow_html=True
    )
        
    st.markdown('<h1 class="centered-header">ZOMA</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        mausam = st.selectbox('Weather in your area:', ('Sunny', 'Warm', 'Cold', 'Rainy', 'Cloudy', 'Cool'))
    with col2:
        location = st.text_input('City you are currently in:')
    with col3:
        mood = st.selectbox('Your current mood:', ('Happy', 'Sad', 'Neutral', 'Romantic', 'Excited', 'Calm'))

    col4, col5, col6 = st.columns(3)
    with col4:
        diet = st.selectbox('Are you on diet:', ('Yes', 'No'))
    with col5:
        type = st.selectbox('What kind of person you are:', ('Food lover', 'Casual eater'))
    with col6:
        category = st.selectbox('Veg or non-veg:', ('Veg', 'Non-veg'))

    col7, col8, col9 = st.columns(3)
    with col8:
        if st.button('Find My Perfect Meal'):
            with st.spinner('Loading...'):
                crew_result = create_crewai_setup(mausam, mood, type, category, location, diet)
            st.markdown(f'<div class="result-box">{crew_result}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
