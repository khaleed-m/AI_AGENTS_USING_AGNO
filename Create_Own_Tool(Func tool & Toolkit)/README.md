# Create Own Tools

This folder demonstrates how to create custom tools and toolkits using the Agno framework.

## 📁 Files

### 1. Function_Tool.py
Shows how to create a simple function-based tool that can be used by an AI agent.

**Features:**
- Simple multiplication function as a tool
- Direct function registration with the agent

### 2. math_Tookit.py
Defines a custom MathToolkit class with multiple mathematical operations.

**Features:**
- Addition, subtraction, multiplication, division
- Error handling for division by zero
- Proper toolkit structure following Agno conventions

### 3. Test_Toolkit.py
Tests the MathToolkit with an AI agent using OpenAI's GPT model.

**Features:**
- AI-powered mathematical calculations
- Integration with OpenAI API
- Demonstrates toolkit usage in real scenarios

### 4. test_tools_locally.py
Interactive calculator that works without API calls for local testing.

**Features:**
- Interactive command-line interface
- Real-time calculations using custom tools
- No API key required for testing

## 🚀 Usage

### Prerequisites
```bash
pip install agno openai
```

### Set API Key (for AI-powered tools)
```bash
set OPENAI_API_KEY=your_openai_key_here
```

### Run Examples

**1. Test Function Tool:**
```bash
python Function_Tool.py
```

**2. Test MathToolkit with AI:**
```bash
python Test_Toolkit.py
```

**3. Interactive Calculator (No API required):**
```bash
python test_tools_locally.py
```

## 💡 Key Concepts

### Creating Function Tools
```python
def multiply_numbers(a: int, b: int) -> int:
    """Multiplies two numbers and returns the result."""
    return str(a * b)

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[multiply_numbers]  # Direct function registration
)
```

### Creating Toolkit Classes
```python
from agno.tools import Toolkit

class MathToolkit(Toolkit):
    def __init__(self):
        super().__init__(name="math_toolkit")
        self.register(self.add_numbers)
        self.register(self.subtract_numbers)
        # ... register more functions
```

## 🎯 Learning Outcomes

- How to create custom function-based tools
- How to build comprehensive toolkits
- How to integrate custom tools with AI agents
- How to test tools locally without API calls
- Best practices for tool development in Agno

## 🔧 Customization

You can extend these examples by:
- Adding more mathematical operations
- Creating tools for different domains (text processing, file operations, etc.)
- Building complex multi-step toolkits
- Adding input validation and error handling

---
Built with ❤️ using [Agno Framework](https://github.com/agno-ai/agno)