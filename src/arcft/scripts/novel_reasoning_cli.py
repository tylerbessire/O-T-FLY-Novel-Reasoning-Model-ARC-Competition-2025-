#!/usr/bin/env python3
"""
Command Line Interface for the Novel Reasoning Engine

This script provides an easy-to-use CLI for the novel reasoning engine,
allowing users to solve problems, view learned rules, and manage the system.
"""

import asyncio
import argparse
import json
import sys
import os
from pathlib import Path
from typing import Optional

# Add the parent directory to the path to import the novel reasoning module
sys.path.append(str(Path(__file__).parent.parent))

from novel_reasoning import NovelReasoningEngine

async def solve_problem(engine: NovelReasoningEngine, problem: str, context: str = ""):
    """Solve a problem using the novel reasoning engine"""
    print("🧠 Starting novel reasoning process...")
    print("=" * 60)
    
    try:
        result = await engine.solve_problem(problem, context)
        
        print("\n🎯 REASONING RESULTS:")
        print("=" * 60)
        
        # Display character thoughts
        print(f"\n📚 Philosophical Perspectives:")
        for char, thought in result["character_thoughts"].items():
            print(f"\n{char.upper()}:")
            print(f"  {thought[:300]}{'...' if len(thought) > 300 else ''}")
        
        # Display hypotheses
        print(f"\n🔍 Generated Hypotheses:")
        print(f"  {result['hypotheses'][:400]}{'...' if len(result['hypotheses']) > 400 else ''}")
        
        # Display dual answers
        print(f"\n💡 Dual Answer Analysis:")
        dual = result["dual_answers"]
        print(f"  Primary Answer: {dual['primary_answer']}")
        print(f"  Alternative Answer: {dual['alternative_answer']}")
        print(f"  Primary Confidence: {dual['primary_confidence']:.2f}")
        print(f"  Alternative Confidence: {dual['alternative_confidence']:.2f}")
        print(f"  Recommended: {dual['recommended_answer']}")
        
        # Display reasoning comparison
        print(f"\n🤔 Reasoning Comparison:")
        print(f"  {dual['reasoning_comparison'][:300]}{'...' if len(dual['reasoning_comparison']) > 300 else ''}")
        
        # Display learning summary
        print(f"\n📊 Learning Summary:")
        print(f"  New Rules Learned: {result['new_rules_learned']}")
        print(f"  Total Rules: {result['total_rules']}")
        print(f"  Reasoning Steps: {result['reasoning_steps']}")
        
        print(f"\n🎉 Novel reasoning completed successfully!")
        
        return result
        
    except Exception as e:
        print(f"❌ Error during reasoning: {e}")
        return None

async def view_rules(engine: NovelReasoningEngine, rule_id: Optional[str] = None):
    """View learned rules"""
    rules = engine.get_learned_rules()
    
    if not rules:
        print("📚 No rules have been learned yet.")
        return
    
    if rule_id:
        # Show specific rule
        rule = next((r for r in rules if r.rule_id == rule_id), None)
        if rule:
            print(f"\n📖 Rule: {rule.rule_id}")
            print("=" * 40)
            print(f"Description: {rule.description}")
            print(f"Pattern: {rule.pattern}")
            print(f"Confidence: {rule.confidence:.2f}")
            print(f"Usage Count: {rule.usage_count}")
            print(f"Success Rate: {rule.success_rate:.2f}")
            print(f"Created: {rule.created_at}")
            print(f"Last Used: {rule.last_used}")
        else:
            print(f"❌ Rule with ID '{rule_id}' not found.")
    else:
        # Show all rules
        print(f"\n📚 Learned Rules ({len(rules)} total):")
        print("=" * 60)
        
        for i, rule in enumerate(rules, 1):
            print(f"\n{i}. {rule.rule_id}")
            print(f"   Description: {rule.description[:100]}{'...' if len(rule.description) > 100 else ''}")
            print(f"   Confidence: {rule.confidence:.2f} | Usage: {rule.usage_count} | Success: {rule.success_rate:.2f}")

