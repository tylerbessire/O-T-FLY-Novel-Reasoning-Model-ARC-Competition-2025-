#!/usr/bin/env python3
"""
Demo Script for Novel Reasoning Engine

This script demonstrates the key features of our novel reasoning engine
with a simple pattern recognition example.
"""

import asyncio
import os
import sys
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent / "src"))

from arcft.novel_reasoning import NovelReasoningEngine

async def demo_novel_reasoning():
    """Demonstrate the novel reasoning engine capabilities"""
    
    print("🧠 NOVEL REASONING ENGINE DEMO")
    print("=" * 50)
    
    # Check for API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set your OpenAI API key:")
        print("export OPENAI_API_KEY='your_key_here'")
        return
    
    # Initialize the engine
    print("🚀 Initializing Novel Reasoning Engine...")
    engine = NovelReasoningEngine(api_key, "gpt-5")
    
    # Demo problem: Pattern recognition
    problem = """
    I have a sequence of numbers: 2, 4, 8, 16, 32, ?
    
    What comes next in this sequence? Explain your reasoning process.
    """
    
    print(f"\n📝 Problem: {problem.strip()}")
    print("\n🤔 Solving with novel reasoning engine...")
    print("   (This will use meta-cognition, philosophical character compartmentalization,")
    print("    hypothesis generation, and dual-answer generation)")
    
    try:
        # Solve the problem
        result = await engine.solve_problem(
            problem,
            context="Mathematical pattern recognition"
        )
        
        if result:
            print("\n✅ SOLUTION GENERATED!")
            print("=" * 50)
            
            # Display the reasoning process
            print("🧠 REASONING PROCESS:")
            print(f"   Meta-cognitive reflection: {result.meta_cognition}")
            print(f"   Hypotheses generated: {len(result.hypotheses)}")
            
            # Display hypotheses
            for i, hypothesis in enumerate(result.hypotheses):
                print(f"   Hypothesis {i+1}: {hypothesis}")
            
            # Display answers
            print(f"\n💡 ANSWERS GENERATED: {len(result.answers)}")
            for i, answer in enumerate(result.answers):
                print(f"\n   Answer {i+1} (Confidence: {answer.confidence:.1f}%):")
                print(f"   {answer.answer}")
                print(f"   Reasoning: {answer.reasoning}")
            
            # Display learned rules
            if result.learned_rules:
                print(f"\n📚 RULES LEARNED: {len(result.learned_rules)}")
                for rule in result.learned_rules:
                    print(f"   • {rule}")
            
            # Display philosophical character insights
            if result.character_insights:
                print(f"\n🎭 PHILOSOPHICAL CHARACTER INSIGHTS:")
                for character, insight in result.character_insights.items():
                    print(f"   {character}: {insight}")
            
            print("\n🎉 Demo completed successfully!")
            print("   The novel reasoning engine demonstrated:")
            print("   • Meta-cognition and self-reflection")
            print("   • Multiple hypothesis generation")
            print("   • Dual-answer generation")
            print("   • Rule learning and abstraction")
            print("   • Philosophical character compartmentalization")
            
        else:
            print("❌ No result generated")
            
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        print("   This might be due to API rate limits or connectivity issues")

async def demo_arc_style_problem():
    """Demonstrate with an ARC-style pattern recognition problem"""
    
    print("\n" + "=" * 60)
    print("🧩 ARC-STYLE PATTERN RECOGNITION DEMO")
    print("=" * 60)
    
    # Check for API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        return
    
    # Initialize the engine
    engine = NovelReasoningEngine(api_key, "gpt-5")
    
    # ARC-style problem
    problem = """
    I have a pattern recognition problem:
    
    Training Example 1:
    Input:  [1, 2, 3]
    Output: [2, 4, 6]
    
    Training Example 2:
    Input:  [4, 5, 6]
    Output: [8, 10, 12]
    
    Test Input: [7, 8, 9]
    
    What should the output be? Explain the pattern you identified.
    """
    
    print(f"📝 Problem: {problem.strip()}")
    print("\n🤔 Solving with novel reasoning engine...")
    
    try:
        result = await engine.solve_problem(
            problem,
            context="ARC-style pattern recognition"
        )
        
        if result:
            print("\n✅ PATTERN RECOGNITION COMPLETED!")
            print("=" * 50)
            
            # Display the pattern analysis
            print("🔍 PATTERN ANALYSIS:")
            for i, hypothesis in enumerate(result.hypotheses):
                print(f"   Pattern {i+1}: {hypothesis}")
            
            # Display the solution
            print(f"\n💡 SOLUTION:")
            for i, answer in enumerate(result.answers):
                print(f"   Answer {i+1}: {answer.answer}")
                print(f"   Reasoning: {answer.reasoning}")
            
            print("\n🎯 This demonstrates the engine's ability to:")
            print("   • Identify mathematical patterns")
            print("   • Generalize from examples")
            print("   • Apply patterns to new inputs")
            print("   • Provide clear reasoning explanations")
            
        else:
            print("❌ No result generated")
            
    except Exception as e:
        print(f"❌ Error during ARC demo: {e}")

async def main():
    """Main demo function"""
    print("🌟 Welcome to the Novel Reasoning Engine Demo!")
    print("This will showcase the advanced reasoning capabilities.")
    
    # Run the main demo
    await demo_novel_reasoning()
    
    # Run the ARC-style demo
    await demo_arc_style_problem()
    
    print("\n🎊 Demo completed!")
    print("\n💡 Next steps:")
    print("   1. Try the ARC test runner: python arc_test_runner.py")
    print("   2. Explore the novel reasoning engine capabilities")
    print("   3. Test with your own problems")
    print("\n🚀 Ready to revolutionize AI reasoning!")

if __name__ == "__main__":
    asyncio.run(main())
