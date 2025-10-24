import os
# import dotenv
from dotenv import load_dotenv
from langchain_groq import ChatGroq 
from langchain_core.prompts import PromptTemplate


# work when running locally
# os.environ['GROQ_API_KEY'] =dotenv.get_key(dotenv.find_dotenv(), "GROQ_API_KEY")

#Use when push on github
load_dotenv()

model = ChatGroq(model ="llama-3.1-8b-instant" , temperature=0.6)

prompt_template = PromptTemplate.from_template("I will provide you the email body and you have to generate its title and subject, In professional way.And make it humanly as possible. The email body is: {email_body}")


def get_subject(email_body: str) -> str:
    prompt = prompt_template.format(email_body = email_body)
    response = model.invoke(prompt)
    return response.content

def main():

    if os.getenv("CI"):
        email = """Hi Team,I hope this message finds you well. I wanted to schedule a quick meeting to discuss the progress on our current project. We need to review the timeline and address any blockers that might be affecting our delivery.Could we meet this Thursday at 2 PM? Please let me know if this works for everyone, or suggest an alternative time that suits you better.Looking forward to hearing from you.Best regards,Sarah"""

        print("Running in CI mode")

    else:
        print("Please enter the email body:")
        email = input()
        subject = get_subject(email)
        print("Recommended Subject and Title are: ", subject)    
# Hi Team,I hope this message finds you well. I wanted to schedule a quick meeting to discuss the progress on our current project. We need to review the timeline and address any blockers that might be affecting our delivery.Could we meet this Thursday at 2 PM? Please let me know if this works for everyone, or suggest an alternative time that suits you better.Looking forward to hearing from you.Best regards,Sarah


if __name__ == "__main__":
    main()
