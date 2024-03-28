
# Tiny Devin

TinyDevin is an Intern Software Engineer that takes your task as input ,analyses it , searches Internet for research and builds code on the basis of research.





## Installation

Clone the project

```bash
  git clone https://github.com/anmolkys/TinyDevin
```

Go to the project directory

```bash
  cd TinyDevin
```

Install dependencies

```bash
  pip install -r /path/to/requirements.txt
```




## Setup API keys

Go to libs/llm.py 

```python
key = "your-gemini-key"
```

Go to libs/Tools.py

```python
serper_key = "your-serper-api-key"
browser_key = "your-scrapingAnt-api-key"
```
## Running

To run devin - Change task in tinyDevin.py as per required

```bash
  python tinyDevin.py
```


## Screenshots

- Setting up task variable

[![Screenshot-2024-03-28-225750.png](https://i.postimg.cc/HnHDdPZg/Screenshot-2024-03-28-225750.png)](https://postimg.cc/gXMBK4bS)

- During Execution - Searching the Internet

[![Screenshot-2024-03-28-230408.png](https://i.postimg.cc/Hxr4jpN0/Screenshot-2024-03-28-230408.png)](https://postimg.cc/62NGmNtT)

- After Execution: 

[![ss.png](https://i.postimg.cc/ZRQBQpVp/ss.png)](https://postimg.cc/34gx44Mx)
## Todos

- [ ]  Add .env Support (idk why I did not think of it)
- [ ]  Add a task input
- [ ]  Optimise prompts to increase accuracy
- [ ]  Make a UI (probably)
- [x]  Have fun building
