# 🧠 AI Emotion Detector — NLP Project with Deep Insight Layer

A web-based application that analyzes the emotional tone of user-submitted text using NLP (Natural Language Processing) and visualizes the result with clean, professional UI. It goes beyond simple classification, offering a smart feedback layer to help understand the emotional weight behind the words.

---

## ✨ Key Features

- 🔍 **Multi-emotion detection**: Detects complex emotional content (joy, anger, fear, sadness, surprise, love).
- 📈 **Pie chart visualization**: Emotions are visualized in real-time using clear, expressive pie charts.
- 💡 **Insight generation**: Provides a dynamic interpretation (insight) based on emotional dominance.
- 🧼 **Minimal UI**: Custom-designed HTML/CSS UI for a smooth and clean user experience.
- 🖱️ **Interactive form**: Includes reset button, character counter, loading animation.
- 🔄 **Stateless design**: No login required, lightweight for fast prototyping and further API integration.

---

## ⚙️ Technologies Used

| Tool/Library        | Purpose                                |
|---------------------|----------------------------------------|
| **Python 3.13**     | Core logic                             |
| **Flask**           | Web server / routing                   |
| **Transformers (Hugging Face)** | Pretrained emotion model         |
| **Matplotlib**      | Pie chart generation                   |
| **HTML + CSS**      | UI layout and styling                  |
| **Jinja2**          | Template engine for Flask              |
| **UUID**            | Unique naming for chart images         |

---

## 🧠 Emotion Model Used

- Model: [`bhadresh-savani/distilbert-base-uncased-emotion`](https://huggingface.co/bhadresh-savani/distilbert-base-uncased-emotion)
- Hosted locally, **no API key required**
- Emotions detected: `joy`, `anger`, `fear`, `sadness`, `surprise`, `love`
- Fine for project/demo use – not intended for production workloads

---

## 📂 Project Structure

text_emotions/
│
├── static/
│ ├── styles.css # All custom CSS styling
│ └── <generated_charts>.png
│
├── templates/
│ ├── index.html # Input form UI
│ └── results.html # Results display with chart and insight
│
├── main.py # Flask app logic + routing
├── charts.py # Matplotlib pie chart generation
├── insights.py # AI feedback logic (insight generation)
└── README.md # This file

💬 Why this project matters
In an era where digital communication is constant, understanding how something is said is just as important as what is said.

This project aims to:

Make AI accessible and human-centered

Support journaling, emotional check-ins, and communication analysis

Offer an elegant, lightweight, no-login tool for expression analysis

🛠️ Built with Care
This project is a personal showcase of full-stack AI web integration, done with precision and purpose.
It combines frontend design, backend logic, and modern AI capabilities — with a love for clean code and meaningful interaction.

📌 Future Enhancements (Planned)
🌍 Language detection and multilingual emotion support

📊 Emotion history per user (with authentication)

🧠 Deeper GPT-based feedback: “Want to talk about it?” style prompts

📲 Mobile-ready frontend or React.js integration

🌐 API endpoints for external access (future app integration)
