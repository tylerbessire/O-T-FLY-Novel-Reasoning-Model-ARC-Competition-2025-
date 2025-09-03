# Example configuration for Novel Reasoning Engine
# Copy this file to config.py and update with your settings

import os

# OpenAI API Configuration
# Get your API key from: https://platform.openai.com/api-keys
OPENAI_API_KEY = "your_openai_api_key_here"

# Model configuration
OPENAI_MODEL = "gpt-5"  # or "gpt-4" if gpt-5 is not available

# Logging configuration
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR

# Rule storage configuration
RULE_STORAGE_FILE = "learned_rules.json"

# Character configuration (you can customize these)
PHILOSOPHICAL_CHARACTERS = {
    "socrates": {
        "name": "Socrates",
        "description": "Ancient Greek philosopher known for the Socratic method",
        "thinking_style": "Questioning, dialectical, seeking definitions and clarity through systematic inquiry",
        "expertise": ["logic", "ethics", "epistemology", "critical thinking", "questioning assumptions"]
    },
    "aristotle": {
        "name": "Aristotle", 
        "description": "Ancient Greek philosopher and scientist, student of Plato",
        "thinking_style": "Systematic, empirical, categorizing, seeking causes and principles",
        "expertise": ["logic", "metaphysics", "ethics", "politics", "natural sciences", "categorization"]
    },
    # Add more characters as needed
}

# Example usage:
# 1. Copy this file to config.py
# 2. Update OPENAI_API_KEY with your actual API key
# 3. Customize other settings as needed
# 4. Import and use in your scripts:
#
# from config import OPENAI_API_KEY, OPENAI_MODEL
# engine = NovelReasoningEngine(OPENAI_API_KEY, OPENAI_MODEL)
