from dotenv import load_dotenv
import os
load_dotenv()


if __name__=='__main__':
    print("Hello from LangGraph ReAct with Function calling")
    print(os.getenv("OPENAI_API_KEY"))