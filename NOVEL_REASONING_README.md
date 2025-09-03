# 🧠 Novel Reasoning Engine

A sophisticated AI reasoning system that implements **meta-cognition**, **philosophical character compartmentalization**, and **novel problem-solving capabilities** using GPT-5 as the cognitive core.

## 🌟 Key Features

### 🎭 Philosophical Character Compartmentalization
- **Socrates**: Questioning, dialectical thinking, systematic inquiry
- **Aristotle**: Systematic, empirical, categorizing approach
- **Descartes**: Analytical, mathematical, systematic doubt
- **Kant**: Critical, systematic, universal principles
- **Nietzsche**: Perspectival, genealogical, creative destruction

### 🧩 Advanced Reasoning Capabilities
- **Meta-cognition**: Self-reflection and self-awareness in reasoning
- **Hypothesis Generation**: Multiple hypotheses before answering
- **Future Simulation**: Simulating potential answers before responding
- **Dual Answer Generation**: Two different approaches for better accuracy
- **Rule Abstraction**: Learning and storing patterns for future use

### 📚 Learning & Memory
- **Persistent Rule Storage**: Saves learned patterns to JSON
- **Reasoning History**: Tracks all thinking steps
- **Confidence Scoring**: Measures certainty in answers
- **Success Rate Tracking**: Monitors rule effectiveness

## 🚀 Quick Start

### 1. Installation

```bash
# Install dependencies
pip install -r requirements_novel_reasoning.txt

# Or install individually
pip install openai python-dotenv
```

### 2. Configuration

Create a `.env` file in your project root:

```bash
OPENAI_API_KEY=your_actual_openai_api_key_here
```

### 3. Basic Usage

#### Python Script
```python
import asyncio
from src.arcft.novel_reasoning import NovelReasoningEngine
import os
from dotenv import load_dotenv

load_dotenv()

async def main():
    engine = NovelReasoningEngine(os.getenv("OPENAI_API_KEY"))
    
    problem = "What is the pattern in this sequence: 2, 4, 8, 16?"
    result = await engine.solve_problem(problem)
    
    print(f"Primary Answer: {result['dual_answers']['primary_answer']}")
    print(f"Alternative Answer: {result['dual_answers']['alternative_answer']}")

asyncio.run(main())
```

#### Command Line Interface
```bash
# Solve a problem
python src/arcft/scripts/novel_reasoning_cli.py solve "What is the pattern in this sequence: 2, 4, 8, 16?"

# View learned rules
python src/arcft/scripts/novel_reasoning_cli.py rules

# Interactive mode
python src/arcft/scripts/novel_reasoning_cli.py interactive
```

## 🎯 How It Works

### 1. **Multi-Perspective Analysis**
Each philosophical character analyzes the problem from their unique worldview:
- **Socrates** questions assumptions and seeks clarity
- **Aristotle** categorizes and seeks systematic patterns
- **Descartes** applies mathematical rigor and systematic doubt
- **Kant** looks for universal principles and conditions
- **Nietzsche** considers multiple perspectives and creative solutions

### 2. **Hypothesis Generation**
Based on the philosophical insights, the system generates multiple testable hypotheses that could explain the observed patterns.

### 3. **Future Simulation**
The system simulates two different approaches to solving the problem:
- **Systematic/Analytical**: Methodical, step-by-step reasoning
- **Creative/Intuitive**: Innovative, pattern-recognition based

### 4. **Dual Answer Generation**
Two different solutions are generated, each with confidence scores and reasoning explanations.

### 5. **Rule Abstraction**
The system learns general patterns and rules that can be applied to similar problems in the future.

## 🔧 Advanced Usage

### Custom Philosophical Characters

```python
from src.arcft.novel_reasoning import PhilosophicalCharacter

# Create a custom character
einstein = PhilosophicalCharacter(
    name="Einstein",
    description="Theoretical physicist known for relativity",
    thinking_style="Intuitive, visual, thought experiments, seeking elegant solutions",
    expertise=["physics", "mathematics", "philosophy of science", "creative thinking"]
)

# Add to engine
engine.characters["einstein"] = einstein
```

### Batch Problem Solving

```python
problems = [
    "What is the next number in: 1, 3, 6, 10, 15?",
    "Find the pattern: A, C, F, J, O?",
    "What comes next: 2, 6, 12, 20, 30?"
]

results = []
for problem in problems:
    result = await engine.solve_problem(problem)
    results.append(result)
```

### Rule Management

```python
# Get all learned rules
rules = engine.get_learned_rules()

# View specific rule
for rule in rules:
    if rule.confidence > 0.8:
        print(f"High confidence rule: {rule.description}")

# Clear history
engine.clear_history()
```

