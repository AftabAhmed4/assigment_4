# Professional-style Mad Libs Generator

print("Welcome to the Professional Mad Libs Generator!")

# Collect user inputs
name = input("Enter a name: ")
job_title = input("Enter a job title: ")
company = input("Enter a company name: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb (past tense): ")
noun = input("Enter a noun: ")
place = input("Enter a place: ")

# Story using f-strings
story = f"""
Dear Hiring Manager,

My name is {name}, and I am writing to express my keen interest in the position of {job_title} at {company}.
Throughout my career, I have consistently demonstrated a {adjective} approach to problem-solving and team collaboration.

Recently, I {verb} a complex project involving a cutting-edge {noun}, resulting in a 25% efficiency boost.
I believe my skill set and experience make me a valuable addition to your esteemed team at {company}.

I would be thrilled to discuss this opportunity further at your convenience, either in person or via video call from {place}.

Thank you for your time and consideration.

Sincerely,  
{name}
"""

print("\nHere is your professional-style story:")
print(story)

