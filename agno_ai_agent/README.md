# 🔍 Advanced Web Search Agent

An intelligent web search agent built with Agno framework that provides comprehensive search capabilities with an enhanced user interface.

## ✨ Features

- **Smart Query Processing**: Automatically enhances queries based on context
- **Rich Console Interface**: Beautiful terminal UI with colors and formatting
- **Search History**: Keeps track of your search queries and results
- **Multiple Search Types**: News, research, trends, and comparison searches
- **Real-time Results**: Streams results as they're generated
- **Error Handling**: Robust error handling and user feedback

## 🚀 Quick Start

### Prerequisites

```bash
pip install agno ollama rich
```

Make sure Ollama is running:
```bash
ollama pull llama3.2:3b
ollama serve
```

### Run the Agent

```bash
python advanced_search_agent.py
```

## 🎯 Usage Examples

### Basic Search
```
🔍 Enter your search query: What is artificial intelligence?
```

### News Search
```
🔍 Enter your search query: news about climate change
```

### Research Query
```
🔍 Enter your search query: research quantum computing
```

### Trend Analysis
```
🔍 Enter your search query: trends in renewable energy
```

### Comparison
```
🔍 Enter your search query: compare Python vs JavaScript
```

## 📋 Available Commands

| Command | Description |
|---------|-------------|
| `history` | Show your search history |
| `clear` | Clear search history |
| `help` | Show help and examples |
| `exit` | Quit the application |

## 🛠️ Technical Details

- **Model**: Ollama Llama 3.2 3B (local, no API keys required)
- **Search Engine**: DuckDuckGo integration
- **UI Framework**: Rich console library
- **Response Format**: Markdown with syntax highlighting

## 🎨 Interface Features

- **Welcome Screen**: Informative startup interface
- **Progress Indicators**: Shows search progress with spinners
- **Colored Output**: Syntax-highlighted responses
- **Panel Layouts**: Organized information display
- **Error Messages**: Clear error reporting

## 🔧 Customization

You can modify the agent by:

1. **Changing the Model**: Replace `Ollama(id='llama3.2:3b')` with other models
2. **Adding Tools**: Include additional search tools or APIs
3. **Enhancing Queries**: Modify the `process_query()` method
4. **UI Styling**: Customize colors and layouts in the Rich console

## 📝 Example Session

```
🔍 Advanced Web Search Agent

Welcome to the Advanced Web Search Agent! I can help you with:
• Web Search: Search for current information on any topic
• News Search: Find latest news and updates
• Research: Comprehensive research on complex topics

🔍 Enter your search query: latest AI developments

🎯 Results for: latest AI developments
────────────────────────────────────────────────────────────
# Latest AI Developments

Recent breakthroughs in artificial intelligence include:

1. **Large Language Models**: GPT-4 and similar models showing improved reasoning
2. **Multimodal AI**: Systems that can process text, images, and audio together
3. **AI Safety**: New research on alignment and responsible AI development

[Sources and detailed information...]
────────────────────────────────────────────────────────────
```

## 🤝 Contributing

Feel free to enhance this agent by adding:
- More search engines
- Additional query types
- Export functionality
- Search result filtering
- Custom themes

## 📄 License

This project is part of the AI_AGENTS_USING_AGNO repository and follows the same license terms.