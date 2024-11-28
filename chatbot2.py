import tkinter as tk
from tkinter import scrolledtext, font

faq_data = {
    "fee structure": "The fee structure for undergraduate programs is around ₹20,000 per year. For postgraduate programs, it varies based on the course and ranges from ₹20,000 to ₹40,000 per year.",
    "location": "JNTU-GV is located in Dwarapudi, Vizianagaram, Andhra Pradesh, India.",
    "student strength": "JNTU-GV has an approximate student strength of around 2,500 to 3,000 students across various programs.",
    "history": "JNTU-GV was established in January 2022. It was originally the University College of Engineering Vizianagaram and later upgraded to an autonomous university.",
    "branches": "The university offers various branches in engineering, including Computer Science, Civil, Electronics and Communication, Mechanical, Information Technology, and Metallurgical Engineering.",
    "number of faculty": "JNTU-GV has around 150 faculty members, who specialize in various fields within the engineering and technical disciplines.",
    "facilities": "The university has facilities such as a library, hostels, sports amenities, banking services, a canteen, and a dispensary.",
    "admission process": "For undergraduate programs, admissions are based on EAPCET scores. For postgraduate programs, GATE or PGECET scores are required.",
    "contact information": "You can reach JNTU-GV at +91-08922-123456 or visit their website at https://jntugv.edu.in.",
    "academics": "JNTU-GV offers undergraduate and postgraduate programs in various engineering disciplines. It also focuses on research in emerging fields and promotes innovation among students.",
    "sports": "JNTU-GV provides sports facilities for cricket, football, basketball, and indoor games. It encourages students to participate in sports events and maintains facilities to support a range of athletic activities."
}

def get_response(user_input, initial_greeting_shown):
    if not initial_greeting_shown:
        if user_input.lower() in ["hi", "hello"]:
            greeting_message = (
                "Hi! I'm here to help you with information about JNTU-GV.\n\n"
                "You can ask about:\n"
                "1. Fee structure\n"
                "2. Location\n"
                "3. Student strength\n"
                "4. History\n"
                "5. Available branches\n"
                "6. Number of faculty\n"
                "7. Facilities\n"
                "8. Admission process\n"
                "9. Contact information\n"
                "10. Academics\n"
                "11. Sports\n\n"
                "Type 'menu' to see these options again."
            )
            return greeting_message, True
        else:
            return "Please start by saying 'Hi' or 'Hello' to begin.", False
    elif user_input.lower() == "menu":
        return (
            "Here's what you can ask about:\n"
            "1. Fee structure\n"
            "2. Location\n"
            "3. Student strength\n"
            "4. History\n"
            "5. Available branches\n"
            "6. Number of faculty\n"
            "7. Facilities\n"
            "8. Admission process\n"
            "9. Contact information\n"
            "10. Academics\n"
            "11. Sports\n"
            "Type your question below!"
        ), True
    else:
        for key in faq_data:
            if key in user_input.lower():
                return faq_data[key], True
        return "I'm sorry, I don't have information on that topic. Please ask another question or type 'menu' to see options.", True
    
def chatbot_interface():
    root = tk.Tk()
    root.title("JNTU-GV Chatbot")
    root.geometry("550x600")
    root.configure(bg="#34495E")
    title_font = font.Font(family="Comic Sans MS", size=18, weight="bold")
    text_font = font.Font(family="Arial", size=12)
    title_label = tk.Label(root, text="Welcome to JNTU-GV Chatbot", font=title_font, fg="#ECF0F1", bg="#34495E")
    title_label.pack(pady=10)
    conversation_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=20, width=55, font=text_font)
    conversation_area.pack(pady=10, padx=10)
    conversation_area.configure(bg="#ECF0F1", fg="#2C3E50")
    initial_greeting_shown = False

    def update_conversation(user_input, bot_response):
        conversation_area.config(state='normal')
        conversation_area.insert(tk.END, f"You: {user_input}\n", "user_text")
        conversation_area.insert(tk.END, f"Bot: {bot_response}\n\n", "bot_text")
        conversation_area.config(state='disabled')
        conversation_area.tag_config("user_text", foreground="#1ABC9C")
        conversation_area.tag_config("bot_text", foreground="#E74C3C")
        conversation_area.see(tk.END)

    user_input_box = tk.Entry(root, width=40, font=text_font, bg="#2C3E50", fg="#ECF0F1")
    user_input_box.pack(pady=10)

    def handle_user_input():
        nonlocal initial_greeting_shown
        user_input = user_input_box.get()
        if user_input:
            bot_response, initial_greeting_shown = get_response(user_input, initial_greeting_shown)
            update_conversation(user_input, bot_response)
            user_input_box.delete(0, tk.END)
    submit_button = tk.Button(root, text="Ask", command=handle_user_input, font=text_font, bg="#3498DB", fg="white", width=10)
    submit_button.pack(pady=5)
    root.mainloop()
chatbot_interface()