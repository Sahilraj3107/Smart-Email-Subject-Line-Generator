import os
import dotenv
from langchain_groq import ChatGroq 
from langchain_core.prompts import PromptTemplate



os.environ['GROQ_API_KEY'] =dotenv.get_key(dotenv.find_dotenv(), "GROQ_API_KEY")

model = ChatGroq(model ="llama-3.1-8b-instant" , temperature=0.6)


# response = model.invoke("What is the lifestyle of successful people?")
# print(response.content)

prompt_template = PromptTemplate.from_template("I will provide you the email body and you have to generate its title and subject, In professional way.And make it humanly as possible. The email body is: {email_body}")

email = input("Enter you email body: ")

prompt = prompt_template.format(email_body = email)
response = model.invoke(prompt)


print("The email title and subject is: ",response.content)

# Hi Team,I hope this message finds you well. I wanted to schedule a quick meeting to discuss the progress on our current project. We need to review the timeline and address any blockers that might be affecting our delivery.Could we meet this Thursday at 2 PM? Please let me know if this works for everyone, or suggest an alternative time that suits you better.Looking forward to hearing from you.Best regards,Sarah

