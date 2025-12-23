# AI_AGENTS_USING_AGNO

A collection of AI agents built using the Agno framework for various automation tasks.

## 🚀 Projects

### 1. Travel Planning Agent
An intelligent travel planning system that creates detailed itineraries for European trips with budget optimization and real-time information.

## 📋 Prerequisites

Before running any project, install the required dependencies:

```bash
pip install -U agno openai exa_py httpx duckduckgo_search rich pydantic
```

## 🔑 API Keys Required

### For Travel Planning Agent:
- **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)
- **EXA API Key**: Get from [EXA](https://exa.ai/)
- **Google Maps API Key**: Get from [Google Cloud Console](https://console.cloud.google.com/)

## 🗂️ Project Structure

```
AI_AGENTS_USING_AGNO/
├── Travel_Planning_Agent/
│   ├── Travel_Plan.py          # Main AI agent with OpenAI integration
│   ├── Simple_Travel_Planner.py # Standalone planner (no API required)
│   ├── maps_tools.py           # Google Maps integration
│   ├── prompt.py               # Agent prompts and instructions
│   └── README.md               # Project-specific documentation
├── README.md                   # This file
└── requirements.txt            # Dependencies
```

## 🛠️ Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/khaleed-m/AI_AGENTS_USING_AGNO.git
cd AI_AGENTS_USING_AGNO
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up API keys:**
   - Edit the respective Python files and add your API keys
   - Or set environment variables:
```bash
export OPENAI_API_KEY="your_openai_key_here"
export EXA_API_KEY="your_exa_key_here"
export GOOGLE_MAPS_API_KEY="your_maps_key_here"
```

## 🎯 Usage

### Travel Planning Agent

**Option 1: AI-Powered Agent (requires API keys)**
```bash
cd Travel_Planning_Agent
python Travel_Plan.py
```

**Option 2: Simple Planner (no API required)**
```bash
cd Travel_Planning_Agent
python Simple_Travel_Planner.py
```

## 📝 Features

### Travel Planning Agent
- ✅ AI-powered itinerary generation
- ✅ Real-time web search integration
- ✅ Google Maps integration
- ✅ Budget optimization
- ✅ Family-friendly recommendations
- ✅ Booking links and resources
- ✅ Weather considerations

## 🤝 Contributing

Feel free to contribute by adding more AI agent examples or improving existing ones.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔮 Future Projects

More AI agent examples will be added to this repository:
- Customer Service Agent
- Data Analysis Agent
- Content Creation Agent
- And more...

---
Built with ❤️ using [Agno Framework](https://github.com/agno-ai/agno)