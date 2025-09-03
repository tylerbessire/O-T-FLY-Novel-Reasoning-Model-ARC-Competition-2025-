#!/usr/bin/env python3
"""
Test script for the Novel Reasoning Engine

This script demonstrates the basic functionality of the novel reasoning engine
with a simple pattern recognition problem.
"""

import asyncio
import os
import sys
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent / "src"))

from arcft.novel_reasoning import NovelReasoningEngine
from dotenv import load_dotenv

async def test_novel_reasoning():
    """Test the novel reasoning engine with a simple problem"""
    
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please create a .env file with your OpenAI API key:")
        print("OPENAI_API_KEY=your_actual_api_key_here")
        return False
    
    print("🧠 Testing Novel Reasoning Engine...")
    print("=" * 50)
    
    try:
        # Initialize the engine
        print("🚀 Initializing engine...")
        engine = NovelReasoningEngine(api_key)
        print("✅ Engine initialized successfully!")
        
        # Test problem
        test_problem = """
        Consider this sequence of numbers: 1, 3, 6, 10, 15
        
        What is the pattern, and what should the next number be?
        Explain your reasoning step by step.
        """
        
        print(f"\n📝 Test Problem:")
        print(test_problem.strip())
        print("=" * 50)
        
        # Solve the problem
        print("\n🧠 Starting novel reasoning process...")
        result = await engine.solve_problem(test_problem)
        
        # Display results
        print("\n🎯 REASONING RESULTS:")
        print("=" * 50)
        
        # Character thoughts
        print(f"\n📚 Philosophical Perspectives:")
        for char, thought in result["character_thoughts"].items():
            print(f"\n{char.upper()}:")
            print(f"  {thought[:200]}{'...' if len(thought) > 200 else ''}")
        
        # Hypotheses
        print(f"\n🔍 Generated Hypotheses:")
        print(f"  {result['hypotheses'][:300]}{'...' if len(result['hypotheses']) > 300 else ''}")
        
        # Dual answers
        print(f"\n💡 Dual Answer Analysis:")
        dual = result["dual_answers"]
        print(f"  Primary Answer: {dual['primary_answer']}")
        print(f"  Alternative Answer: {dual['alternative_answer']}")
        print(f"  Primary Confidence: {dual['primary_confidence']:.2f}")
        print(f"  Alternative Confidence: {dual['alternative_confidence']:.2f}")
        print(f"  Recommended: {dual['recommended_answer']}")
        
        # Learning summary
        print(f"\n📊 Learning Summary:")
        print(f"  New Rules Learned: {result['new_rules_learned']}")
        print(f"  Total Rules: {result['total_rules']}")
        print(f"  Reasoning Steps: {result['reasoning_steps']}")
        
        print(f"\n🎉 Test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_rule_learning():
    """Test the rule learning capabilities"""
    
    print("\n" + "=" * 50)
    print("🧪 Testing Rule Learning...")
    print("=" * 50)
    
    try:
        # Load environment variables
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key:
            print("❌ API key not available for rule learning test")
            return False
        
        engine = NovelReasoningEngine(api_key)
        
        # Test with a different problem to generate new rules
        test_problem2 = """
        Find the pattern in this sequence: A, C, F, J, O
        
        What letter comes next and why?
        """
        
        print(f"📝 Second Test Problem:")
        print(test_problem2.strip())
        
        result2 = await engine.solve_problem(test_problem2)
        
        print(f"\n📚 Rules after second problem:")
        rules = engine.get_learned_rules()
        for i, rule in enumerate(rules, 1):
            print(f"  {i}. {rule.description[:100]}{'...' if len(rule.description) > 100 else ''}")
        
        print(f"\n✅ Rule learning test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Error during rule learning test: {e}")
        return False

async def main():
    """Main test function"""
    
    print("🧠 NOVEL REASONING ENGINE - TEST SUITE")
    print("=" * 60)
    
    # Test basic functionality
    success1 = await test_novel_reasoning()
    
    if success1:
        # Test rule learning
        success2 = await test_rule_learning()
        
        if success1 and success2:
            print("\n🎉 ALL TESTS PASSED!")
            print("\n🚀 The Novel Reasoning Engine is working correctly!")
            print("\n💡 Try running the CLI interface:")
            print("   python src/arcft/scripts/novel_reasoning_cli.py interactive")
        else:
            print("\n⚠️  Some tests failed. Check the error messages above.")
    else:
        print("\n❌ Basic functionality test failed. Cannot proceed with rule learning test.")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    asyncio.run(main())
