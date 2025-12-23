# Movie Recommendation Agent

An intelligent movie recommendation system that suggests films from Bollywood (Hindi), Tollywood (Telugu), and Hollywood based on user preferences and current 2024-2025 releases.

## 🌟 Features

- **Multi-Industry Coverage**: Recommendations from Bollywood, Tollywood, and Hollywood
- **Current Releases**: Focus on 2024-2025 movies
- **Offline Mode**: Works without API when quota is exceeded
- **Date Night Suggestions**: Perfect movie picks for couples
- **Detailed Information**: Cast, director, ratings, and streaming availability
- **Rich Console Interface**: Beautiful formatted output with emojis and markdown

## 📋 Prerequisites

Before running the Movie Recommendation Agent, install the required dependencies:

```bash
pip install agno exa_py openai
pip install sqlalchemy fastapi[standard]
pip install rich pydantic
```

## 🔑 API Keys Required

### For AI-Powered Recommendations:
- **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)
- **EXA API Key**: Get from [EXA](https://exa.ai/)

### Setup API Keys:
Edit the `agent_movie_recommendation.py` file and add your API keys:
```python
os.environ["OPENAI_API_KEY"] = "your_openai_key_here"
os.environ["EXA_API_KEY"] = "your_exa_key_here"
```

## 🚀 Usage

Run the movie recommendation agent:

```bash
python agent_movie_recommendation.py
```

### Example Queries:
- "Telugu movies for date night with girlfriend"
- "Best Bollywood movies of 2024"
- "Hollywood action movies 2025"
- "Romantic movies from Tollywood"

## 🎬 Movie Categories

### Tollywood (Telugu Cinema)
- **Pushpa 2: The Rule** (2024) - Allu Arjun
- **Kalki 2898 AD** (2024) - Prabhas
- **Devara: Part 1** (2024) - Jr. NTR
- **Kushi** (2023) - Vijay Deverakonda
- **Family Star** (2024) - Vijay Deverakonda
- **Arjun Redyy** (2017) - Vijay Deverakonda
- **Dear Commrade** (2019) - Vijay Deverakonda
- **Geetha Govindam** (2018) - Vijay Deverakonda

### Bollywood (Hindi Cinema)
- **Stree 2** (2024)
- **Bade Miyan Chote Miyan** (2024)
- **Khel Khel Mein** (2024)
- **Sarfira** (2024)
- **Munjya** (2024)

### Hollywood (English Cinema)
- **Dune: Part Two** (2024)
- **Inside Out 2** (2024)
- **Deadpool & Wolverine** (2024)
- **Bad Boys: Ride or Die** (2024)
- **A Quiet Place: Day One** (2024)

## 📺 Streaming Platforms

### Telugu Movies
- **Netflix**: Kalki 2898 AD, Devara
- **Amazon Prime Video**: Pushpa 2, Kushi, Family Star
- **Disney+ Hotstar**: Regional Telugu content

### Hindi Movies
- **Netflix**: Various Bollywood releases
- **Amazon Prime Video**: Bollywood originals
- **Disney+ Hotstar**: Star network films

### English Movies
- **Netflix**: Hollywood blockbusters
- **Disney+**: Marvel and Disney releases
- **HBO Max**: Warner Bros films
- **Paramount+**: Paramount pictures

## 🛠️ How It Works

1. **AI-Powered Mode**: Uses OpenAI and EXA search for real-time recommendations
2. **Offline Mode**: Provides curated recommendations when API quota is exceeded
3. **Smart Parsing**: Understands user preferences and suggests relevant movies
4. **Rich Output**: Formatted recommendations with all movie details

## 🎯 Perfect For

- **Date Nights**: Romantic movie suggestions for couples
- **Family Time**: Family-friendly entertainment options
- **Movie Buffs**: Latest releases and trending films
- **Regional Cinema**: Authentic Bollywood and Tollywood experiences
- **Current Trends**: 2024-2025 releases and upcoming films

## 📝 Sample Output

```
# 🎬 Telugu Movies Perfect for Date Night (2024-2025)

## Top Romantic Telugu Movies

### 1. **Kushi** (2023)
- **Genre**: Romance/Drama
- **Cast**: Vijay Deverakonda, Samantha Ruth Prabhu
- **Director**: Shiva Nirvana
- **Rating**: ⭐ 7.2/10
- **Plot**: A heartwarming tale of love, relationships, and family bonds
- **Streaming**: Netflix, Amazon Prime Video
```

## 🔧 Troubleshooting

### Common Issues:
1. **API Quota Exceeded**: The agent automatically switches to offline mode
2. **Missing Dependencies**: Run `pip install -r requirements.txt`
3. **API Key Errors**: Ensure your OpenAI and EXA API keys are valid

### Offline Mode:
When API quota is exceeded, the agent provides curated recommendations from:
- Latest 2024-2025 releases
- Popular movies from all three industries
- Detailed streaming information

## 🤝 Contributing

Feel free to contribute by:
- Adding more movie recommendations
- Improving the recommendation algorithm
- Adding new streaming platforms
- Enhancing the user interface

## 📄 License

This project is part of the AI_AGENTS_USING_AGNO repository and is available under the [MIT License](../LICENSE).

---
Built with ❤️ using [Agno Framework](https://github.com/agno-ai/agno)