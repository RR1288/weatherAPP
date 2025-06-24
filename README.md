# Weather Activity App

A super simple web app that takes a city name, checks the weather, and gives you ideas for what to do.

---

## Technology Stack

- **Flask** – for the backend and routing
- **Bootstrap (super simple)** – for styling and layout
- **Docker** – to containerize the app

---

## Process

1. **Get the weather**  
   The user enters a city name, which is **validated and sanitized** before being used in any prompt or API call. The app fetches current weather data (temperature, condition, etc.).

2. **Generate activity ideas**  
   Using the city and weather description, the app calls an LLM API to generate a list of fun or relevant activities. Each comes with an image prompt.

3. **(Next step)** Generate an image  
   The image prompt will be used to generate or fetch a visual suggestion for each activity.

4. **(Later)** Optimize loading  
   The goal is to make the app load faster by minimizing API latency, possibly caching or streaming responses.

---

## Bells and Whistles

- No custom CSS. Just raw, minimal Bootstrap
- Took only a short while to build. Intentionally small
- Meant to be a **“baby app”** that just shows the weather and gives fun, LLM-generated activity ideas
- Built with curiosity and caffeine. Just for fun.

---

## Running the App

Make sure you have Docker installed. Then:

```bash
docker-compose up --build
```

Open your browser to: http://localhost:5000

## To Do

- Add image generation using image prompts
- Improve performance and response times
- Cache weather and activity results
- Improve city input sanitization and feedback