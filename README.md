# Zoma
## Food Recommending AI agents
Food Recommendation System designed to suggest dishes to users based on various factors such as weather, mood, dietary preferences, location, and eating habits. The system utilizes Crew AI for creating specialized AI agents, Travily Search API for web searches, and Groq-integrated Llama 3 model as the LLM (Large Language Model).

## System Components
#### 1. Crew AI Agents
  Food Expert: Provides expertise on various cuisines and dishes.
  Food Influencer: Recommends trending and popular dishes.
  Nutritionist: Suggests dishes based on dietary preferences and nutritional needs.

#### 2. Travily Search API
  Performs web searches to gather information about dishes, restaurants, and food trends.

#### 4. Groq Integrated Llama 3 Model
  A state-of-the-art language model used for natural language processing and understanding user inputs.

## Features
#### 1. Personalized Recommendations
  Weather-Based Suggestions: Recommends dishes based on the current weather (e.g., hot soups for cold weather).
  Mood-Based Suggestions: Adapts recommendations based on the user's mood (e.g., comfort food for a sad mood).
  Dietary Preferences: Filters dishes based on whether the user is vegetarian, non-vegetarian, on a diet, or has specific dietary restrictions.
  Location-Based Recommendations: Suggests local dishes or restaurants nearby.
  Eating Habits: Tailors suggestions for food lovers (gourmet choices) or casual eaters (quick and easy meals).

## Integration and APIs
  Crew AI Integration: Utilizes different AI agents to provide expert recommendations.
  Travily Search API: Fetches real-time data and reviews to enhance recommendations.
  Groq Integrated Llama 3 Model: Enhances the system's understanding of complex user queries and preferences.

## Challenges

### Optimizing the Output Results Time

One of the primary challenges encountered was the time taken to generate a single dish recommendation, which is approximately 15 minutes. To address this, the following strategies were implemented:

Caching Web Search Results: To reduce repeated web search queries and improve response times, we attempted storing search results in cache memory. This approach aimed to speed up subsequent searches by reusing previously fetched data.

Despite these efforts, further optimization is necessary to achieve acceptable performance levels for practical deployment.

## Conclusion
  This experimental project demonstrates the potential of using Crew AI agents to tackle complex tasks such as personalized dish recommendations. While the results are promising, the current processing time of      approximately 15 minutes per recommendation needs optimization for practical use.
