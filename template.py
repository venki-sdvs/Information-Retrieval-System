import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

list_of_files =[
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/helper.py",
    "config/config.yaml",
    ".env",
    "requirements.tct",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
]

for filepath in list_of_git credential reject https://github.com
git credential fill <<EOF
protocol=https
host=github.com
EOF files:
    filepath = Path(filepath)
    filedir, filename =os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory;{filedir} for the file:{filename}")
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filename)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file:{filepath}")
            
    else:
        logging.info(f"{filename} is already exists")
        
        