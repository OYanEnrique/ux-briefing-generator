# UX Briefing creator
import os
from groq import Groq

MY_API_KEY = "YOUR_KEY_HERE"

def create_briefing():
    
    print("Welcome to the Briefing Generator with Groq!")
    print("-" * 50)

    # Collect information from the user
    project_description = input("What kind of product or website do you need a briefing for? (e.g., meditation app, plant e-commerce)\n> ")
    target_audience = input("Who is the main target audience for this project? (e.g., young adults, seniors, new parents)\n> ")

    print("\n Understood! Thinking of a briefing for you... Please wait a moment.\n")

    # Preparing to call the Groq API
    try:
        # Initializes the Groq "client" with your key
        groq_client = Groq(api_key=MY_API_KEY)

        # Create the prompt
        
        prompt_for_ai = f"""
        **AI Role:** You are to act as an expert Senior UX/UI Designer with 10+ years of experience in creating intuitive, user-centric, and visually stunning digital products. Your task is to develop a complete design concept based on the detailed briefing below.

---
### **0. The theme

* **What kind of product or website this is:** `{project_description}`

* **Target audience:** `{target_audience}`

### **1. Project Foundation**

* **Creative Project Name:** `[e.g., "FlowState Finance", "TerraNova Eco-Market", "ConnectSphere"]`
* **One-Line Pitch:** `[A single sentence describing the product. e.g., "A mobile app for freelancers to manage their invoices and track payments effortlessly."]`
* **The Core Problem:** `[What specific user problem are you solving? Be specific. e.g., "Freelancers struggle with disorganized financial tracking, leading to missed payments and a poor understanding of their monthly income."]`
* **Business Goals & Success Metrics:** `[What is the primary goal of this project? How will you measure success? e.g., "Goal: Increase user retention by 20% in the first 6 months. Metrics: Daily Active Users (DAU), task completion rate for 'invoice creation', user satisfaction surveys."]`

---

### **2. Target User & Context**

* **Primary Target Audience:** `[Describe your main user group. e.g., "Creative freelancers and independent contractors in North America, aged 25-40, who are tech-savvy but not financial experts."]`
* **User Persona:**
    * **Name:** `[e.g., Alex Chen]`
    * **Age:** `[e.g., 32]`
    * **Occupation:** `[e.g., Freelance Graphic Designer]`
    * **Goals:** `[What do they want to achieve with this product? e.g., "Wants to spend less time on admin, get a clear overview of their financial health, and appear professional to clients."]`
    * **Frustrations/Pain Points:** `[What are their current struggles related to the problem? e.g., "Hates using complex spreadsheets, forgets to follow up on unpaid invoices, feels anxious about tax season."]`
* **Key User Scenarios (User Stories):**
    * `As a user, I want to... [create a new invoice in under 2 minutes] ...so that I can... [bill my clients quickly after finishing a project].`
    * `As a user, I want to... [see a dashboard of my paid vs. unpaid invoices] ...so that I can... [know who to follow up with].`
    * `As a user, I want to... [receive a notification when an invoice is paid] ...so that I can... [feel secure about my cash flow].`

---

### **3. Brand & Visual Identity (UI)**

* **Brand Core Values:** `[List 3-5 keywords that describe the brand's personality. e.g., "Empowering, Simple, Trustworthy, Calm, Professional"]`
* **Visual Style & Mood Keywords:** `[List adjectives for the look and feel. e.g., "Clean, Minimalist, Modern, Approachable, Light, Airy, Data-rich, Sophisticated"]`
* **Color Palette:**
    * **Primary:** `[e.g., A deep, trustworthy blue - #0A2540]`
    * **Secondary/Accent:** `[e.g., A vibrant, energetic green for success states and CTAs - #2ECC71]`
    * **Neutrals:** `[e.g., Light grays for backgrounds (#F6F9FC), dark grays for text (#333333)]`
    * **System Colors:** `[e.g., Red for errors, Yellow for warnings]`
* **Typography:**
    * **Heading Font:** `[e.g., "Inter", Bold. A modern, geometric sans-serif for clarity and impact.]`
    * **Body Font:** `[e.g., "Inter", Regular. Highly legible and clean for data and long-form text.]`
* **Inspiration (What to Emulate):**
    * `[List 2-3 apps or websites you like the visual style of. Explain why. e.g., "Stripe Dashboard - for its clean data visualization and professional feel. Notion - for its minimalist and component-based UI."]`
* **Anti-Inspiration (What to Avoid):**
    * `[List 1-2 apps or websites whose style you dislike. Explain why. e.g., "Avoid cluttered interfaces like old banking apps. Avoid dark, gamified aesthetics that feel unprofessional."]`

---

### **4. Scope & Technical Constraints**

* **Platform(s):** `[e.g., Mobile-first (iOS and Android), Responsive Web App, Desktop-only]`
* **Key Features for this Design Sprint:** `[List the core features to be designed. e.g., "1. User Onboarding & Sign-up, 2. Main Dashboard, 3. Invoice Creation Flow, 4. Client List, 5. Settings Page."]`

---

### **5. Deliverables Required**

Based on all the information above, please generate the following:

1.  **High-Fidelity Mockups** for the following key screens:
    * `[Screen 1: e.g., Login/Sign Up Screen]`
    * `[Screen 2: e.g., Main Dashboard showing key financial metrics]`
    * `[Screen 3: e.g., 'Create New Invoice' form]`
    * `[Screen 4: e.g., List of all invoices with status filters (Paid, Unpaid, Overdue)]`
    * `[Screen 5: e.g., User Profile/Settings Page]`

2.  A **Basic Style Guide / Component Sheet** showing:
    * Color Palette
    * Typography (Headings, Body, Labels)
    * Key UI Components (e.g., Buttons in primary, secondary, and disabled states; Form fields; Dropdown menus; Icons style).

**Final Instruction:** Please review all sections to ensure a cohesive and user-centric design. The final output should feel professional, solve the user's core problem.
        """

        # Make the call to the Groq API
        
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt_for_ai,
                }
            ],
            model="llama3-8b-8192",
        )

        # Show the AI's response to the user
        generated_briefing = chat_completion.choices[0].message.content
        print("-" * 50)
        print("Briefing Generated Successfully! \n")
        print(generated_briefing)
        print("-" * 50)
        with open("briefing_generator.txt", "a") as savefile:
        	savefile.write("\n")
        	savefile.write(generated_briefing)
        	savefile.write("\n" + "="*50)
        	savefile.write("\n")

    except Exception as e:
        # Handling errors
        print(f"\n An error occurred: {e}")
        print("Please check if your API key is correct and if you have an internet connection.")


# Start the program
if __name__ == "__main__":
    create_briefing()