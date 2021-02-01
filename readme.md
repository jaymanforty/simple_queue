# simple_queue
Simple Discord bot to allow queuing in text channels

# Download Project
`git clone https://github.com/jaymanforty/simple_queue.git`

# Create and activate a virtual environment in the project directory
`python -m venv venv`
`venv\Scripts\activate`

# Install project dependencies
```
pip install discord
pip install pyyaml
pip install python-dotenv
```

# Set up the bot
`In .env.example enter bot token and rename the file to .env`

# Run
`python run.py`
* A new directory 'cfg' with files 'config.yml' and 'cogs.yml' should have been created after first time run. Change or add whatever you need to in 'config.yml'
* Run the bot again after entering desired changes

# Commands for the bot
* join, j
* leave, l
* queue, q
* clear, c
* forcejoin
* forceleave
* freeze
* unfreeze
