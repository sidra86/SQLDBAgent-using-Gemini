#!/usr/bin/env python3
"""
Test script for SQL Agent CLI functionality.

This script tests the CLI without requiring actual API calls.
"""

import subprocess
import sys
from pathlib import Path

def test_cli_help():
    """Test CLI help functionality."""
    print("🧪 Testing CLI help...")
    try:
        result = subprocess.run([sys.executable, "cli.py", "--help"], 
                              capture_output=True, text=True, cwd=Path(__file__).parent)
        if result.returncode == 0 and "SQL Agent CLI" in result.stdout:
            print("✅ CLI help test passed")
            return True
        else:
            print("❌ CLI help test failed")
            return False
    except Exception as e:
        print(f"❌ CLI help test error: {e}")
        return False

def test_cli_list():
    """Test CLI list functionality."""
    print("🧪 Testing CLI list...")
    try:
        result = subprocess.run([sys.executable, "cli.py", "list"], 
                              capture_output=True, text=True, cwd=Path(__file__).parent)
        if result.returncode == 0 and "Available Scripts" in result.stdout:
            print("✅ CLI list test passed")
            return True
        else:
            print("❌ CLI list test failed")
            return False
    except Exception as e:
        print(f"❌ CLI list test error: {e}")
        return False

def test_cli_status():
    """Test CLI status functionality."""
    print("🧪 Testing CLI status...")
    try:
        result = subprocess.run([sys.executable, "cli.py", "status"], 
                              capture_output=True, text=True, cwd=Path(__file__).parent)
        if result.returncode == 0:
            print("✅ CLI status test passed")
            return True
        else:
            print("❌ CLI status test failed")
            return False
    except Exception as e:
        print(f"❌ CLI status test error: {e}")
        return False

def main():
    """Run all CLI tests."""
    print("🚀 Starting CLI Tests")
    print("=" * 40)
    
    tests = [
        test_cli_help,
        test_cli_list,
        test_cli_status
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("📊 Test Results:")
    print(f"✅ Passed: {passed}/{total}")
    print(f"❌ Failed: {total - passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed!")
        return True
    else:
        print("⚠️  Some tests failed")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
