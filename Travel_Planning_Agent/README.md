# Travel Planning Agent

An intelligent AI agent that creates detailed European travel itineraries with budget optimization and real-time information.

## 🌟 Features

- **AI-Powered Planning**: Uses OpenAI GPT models for intelligent itinerary generation
- **Real-time Search**: Integrates EXA and DuckDuckGo for current travel information
- **Google Maps Integration**: Provides location links and place IDs
- **Budget Optimization**: Calculates costs and suggests budget-friendly options
- **Family-Friendly**: Tailored recommendations for family travel
- **Booking Resources**: Direct links to booking platforms and travel resources

## 🚀 Quick Start

### Option 1: AI Agent (Requires API Keys)
```bash
python Travel_Plan.py
```

### Option 2: Simple Planner (No API Required)
```bash
python Simple_Travel_Planner.py
```

## 🔑 API Keys Setup

1. **OpenAI API Key**: 
   - Get from: https://platform.openai.com/api-keys
   - Add to `Travel_Plan.py`: `os.environ["OPENAI_API_KEY"] = "your_key_here"`

2. **EXA API Key**: 
   - Get from: https://exa.ai/
   - Already configured: `EXA_API_KEY = "your_key_here"`

3. **Google Maps API Key**: 
   - Get from: https://console.cloud.google.com/
   - Already configured: `MAPS_API_KEY = "your_key_here"`

## 📝 Usage Example

```
User: I am planning a trip for a family of 5 with budget around $6000. Looking at countries in Europe for 15 days around April or May.
```

The agent will generate:
- Detailed 15-day itinerary
- Budget breakdown
- Accommodation suggestions with booking links
- Activity recommendations
- Transportation options
- Google Maps links for locations
- Weather considerations
- Family travel tips

## 🛠️ Files Description

- `Travel_Plan.py` - Main AI agent with full API integration
- `Simple_Travel_Planner.py` - Standalone version without API requirements
- `maps_tools.py` - Google Maps API integration tools
- `prompt.py` - Agent system prompts and instructions

## 💡 Tips

- For budget travel, the agent suggests Eastern European countries
- For luxury travel, it recommends Western/Northern European destinations
- All recommendations include direct booking links
- Google Maps integration provides exact location references

## 🔧 Troubleshooting

- **OpenAI Quota Error**: Add credits to your OpenAI account
- **API Key Issues**: Ensure all keys are properly set in the code
- **Import Errors**: Run `pip install -r requirements.txt`