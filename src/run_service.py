import uvicorn
from dotenv import load_dotenv

from core import settings

load_dotenv()

if __name__ == "__main__":
    # import sys
    # import os
    #
    # print("Current working directory:", os.getcwd())
    # print("PYTHONPATH:", sys.path)
    uvicorn.run("service:app",
                host=settings.HOST,
                port=settings.PORT,
                reload=settings.is_dev()
                )
