# 🛡️ SQL Agent CLI - Command Line Interface

A comprehensive command-line interface for testing and running all SQL Agent scripts (00-04) with ease.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API key
- All dependencies installed (`pip install -r requirements.txt`)

### Basic Usage

```bash
# Navigate to the SQLAgent directory
cd SQLAgent

# Run the CLI
python cli.py --help

# Or on Windows
run_cli.bat --help
```

## 📋 Available Commands

### 1. **Run Scripts**
```bash
# Run a specific script
python cli.py run 00                    # Run script 00 (Simple LLM)
python cli.py run 01                    # Run script 01 (Simple Agent)
python cli.py run 02                    # Run script 02 (Risky Agent)
python cli.py run 03                    # Run script 03 (Guardrailed Agent)
python cli.py run 04                    # Run script 04 (Complex Queries)

# Run multiple scripts
python cli.py run 01 03 04              # Run scripts 01, 03, and 04

# Run all scripts
python cli.py run all                   # Run all scripts in sequence

# Run with verbose output
python cli.py run 01 --verbose          # Show detailed output
```

### 2. **Interactive Mode**
```bash
# Start interactive mode
python cli.py interactive

# In interactive mode, you can use:
# - help     : Show available commands
# - list     : List all scripts
# - status   : Check environment
# - run 01   : Run specific script
# - all      : Run all scripts
# - quit     : Exit
```

### 3. **Environment Management**
```bash
# Check environment status
python cli.py status

# Setup environment (first time)
python cli.py setup

# List available scripts
python cli.py list
```

## 🎯 Script Descriptions

| Script | Name | Description | Security Level |
|--------|------|-------------|----------------|
| 00 | Simple LLM | Basic language model without agents | N/A |
| 01 | Simple Agent | Basic SQL agent with no restrictions | ❌ None |
| 02 | Risky Agent | DANGEROUS demo (allows DELETE) | ⚠️ Dangerous |
| 03 | Guardrailed Agent | Secure SQL agent with safety features | ✅ High |
| 04 | Complex Queries | Advanced analytics capabilities | ✅ High |

## 🔧 Setup Instructions

### First Time Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup environment**:
   ```bash
   python cli.py setup
   ```

3. **Configure API key**:
   - Edit `.env` file
   - Add your Gemini API key: `GEMINI_API_KEY=your_key_here`
   - Get API key from: https://makersuite.google.com/app/apikey

4. **Verify setup**:
   ```bash
   python cli.py status
   ```

### Windows Users

Use the provided batch file for easier execution:

```cmd
# Instead of: python cli.py run all
run_cli.bat run all

# Instead of: python cli.py interactive
run_cli.bat interactive
```

## 📊 Example Workflows

### Testing All Scripts
```bash
# Run all scripts and see results
python cli.py run all

# Output will show:
# ✅ Script 00: Simple LLM - PASS
# ✅ Script 01: Simple Agent - PASS
# ⚠️ Script 02: Risky Agent - PASS (with warnings)
# ✅ Script 03: Guardrailed Agent - PASS
# ✅ Script 04: Complex Queries - PASS
```

### Interactive Testing
```bash
python cli.py interactive

sql-agent> status
✅ GEMINI_API_KEY found in .env file
✅ Database file found
✅ All scripts found
✅ Environment is properly configured!

sql-agent> list
📋 Available Scripts:
✅ 00: Simple LLM - Basic language model without agents
✅ 01: Simple Agent - Basic SQL agent with no restrictions
✅ 02: Risky Agent - DANGEROUS demo (allows DELETE operations)
✅ 03: Guardrailed Agent - Secure SQL agent with safety features
✅ 04: Complex Queries - Advanced analytics capabilities

sql-agent> run 03
🚀 Running script 03: Guardrailed Agent - Secure SQL agent with safety features
...
```

### Development Testing
```bash
# Test specific scripts during development
python cli.py run 03 --verbose

# Test multiple scripts
python cli.py run 01 03 04

# Check environment before running
python cli.py status && python cli.py run all
```

## 🛠️ Advanced Usage

### Custom Script Execution
The CLI automatically handles:
- Environment variable loading
- Database path resolution
- Error handling and reporting
- Output formatting

### Error Handling
- Script failures are caught and reported
- Environment issues are detected and explained
- Detailed error messages help with troubleshooting

### Output Control
- Use `--verbose` for detailed output
- Default mode shows summary results
- Interactive mode provides real-time feedback

## 🔍 Troubleshooting

### Common Issues

**"ModuleNotFoundError"**
```bash
# Ensure dependencies are installed
pip install -r requirements.txt
```

**"GEMINI_API_KEY not found"**
```bash
# Check environment setup
python cli.py status
python cli.py setup
```

**"Database file not found"**
```bash
# Reset the database
python cli.py setup
```

**Script execution fails**
```bash
# Run with verbose output to see details
python cli.py run <script_number> --verbose
```

### Debug Mode
For detailed debugging, you can modify the CLI or run scripts directly:

```bash
# Run script directly for debugging
cd scripts
python 00_simple_llm.py
```

## 📁 File Structure

```
SQLAgent/
├── cli.py                 # Main CLI application
├── test_cli.py           # CLI testing script
├── run_cli.bat           # Windows batch file
├── CLI_README.md         # This documentation
├── .env                  # Environment variables
├── env_template.txt      # Environment template
├── sql_agent_class.db    # SQLite database
├── sql_agent_seed.sql    # Database schema
└── scripts/              # SQL Agent scripts
    ├── 00_simple_llm.py
    ├── 01_simple_agent.py
    ├── 02_risky_delete_demo.py
    ├── 03_guardrailed_agent.py
    ├── 04_complex_queries.py
    └── reset_db.py
```

## 🎓 Learning Path

### Recommended Testing Sequence

1. **Start with environment check**:
   ```bash
   python cli.py status
   ```

2. **Run basic script**:
   ```bash
   python cli.py run 00
   ```

3. **Test simple agent**:
   ```bash
   python cli.py run 01
   ```

4. **See dangerous patterns** (carefully):
   ```bash
   python cli.py run 02
   ```

5. **Test secure implementation**:
   ```bash
   python cli.py run 03
   ```

6. **Explore advanced analytics**:
   ```bash
   python cli.py run 04
   ```

7. **Run all scripts**:
   ```bash
   python cli.py run all
   ```

## 🤝 Contributing

To improve the CLI:
- Add new commands in `cli.py`
- Update tests in `test_cli.py`
- Document changes in `CLI_README.md`

## 📄 License

Educational use encouraged. Part of the SQL Agent Security & Analytics Masterclass.
