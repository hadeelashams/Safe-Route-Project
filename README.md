# Safe Route AI Travel Assistant

## Abstract

The **Safe Route AI Travel Assistant** is a web-based application developed to help travelers plan safe and personalized trips within Kerala. It utilizes artificial intelligence and machine learning to detect safety risks and provide smart destination suggestions based on user preferences like budget and interests.

This system is helpful for tourists, local travelers, and trip planners who want support in choosing safe and smart travel options. The application is built using **HTML and CSS** for the frontend, **Python with Flask** for the backend, and stores data in **SQLite** or **CSV files**.

The system features a **rule-based chatbot** that interacts with users through predefined questions and responses to:
- Collect user inputs  
- Provide filtered destination options based on safety levels  
- Display personalized travel plans tailored to individual needs  

For safety evaluation, the system employs a **Random Forest classification algorithm**, a supervised machine learning technique well-suited for multi-feature classification problems. It analyzes:
- Recent weather updates  
- Historical disaster data  
- Health-related concerns  

These inputs help users avoid potentially unsafe routes.

Additional features include:
- Marking favorite destinations  
- Personalized recommendations based on previous travel history  

By integrating AI, ML, chatbot technology, and personalized recommendation mechanisms, the Safe Route AI Travel Assistant delivers a practical, safety-aware travel planner. It empowers users to make informed, confident travel decisions suited to their preferences and safety concerns.