## 📊 Output Structure

The engine returns a comprehensive result dictionary:

```python
{
    "problem": "Original problem text",
    "context": "Additional context provided",
    "timestamp": "ISO timestamp of solution",
    "character_thoughts": {
        "socrates": "Socrates' analysis...",
        "aristotle": "Aristotle's analysis...",
        # ... other characters
    },
    "hypotheses": "Generated hypotheses text",
    "dual_answers": {
        "primary_answer": "Most likely solution",
        "alternative_answer": "Alternative solution",
        "primary_confidence": 0.95,
        "alternative_confidence": 0.87,
        "reasoning_comparison": "Why these answers differ",
        "recommended_answer": "Which answer to use"
    },
    "new_rules_learned": 3,
    "total_rules": 15,
    "reasoning_steps": 25
}
```

## 🎨 Example Use Cases

### 1. **Pattern Recognition**
- Mathematical sequences
- Visual patterns
- Language patterns
- Logical puzzles

### 2. **Problem Decomposition**
- Complex multi-step problems
- Creative problem solving
- Strategic planning
- Decision making

### 3. **Learning & Education**
- Teaching complex concepts
- Multiple perspective analysis
- Critical thinking development
- Hypothesis testing

### 4. **Research & Analysis**
- Data pattern analysis
- Hypothesis generation
- Alternative solution exploration
- Systematic reasoning

## 🔍 CLI Commands

### Solve Command
```bash
# Basic problem solving
python novel_reasoning_cli.py solve "Your problem here"

# With context
python novel_reasoning_cli.py solve --problem "Problem" --context "Additional info"

# Using different model
python novel_reasoning_cli.py solve --problem "Problem" --model gpt-4
```

### Rules Command
```bash
# View all rules
python novel_reasoning_cli.py rules

# View specific rule
python novel_reasoning_cli.py rules --rule-id rule_001_20241201_143022
```

### History Command
```bash
# View recent history
python novel_reasoning_cli.py history

# View more history items
python novel_reasoning_cli.py history --limit 20
```

### Interactive Mode
```bash
python novel_reasoning_cli.py interactive
```

Available interactive commands:
- `solve <problem>` - Solve a problem
- `rules` - View learned rules
- `history` - View reasoning history
- `clear` - Clear history
- `help` - Show commands
- `quit` - Exit

## 🛠️ Troubleshooting

### Common Issues

1. **API Key Error**
   ```
   Error: OPENAI_API_KEY environment variable not set
   ```
   - Create a `.env` file with your API key
   - Or set the environment variable directly

2. **Model Not Available**
   ```
   Error: The model 'gpt-5' does not exist
   ```
   - Use `--model gpt-4` instead
   - Check OpenAI model availability

3. **Import Errors**
   ```
   ModuleNotFoundError: No module named 'novel_reasoning'
   ```
   - Ensure you're in the correct directory
   - Check Python path configuration

### Performance Tips

- **Batch Processing**: Solve multiple related problems together
- **Rule Reuse**: The engine learns and improves over time
- **Context Optimization**: Provide relevant context for better results
- **Model Selection**: Use GPT-4 for faster responses, GPT-5 for better reasoning

## 🔬 Technical Details

### Architecture
- **Async Design**: Non-blocking API calls for better performance
- **Modular Structure**: Easy to extend and customize
- **Persistent Storage**: JSON-based rule and history storage
- **Error Handling**: Graceful degradation and logging

### Dependencies
- `openai`: OpenAI API client
- `python-dotenv`: Environment variable management
- `asyncio`: Asynchronous programming support
- `typing-extensions`: Enhanced type hints

### File Structure
```
src/arcft/
├── novel_reasoning.py          # Main engine
├── scripts/
│   └── novel_reasoning_cli.py # CLI interface
├── __init__.py
└── ...
```

## 🚀 Future Enhancements

- **Multi-Modal Reasoning**: Image and text combined analysis
- **Collaborative Characters**: Characters that build on each other's insights
- **Advanced Rule Learning**: Machine learning for rule optimization
- **Real-time Collaboration**: Multiple engines working together
- **Custom Reasoning Frameworks**: User-defined thinking methodologies

## 📝 License

This project is part of the ARC Competition 2025 submission. Use responsibly and in accordance with OpenAI's terms of service.

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional philosophical characters
- Enhanced rule learning algorithms
- Better parsing of AI responses
- Performance optimizations
- Additional output formats

---

**Ready to unlock the power of novel reasoning?** 🧠✨

Start with a simple problem and watch as the engine generates insights from multiple philosophical perspectives, creates hypotheses, simulates solutions, and learns patterns for future use!
