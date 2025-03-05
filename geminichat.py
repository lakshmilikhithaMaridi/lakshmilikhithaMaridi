import google.generativeai as genai

genai.configure(api_key='AIzaSyDcae-CQUIySMgVdwXpCF4H2A5h2OnoppA')

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat()

while True:
    message = input("Likhitha: ")
    response = chat.send_message(message)

    print("Gemini: " + response.text)