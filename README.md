# Zoma
## Food Recommending AI agents
Food Recommendation System is designed to suggest dishes to users based on various factors such as weather, mood, dietary preferences, location, and eating habits. The system utilizes Crew AI for creating specialized AI agents, Travily Search API for web searches, and the Groq-integrated Llama 3 model as the LLM.

## System Components
#### 1. Crew AI Agents
Food Expert: Provides expertise on various cuisines and dishes.

Food Influencer: Recommends trending and popular dishes.

Nutritionist: Suggests dishes based on dietary preferences and nutritional needs.

#### 2. Travily Search API
Performs web searches to gather information about dishes, restaurants, and food trends.

#### 3. Groq Integrated Llama 3 Model
A state-of-the-art language model used for natural language processing and understanding user inputs.

#### 4. Streamlit
Provide a frontend to the application.

## Features
#### Personalized Recommendations
  Weather-Based Suggestions: Recommends dishes based on the current weather (e.g., hot soups for cold weather).
  Mood-Based Suggestions: Adapt recommendations based on the user's mood (e.g., comfort food for a sad mood).
  Dietary Preferences: Filters dishes based on whether the user is vegetarian, non-vegetarian, on a diet, or has specific dietary restrictions.
  Location-Based Recommendations: Suggest local dishes or restaurants nearby.
  Eating Habits: Tailors suggestions for food lovers (gourmet choices) or casual eaters (quick and easy meals).

## Integration and APIs
  Crew AI Integration: Utilizes different AI agents to provide expert recommendations.
  Travily Search API: Fetches real-time data and reviews to enhance recommendations.
  Groq Integrated Llama 3 Model: Enhances the system's understanding of complex user queries and preferences.

## Results
#### Input:
  Weather: Cold, Mood: happy, Location: Delhi, No dieting, Pure Veg, Persona: food lover
#### Output:
  I highly recommend visiting Saravana Bhawan, located at three outlets in Delhi. This legendary restaurant is known for its authentic South Indian cuisine and deserts. Specifically, I recommend trying their     
  South Indian dishes, such as the Vegetable Kurma, Rava Kesari, and their signature dish, the Saravana Bhawan's Sambar. Additionally, don't miss their signature dessert, the Gulab Jamun, a deep-fried dumpling 
  soaked in a sweet syrup.
  The reason I recommend Saravana Bhawan is because of its authentic South Indian cuisine and the variety of dishes available. The restaurant is also known for its vibrant atmosphere and the unique experience it    offers.

#### Input:
  Weather: Sunny, Mood: Sad, Location: Lucknow, No dieting,Non Veg, Persona: food lover

#### Output:
  The top 3 non-veg dishes from Lucknow that can lift someone's mood on a sunny day are:
  Tunday Kebab: A signature dish of Lucknow, Tunday Kebab is a must-try. The tender kebabs are cooked with a special masala containing hundreds of spices, making it a perfect dish to lift your mood on a sunny day.
  Murg Shahi Korma: This creamy chicken curry is a traditional royal recipe of the Lucknawi cuisine. The combination of crispy fried potatoes stuffed with paneer and traditional spices, blended with savory     
  tomato, onion gravy and served hot, is a perfect comfort food to soothe a sad mood on a sunny day.
  Yakhni: This Kashmiri dish has gained popularity in Lucknow, and for good reason. The creamy chicken curry with a distinct nutty taste, laced with piquant spices, is sure to lift your spirits on a gloomy day.
  These dishes are not only delicious but also have a special significance in Lucknow's culinary culture. They are sure to satisfy your taste buds and lift your mood on a sunny day.

## Challenges

### Optimizing the Output Results Time

One of the primary challenges encountered was the time to generate a single dish recommendation, which is approximately 12-15 minutes. To address this, the following strategies were implemented:

Caching Web Search Results: To reduce repeated web search queries and improve response times, we attempted storing search results in cache memory. This approach aimed to speed up subsequent searches by reusing previously fetched data.

Despite these efforts, further optimization is necessary to achieve acceptable performance levels for practical deployment.

## Conclusion
  This experimental project demonstrates the potential of using Crew AI agents to tackle complex tasks such as personalized dish recommendations. While the results are promising, the current processing time of      approximately 15 minutes per recommendation needs optimization for practical use.
