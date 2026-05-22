import customtkinter as ctk
from google import genai

# 🔥 APNI GOOGLE API KEY YAHAN INVERTED COMMAS KE ANDAR PASTE KARO 🔥
GOOGLE_API_KEY = "AIzaSyCV3SN4LdzW1L4dfPWpAiq7r_SJM4PDu7A"

# AI Client ko shuru karna
client = genai.Client(api_key=GOOGLE_API_KEY)

# App ka design set karna
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("🧸 AI Talking Teddy 🧸")
root.geometry("450x550")

def talk_to_teddy():
    bacche_ka_sawaal = input_box.get()
    if not bacche_ka_sawaal:
        output_label.configure(text="Teddy: Kuch likho to sahi dost! 🤔")
        return
    
    output_label.configure(text="Teddy soch raha hai... 💭")
    root.update()
    
    try:
        prompt = f"You are a friendly, loving, and funny talking Teddy Bear for kids. Reply in friendly Urdu/Roman Urdu. The child says: {bacche_ka_sawaal}"
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        output_label.configure(text=f"Teddy 🧸: {response.text}")
    except Exception as e:
        output_label.configure(text="Oops! Internet ka masla hai ya API Key ghalat hai. 😢")

# --- APP INTERFACE ---
heading = ctk.CTkLabel(root, text="🧸 AI TALKING TEDDY 🧸", font=("Arial", 24, "bold"), text_color="#FFCC00")
heading.pack(pady=20)

instruction = ctk.CTkLabel(root, text="Teddy se jo dil chahe poocho (Kahani, Math, Game)! 👇", font=("Arial", 13))
instruction.pack(pady=5)

input_box = ctk.CTkEntry(root, placeholder_text="Teddy se baatein karo...", width=350, corner_radius=10)
input_box.pack(pady=10)

btn = ctk.CTkButton(root, text="Teddy Ko Btao 🗣️", font=("Arial", 14, "bold"), command=talk_to_teddy, corner_radius=20, fg_color="#FF5733", hover_color="#C70039")
btn.pack(pady=15)

output_frame = ctk.CTkScrollableFrame(root, width=380, height=250, corner_radius=10)
output_frame.pack(pady=10)

output_label = ctk.CTkLabel(output_frame, text="Hi! Main aapka AI Teddy hoon. Aaj hum kya khelein? ✨", font=("Arial", 14), text_color="#00FFCC", wraplength=350, justify="left")
output_label.pack(padx=10, pady=10)

root.mainloop()