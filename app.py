from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# Create chatbot instance
chatbot = ChatBot("VTU Mysore Bot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///vtu_mysore_bot.sqlite3'
)

trainer = ListTrainer(chatbot)
trainer.train([
    "What is the exam schedule?", 
    "The VTU Mysore exam schedule is available on the VTU official website under 'Examinations'.",
    "When is the last date for fee payment?",
    "The last date for fee payment at VTU Mysore is announced via official notifications on the VTU portal.",
    "Where is the VTU Mysore library located?",
    "The VTU Mysore Library is located in the main campus building at Mysore.",
    "What are the VTU Mysore library timings?",
    "The VTU Mysore library timings are from 9 AM to 6 PM on weekdays.",
    "How do I register for VTU Mysore events?",
    "You can register for VTU Mysore events on the Mysore campus portal or VTU official website.",
    "Who should I contact for academic counseling at VTU Mysore?",
    "Contact the academic counselor at VTU Mysore via the Mysore campus office or email counselor@vtu-mysore.edu.in.",
])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get('msg')
    response = chatbot.get_response(user_input)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
