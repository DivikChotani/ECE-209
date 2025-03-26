# ECE-209: Security Project

This repository contains implementations of timing and memory-based attacks for educational purposes in the context of ECE-209 (Security) course.

## Project Structure

The repository consists of two main components:

### 1. Timing Attack (`timeHack/`)
- `time_attack_script.py`: Implementation of a timing-based password attack
- `time_password_checker.py`: Password verification system vulnerable to timing attacks

### 2. Memory Attack (`memHack/`)
- `mem_attack_script.py`: Implementation of a memory-based password attack
- `mem_password_checker.exe`: Password verification executable
- `mem_ctl.exe`: Memory control executable

## Description

This project demonstrates two different types of security vulnerabilities:

1. **Timing Attack**: Exploits timing variations in password verification to guess the correct password by analyzing the time taken for different password attempts.

2. **Memory Attack**: Demonstrates how memory-based vulnerabilities can be exploited to extract sensitive information from a running process.

## Implementation Details

### Timing Attack
The timing attack implementation:
- Uses statistical analysis of response times
- Implements a character-by-character password guessing approach
- Measures execution time using `time.perf_counter()`
- Uses median calculations to reduce noise in timing measurements

### Memory Attack
The memory attack implementation:
- Interacts with a running password verification process
- Exploits memory vulnerabilities to extract sensitive information
- Includes both attack script and target executables

## Usage

### Timing Attack
```python
from timeHack.time_attack_script import solution

solver = solution()
password = solver.getPassword()
print(f"Found password: {password}")
```

### Memory Attack
```python
from memHack.mem_attack_script import attack

# Run the memory attack
result = attack()
```

