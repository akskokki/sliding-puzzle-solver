# User instructions

## Installation

1. Install dependencies with

```
poetry install
```

2. Launch the game with

```
poetry run invoke start
```

## Usage
Arrow keys: Manual board control  
Space: Weak scramble (100 random moves, scrambling past ~200 moves runs the risk of being too complex to solve)  
Enter: Start solve, and after solution is found progress solve with each press  
R: Enter custom board state as terminal input (String form of 2D List, only intended for copy-pasting previously solved boards from the terminal)

## Testing
Unit tests:

```
poetry run invoke test
```

Coverage report (found in `/htmlcov/index.html`):

```
poetry run invoke coverage-report
```

Pylint static code analysis:

```
poetry run invoke lint
```
