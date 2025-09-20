#!/usr/bin/env python3
"""
SQL Agent CLI - Command Line Interface for Testing SQL Agent Scripts

This CLI tool provides an easy way to test and run all the SQL Agent scripts
(00-04) with various options and configurations.

Usage:
    python cli.py --help                    # Show help
    python cli.py run 00                    # Run script 00
    python cli.py run all                   # Run all scripts
    python cli.py interactive               # Interactive mode
    python cli.py setup                     # Setup environment
    python cli.py status                    # Check status
"""

import argparse
import os
import sys
import subprocess
import time
from pathlib import Path
from typing import List, Optional
import json

class SQLAgentCLI:
    """Main CLI class for SQL Agent operations."""
    
    def __init__(self):
        self.script_dir = Path(__file__).parent / "scripts"
        self.env_file = Path(__file__).parent / ".env"
        self.db_file = Path(__file__).parent / "sql_agent_class.db"
        self.scripts = {
            "00": "00_simple_llm.py",
            "01": "01_simple_agent.py", 
            "02": "02_risky_delete_demo.py",
            "03": "03_guardrailed_agent.py",
            "04": "04_complex_queries.py"
        }
        self.script_descriptions = {
            "00": "Simple LLM - Basic language model without agents",
            "01": "Simple Agent - Basic SQL agent with no restrictions",
            "02": "Risky Agent - DANGEROUS demo (allows DELETE operations)",
            "03": "Guardrailed Agent - Secure SQL agent with safety features",
            "04": "Complex Queries - Advanced analytics capabilities"
        }

    def print_banner(self):
        """Print the CLI banner."""
        print("=" * 60)
        print("🛡️  SQL Agent CLI - Security & Analytics Testing Tool")
        print("=" * 60)
        print()

    def check_environment(self) -> bool:
        """Check if the environment is properly set up."""
        issues = []
        
        # Check if .env file exists
        if not self.env_file.exists():
            issues.append(f"❌ .env file not found at {self.env_file}")
        else:
            # Check if GEMINI_API_KEY is set
            with open(self.env_file, 'r') as f:
                content = f.read()
                if "GEMINI_API_KEY=your_gemini_api_key_here" in content or "GEMINI_API_KEY=" not in content:
                    issues.append("❌ GEMINI_API_KEY not properly configured in .env file")
                else:
                    print("✅ GEMINI_API_KEY found in .env file")
        
        # Check if database exists
        if not self.db_file.exists():
            issues.append(f"❌ Database file not found at {self.db_file}")
        else:
            print("✅ Database file found")
        
        # Check if scripts exist
        missing_scripts = []
        for script_num, script_file in self.scripts.items():
            script_path = self.script_dir / script_file
            if not script_path.exists():
                missing_scripts.append(f"{script_num}: {script_file}")
        
        if missing_scripts:
            issues.append(f"❌ Missing scripts: {', '.join(missing_scripts)}")
        else:
            print("✅ All scripts found")
        
        if issues:
            print("\n🚨 Environment Issues Found:")
            for issue in issues:
                print(f"  {issue}")
            return False
        
        print("✅ Environment is properly configured!")
        return True

    def setup_environment(self):
        """Set up the environment for first-time use."""
        print("🔧 Setting up SQL Agent environment...")
        
        # Create .env file if it doesn't exist
        if not self.env_file.exists():
            env_template = self.env_file.parent / "env_template.txt"
            if env_template.exists():
                print("📝 Creating .env file from template...")
                with open(env_template, 'r') as src, open(self.env_file, 'w') as dst:
                    dst.write(src.read())
                print(f"✅ Created .env file at {self.env_file}")
                print("⚠️  Please edit .env and add your actual GEMINI_API_KEY")
            else:
                print("❌ env_template.txt not found")
                return False
        else:
            print("✅ .env file already exists")
        
        # Reset database
        print("🗄️  Setting up database...")
        reset_script = self.script_dir / "reset_db.py"
        if reset_script.exists():
            try:
                result = subprocess.run([sys.executable, str(reset_script)], 
                                      capture_output=True, text=True, cwd=self.script_dir.parent)
                if result.returncode == 0:
                    print("✅ Database reset successfully")
                else:
                    print(f"❌ Database reset failed: {result.stderr}")
                    return False
            except Exception as e:
                print(f"❌ Error resetting database: {e}")
                return False
        else:
            print("❌ reset_db.py not found")
            return False
        
        print("\n🎉 Setup complete! You can now run the scripts.")
        return True

    def list_scripts(self):
        """List all available scripts with descriptions."""
        print("📋 Available Scripts:")
        print("-" * 50)
        for script_num, description in self.script_descriptions.items():
            status = "✅" if (self.script_dir / self.scripts[script_num]).exists() else "❌"
            print(f"{status} {script_num}: {description}")
        print()

    def run_script(self, script_num: str, verbose: bool = True) -> bool:
        """Run a specific script by number."""
        if script_num not in self.scripts:
            print(f"❌ Invalid script number: {script_num}")
            print(f"Available scripts: {', '.join(self.scripts.keys())}")
            return False
        
        script_file = self.scripts[script_num]
        script_path = self.script_dir / script_file
        
        if not script_path.exists():
            print(f"❌ Script file not found: {script_path}")
            return False
        
        print(f"🚀 Running script {script_num}: {self.script_descriptions[script_num]}")
        print("=" * 60)
        
        try:
            # Change to the script directory to ensure proper imports
            result = subprocess.run([sys.executable, str(script_path)], 
                                  cwd=self.script_dir.parent,
                                  capture_output=not verbose,
                                  text=True)
            
            if result.returncode == 0:
                print(f"✅ Script {script_num} completed successfully")
                return True
            else:
                print(f"❌ Script {script_num} failed with return code {result.returncode}")
                if not verbose and result.stderr:
                    print("Error output:")
                    print(result.stderr)
                return False
                
        except Exception as e:
            print(f"❌ Error running script {script_num}: {e}")
            return False

    def run_all_scripts(self, verbose: bool = True) -> dict:
        """Run all scripts in sequence."""
        print("🚀 Running all SQL Agent scripts...")
        print("=" * 60)
        
        results = {}
        
        for script_num in sorted(self.scripts.keys()):
            print(f"\n📝 Script {script_num}: {self.script_descriptions[script_num]}")
            print("-" * 40)
            
            success = self.run_script(script_num, verbose)
            results[script_num] = success
            
            if not success:
                print(f"⚠️  Script {script_num} failed, continuing with next script...")
            
            print()  # Add spacing between scripts
        
        # Summary
        print("📊 Execution Summary:")
        print("=" * 30)
        successful = sum(1 for success in results.values() if success)
        total = len(results)
        
        for script_num, success in results.items():
            status = "✅ PASS" if success else "❌ FAIL"
            print(f"{status} Script {script_num}")
        
        print(f"\n🎯 Results: {successful}/{total} scripts completed successfully")
        return results

    def interactive_mode(self):
        """Start interactive mode for testing scripts."""
        print("🎮 Interactive Mode - SQL Agent Testing")
        print("=" * 50)
        print("Type 'help' for available commands, 'quit' to exit")
        print()
        
        while True:
            try:
                command = input("sql-agent> ").strip().lower()
                
                if command in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                elif command == 'help':
                    self.print_interactive_help()
                elif command == 'list':
                    self.list_scripts()
                elif command == 'status':
                    self.check_environment()
                elif command == 'all':
                    self.run_all_scripts(verbose=False)
                elif command.startswith('run '):
                    script_num = command.split()[1]
                    self.run_script(script_num)
                elif command == '':
                    continue
                else:
                    print(f"❌ Unknown command: {command}")
                    print("Type 'help' for available commands")
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

    def print_interactive_help(self):
        """Print help for interactive mode."""
        print("\n📖 Available Commands:")
        print("  help     - Show this help message")
        print("  list     - List all available scripts")
        print("  status   - Check environment status")
        print("  run <##> - Run specific script (e.g., 'run 01')")
        print("  all      - Run all scripts in sequence")
        print("  quit     - Exit interactive mode")
        print()

    def main(self):
        """Main CLI entry point."""
        parser = argparse.ArgumentParser(
            description="SQL Agent CLI - Test and run SQL Agent scripts",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  python cli.py run 00                    # Run script 00
  python cli.py run all                   # Run all scripts
  python cli.py run 01 02 03              # Run specific scripts
  python cli.py interactive               # Start interactive mode
  python cli.py setup                     # Setup environment
  python cli.py status                    # Check environment status
            """
        )
        
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        
        # Run command
        run_parser = subparsers.add_parser('run', help='Run scripts')
        run_parser.add_argument('scripts', nargs='+', 
                              help='Script numbers to run (00-04) or "all"')
        run_parser.add_argument('--verbose', '-v', action='store_true',
                              help='Show detailed output')
        
        # Interactive command
        subparsers.add_parser('interactive', help='Start interactive mode')
        
        # Setup command
        subparsers.add_parser('setup', help='Setup environment')
        
        # Status command
        subparsers.add_parser('status', help='Check environment status')
        
        # List command
        subparsers.add_parser('list', help='List available scripts')
        
        args = parser.parse_args()
        
        if not args.command:
            parser.print_help()
            return
        
        self.print_banner()
        
        if args.command == 'run':
            if 'all' in args.scripts:
                self.run_all_scripts(args.verbose)
            else:
                for script_num in args.scripts:
                    self.run_script(script_num, args.verbose)
        
        elif args.command == 'interactive':
            self.interactive_mode()
        
        elif args.command == 'setup':
            self.setup_environment()
        
        elif args.command == 'status':
            self.check_environment()
        
        elif args.command == 'list':
            self.list_scripts()

if __name__ == "__main__":
    cli = SQLAgentCLI()
    cli.main()
