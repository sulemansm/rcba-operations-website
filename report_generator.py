import os
from groq import Groq

GROQ_API_KEY=os.getenv("GROQ_API_KEY")


def generate_report(event):

    client=Groq(api_key=GROQ_API_KEY)

    prompt=f"""
Write a professional Rotaract club event report.

Sections:
Aim
Execution
Impact Analysis
Follow Up and Feedback

Event Title: {event['title']}
Venue: {event['venue']}
Chief Guest: {event['chief_guest']}

Description: {event['description']}
Pre Event Work: {event['pre_event']}
On Day Work: {event['on_day']}
Post Event Work: {event['post_event']}
Outcome: {event['outcome']}
"""

    resp=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7,
        max_tokens=2000
    )

    return resp.choices[0].message.content