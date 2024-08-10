from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    user_input = data['message']
    language = data.get('language', 'en')  # Default to English if no language is selected
    response, options = generate_response(user_input, language)
    emit('response', {'response': response, 'options': options})

def generate_response(user_input, language):
    user_input = user_input.lower()
    
    if language == 'hi':
        responses = {
            "welcome": "किसान सहायक बॉट में आपका स्वागत है! मैं आज आपकी कैसे मदद कर सकता हूँ?",
            "profile_exchange": "किसान प्रोफाइल और फसल विनिमय",
            "expert_services": "विशेषज्ञ सलाह सेवाएँ",
            "community_forums": "समुदाय मंच",
            "what_do": "आप क्या करना चाहेंगे?",
            "enter_crop_search": "कृपया उस फसल का नाम दर्ज करें जिसे आप खोज रहे हैं, और हम उपलब्ध विकल्पों को खोजेंगे।",
            "provide_details": "अपनी प्रोफ़ाइल बनाने या देखने के लिए, कृपया निम्नलिखित विवरण प्रदान करें: खेत का आकार, उगाई गई फसलें, और उपलब्ध मात्राएँ।",
            "list_exchange": "कृपया विनिमय के लिए फसलों की सूची दें और बदले में वांछित फसलें बताएं।",
            "list_sale": "कृपया बेचना चाहते हैं फसलों और उनकी मात्राओं को सूचीबद्ध करें। आप मूल्य सुझाव भी मांग सकते हैं।",
            "pricing_suggestions": "कृपया उस फसल और मात्रा को दर्ज करें जिसे आप बेचना चाहते हैं, और हम वर्तमान बाजार मूल्य सुझाव प्रदान करेंगे।",
            "how_assist": "हम आपकी कैसे सहायता कर सकते हैं?",
            "get_recommendations": "कृपया अपने वर्तमान फसलों, कीट समस्याओं, सिंचाई, या मृदा प्रबंधन के बारे में विवरण प्रदान करें ताकि व्यक्तिगत सलाह दी जा सके।",
            "book_consultation": "कृपया एक परामर्श के लिए समय स्लॉट चुनें।",
            "consultation_booked": "आपकी परामर्श {time} के लिए बुक कर दी गई है। हम आपको विवरण के साथ सूचित करेंगे।",
            "weather_impact": "कृपया अपने स्थान और फसलों का विवरण प्रदान करें, और हम संभावित मौसम प्रभाव का विश्लेषण करेंगे और सुझाव देंगे।",
            "discussion_boards": "आप विभिन्न विषयों पर चर्चा में शामिल हो सकते हैं जैसे फसल प्रबंधन, कीट नियंत्रण, और बाजार प्रवृत्तियाँ। आप किस विषय पर चर्चा करना चाहेंगे?",
            "view_knowledge": "यह विभिन्न कृषि पद्धतियों पर लेखों, वीडियो और ट्यूटोरियल्स का भंडार है। आपको किस विशेष विषय में रुचि है?",
            "share_success": "हम आपकी सफलता के बारे में सुनना चाहेंगे! कृपया अपने अनुभव और साथी किसानों के लिए कोई सुझाव प्रदान करें।",
            "returning_main": "मुख्य मेनू पर वापस जा रहा है। मैं आज आपकी कैसे मदद कर सकता हूँ?",
            "general_interaction": "आप क्या पूछना चाहते हैं?",
            "feedback": "हम आपके फीडबैक की सराहना करते हैं! कृपया हमारे सेवाओं को बेहतर बनाने के लिए अपने विचार साझा करें।",
            "not_sure": "मुझे यकीन नहीं है कि इसका उत्तर कैसे दें। कृपया मेनू से एक विकल्प चुनें।"
        }
    else:
        responses = {
            "welcome": "Welcome to the Farmer Assistant Bot! How can I help you today?",
            "profile_exchange": "Farmer Profile and Crop Exchange",
            "expert_services": "Expert Advisory Services",
            "community_forums": "Community Forums",
            "what_do": "What would you like to do?",
            "enter_crop_search": "Please enter the crop you are looking for, and we will search for available options.",
            "provide_details": "To create or view your profile, please provide the following details: farm size, crops grown, and available quantities.",
            "list_exchange": "Please list the crops you want to exchange and the desired crop(s) in return.",
            "list_sale": "Please list the crops you want to sell and their quantities. You can also ask for pricing suggestions.",
            "pricing_suggestions": "Enter the crop and quantity you wish to sell, and we will provide current market pricing suggestions.",
            "how_assist": "How can we assist you?",
            "get_recommendations": "Please provide details about your current crops, pest issues, irrigation, or soil management for personalized advice.",
            "book_consultation": "Please select a time slot for a consultation with an agricultural expert.",
            "consultation_booked": "Your consultation is booked for {time}. We will notify you with the details shortly.",
            "weather_impact": "Please provide details about your location and crops, and we'll analyze the potential weather impact and offer suggestions.",
            "discussion_boards": "You can join discussions on various topics like crop management, pest control, and market trends. What topic would you like to discuss?",
            "view_knowledge": "Here is a repository of articles, videos, and tutorials on various agricultural practices. What specific topic are you interested in?",
            "share_success": "We would love to hear about your success! Please provide details about your experience and any tips for fellow farmers.",
            "returning_main": "Returning to the main menu. How can I assist you today?",
            "general_interaction": "What you want to ask?",
            "feedback": "We appreciate your feedback! Please share your thoughts on how we can improve our services.",
            "not_sure": "I'm not sure how to respond to that. Please choose an option from the menu."
        }
    
    if user_input in ['hi', 'hello', 'start']:
        return (responses['welcome'], 
                [responses['profile_exchange'], responses['expert_services'], responses['community_forums']])
    
    elif user_input == "farmer profile and crop exchange":
        return (responses['what_do'], 
                ["Create or View Profile", "List Crops for Exchange", "Search for Crops Available for Exchange", "List Crops for Sale", "Get Pricing Suggestions", "General bot interaction", "Back to Main Menu"])
    
    elif user_input == "search for crops available for exchange":
        return (responses['enter_crop_search'], [])
    
    elif user_input == "create or view profile":
        return (responses['provide_details'], [])
    
    elif user_input == "list crops for exchange":
        return (responses['list_exchange'], [])
    
    elif user_input == "list crops for sale":
        return (responses['list_sale'], [])
    
    elif user_input == "get pricing suggestions":
        return (responses['pricing_suggestions'], [])
    
    elif user_input == "expert advisory services":
        return (responses['how_assist'], 
                ["Get AI-driven Recommendations", "Book a Live Consultation", "Consult on Weather Impact", "Back to Main Menu"])
    
    elif user_input == "get ai-driven recommendations":
        return (responses['get_recommendations'], [])
    
    elif user_input == "book a live consultation":
        return (responses['book_consultation'], [])
    
    elif "at" in user_input and ("am" in user_input or "pm" in user_input):
        return (responses['consultation_booked'].format(time=user_input), 
                ["Back to Main Menu"])

    elif user_input == "consult on weather impact":
        return (responses['weather_impact'], [])
    
    elif user_input == "community forums":
        return (responses['what_do'], 
                ["Join Discussion Boards", "View Knowledge Base", "Share Success Stories", "Back to Main Menu"])
    
    elif user_input == "join discussion boards":
        return (responses['discussion_boards'], [])
    
    elif user_input == "view knowledge base":
        return (responses['view_knowledge'], [])
    
    elif user_input == "share success stories":
        return (responses['share_success'], [])
    
    elif user_input == "back to main menu":
        return (responses['returning_main'], 
                [responses['profile_exchange'], responses['expert_services'], responses['community_forums']])
    
    elif user_input == "general bot interaction":
        return (responses['general_interaction'], ["Access Tutorials", "Request Technical Support", "Learn about Government Schemes", "Provide Feedback"])
    
    elif user_input == "provide feedback":
        return (responses['feedback'], [])
        
    else:
        return (responses['not_sure'], 
                [responses['profile_exchange'], responses['expert_services'], responses['community_forums']])

if __name__ == '__main__':
    socketio.run(app, debug=True)