async def view_history(engine: NovelReasoningEngine, limit: int = 10):
    """View reasoning history"""
    history = engine.get_reasoning_history()
    
    if not history:
        print("📝 No reasoning history available.")
        return
    
    print(f"\n📝 Recent Reasoning Steps (showing last {min(limit, len(history))}):")
    print("=" * 60)
    
    for i, step in enumerate(history[-limit:], 1):
        print(f"\n{i}. {step.character.upper()} - {step.timestamp}")
        print(f"   {step.thought[:150]}{'...' if len(step.thought) > 150 else ''}")

async def interactive_mode(engine: NovelReasoningEngine):
    """Run the engine in interactive mode"""
    print("🎭 Interactive Novel Reasoning Mode")
    print("=" * 40)
    print("Type 'help' for commands, 'quit' to exit")
    
    while True:
        try:
            command = input("\n🧠 > ").strip().lower()
            
            if command == 'quit' or command == 'exit':
                print("👋 Goodbye!")
                break
            elif command == 'help':
                print("\n📖 Available Commands:")
                print("  solve <problem> - Solve a problem")
                print("  rules - View all learned rules")
                print("  history - View reasoning history")
                print("  clear - Clear reasoning history")
                print("  quit/exit - Exit interactive mode")
            elif command.startswith('solve '):
                problem = command[6:].strip()
                if problem:
                    await solve_problem(engine, problem)
                else:
                    print("❌ Please provide a problem to solve.")
            elif command == 'rules':
                await view_rules(engine)
            elif command == 'history':
                await view_history(engine)
            elif command == 'clear':
                engine.clear_history()
                print("🧹 Reasoning history cleared.")
            else:
                print("❌ Unknown command. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

async def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="Novel Reasoning Engine CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Solve a specific problem
  python novel_reasoning_cli.py solve "What is the pattern in this sequence: 2, 4, 8, 16?"
  
  # View learned rules
  python novel_reasoning_cli.py rules
  
  # View reasoning history
  python novel_reasoning_cli.py history
  
  # Interactive mode
  python novel_reasoning_cli.py interactive
        """
    )
    
    parser.add_argument(
        'command',
        choices=['solve', 'rules', 'history', 'interactive', 'clear'],
        help='Command to execute'
    )
    
    parser.add_argument(
        '--problem', '-p',
        help='Problem to solve (required for solve command)'
    )
    
    parser.add_argument(
        '--context', '-c',
        default='',
        help='Additional context for the problem'
    )
    
    parser.add_argument(
        '--rule-id', '-r',
        help='Specific rule ID to view (for rules command)'
    )
    
    parser.add_argument(
        '--limit', '-l',
        type=int,
        default=10,
        help='Number of history items to show (default: 10)'
    )
    
    parser.add_argument(
        '--model', '-m',
        default='gpt-5',
        help='OpenAI model to use (default: gpt-5)'
    )
    
    args = parser.parse_args()
    
    # Check for API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set your OpenAI API key in a .env file or environment variable")
        sys.exit(1)
    
    # Initialize the reasoning engine
    try:
        engine = NovelReasoningEngine(api_key, args.model)
        print(f"🚀 Novel Reasoning Engine initialized with {args.model}")
    except Exception as e:
        print(f"❌ Error initializing engine: {e}")
        sys.exit(1)
    
    # Execute command
    try:
        if args.command == 'solve':
            if not args.problem:
                print("❌ Error: Problem is required for solve command")
                print("Use: python novel_reasoning_cli.py solve --problem 'Your problem here'")
                sys.exit(1)
            
            await solve_problem(engine, args.problem, args.context)
            
        elif args.command == 'rules':
            await view_rules(engine, args.rule_id)
            
        elif args.command == 'history':
            await view_history(engine, args.limit)
            
        elif args.command == 'interactive':
            await interactive_mode(engine)
            
        elif args.command == 'clear':
            engine.clear_history()
            print("🧹 Reasoning history cleared.")
            
    except Exception as e:
        print(f"❌ Error executing command: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
