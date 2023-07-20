# GPT Weather Review and Recommendations

This project utilizes the AccuWeather API and the GPT-3.5 Turbo model from OpenAI to provide users with weather information, reviews, and recommendations for selected locations. Users can search for locations, and the application will display a list of matching locations. Upon selecting a location, the app will retrieve the current weather information from the AccuWeather API and then generate a review and recommendations using the GPT-3.5 Turbo model.

## Prerequisites
- Python 3.x
- requirements.txt
- AccuWeather API Key
- OpenAI API Key


## Setup

1. Clone the repository:

```bash
git clone https://github.com/Weyaxi/GPTWeather/
```

2. Navigate to the project directory: 

```bash
cd GPTWeather
```

3. Install the required Python packages:

```bash
pip3 install -r requirements.txt
```

4. Get your API keys:

- AccuWeather API Key: Sign up at [AccuWeather API](https://developer.accuweather.com/apis) to get your free API key.
- OpenAI API Key: Sign up at [OpenAI](https://platform.openai.com/) to obtain your API key.

5. Replace the placeholder API keys in the app.py file with your actual API keys:

```python
openai.api_key = "YOUR_OPENAI_API_KEY"
accu_api_key = "YOUR_ACCUWEATHER_API_KEY"
```

## Running the Application

1. Save the provided `app.py` file.

2. Run the Flask application:

```bash
python3 app.py
```

3. The application will start running on your local server, typically at `http://127.0.0.1:5000/`.

## Usage

1. Access the application using your web browser by visiting http://127.0.0.1:5000/.

2. Enter a location in the search input box and click the "Search" button. The application will display a list of matching locations.

3. Click on a location to get the current weather information and a review with recommendations for that location.

4. The application will send the weather information to the GPT-3.5 Turbo model for generating a review and recommendations. The result will be displayed below the weather information.

## Screenshots

### Website

![image](https://github.com/Weyaxi/GPTWeather/assets/81961593/91e2969d-e1c3-4732-98e3-60e42b1f03fa)

### Search Results

![image](https://github.com/Weyaxi/GPTWeather/assets/81961593/b6e0527a-db8e-4c65-b639-b2d982367093)

### Results from GPT API

![image](https://github.com/Weyaxi/GPTWeather/assets/81961593/d9a41f66-1c2e-4c0b-aac8-12a15aeaa598)

## Video Demo 

![demo2](https://github.com/Weyaxi/GPTWeather/assets/81961593/9b14420c-ffcc-495a-9341-f16716a0bcb6)

