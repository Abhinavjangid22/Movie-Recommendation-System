# 🎬 Movie Recommendation System

A personalized **content-based movie recommendation system** that suggests movies similar to the one you search — based on **overview**, **cast**, and **music director**. It fetches posters and movie details using the **TMDb API** and displays them in a clean, modern, Netflix-style UI.

---

## 🔥 What It Does

- 🔍 You enter the name of a movie you like.
- 🎥 It finds **9 similar movies** based on story, cast, and music.
- 🧾 You see movie **posters**, **overview**, **top cast**, and **music director**.
- 🎨 All displayed beautifully in a **Netflix-inspired layout** — clean, responsive, and easy to use.
- 🌐 Data like posters and descriptions come live from the **TMDb API**.

---

## 🧠 Tech Stack

| Layer         | Tools & Libraries                            |
|---------------|-----------------------------------------------|
| **Backend**   | Python, Flask                                 |
| **Frontend**  | HTML, CSS, Jinja2 templates                   |
| **ML/NLP**    | Pandas, Scikit-learn, CountVectorizer         |
| **Similarity**| Cosine Similarity                             |
| **External API** | TMDb API for real-time movie data         |

---

## 📂 Project Structure

movie-recommendation-system/
│
├── static/ → CSS & static assets
├── templates/ → HTML templates for UI
├── app.py → Main Flask app
├── enhance_dataset.py → Script to enrich movie data
├── enhanced_movies.csv → Final movie dataset used in model
├── model.py → Vectorizer and similarity logic
├── tmdb_utils.py → TMDb API helper functions
├── requirements.txt → All dependencies
├── .gitignore → Ignored files/folders
└── README.md → You are here!


---

## ⚙️ How to Run It Locally

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system

### 2.  Launch the App
bash
python app.py


💡 How It Works
This project uses a content-based filtering algorithm:

Extracts textual features like overview, cast, and music director

Uses CountVectorizer to convert text into vectors

Applies Cosine Similarity to find the closest matches

Returns top 9 similar movies with visuals and details

It’s simple, interpretable, and doesn’t need user history or ratings!

🚀 Future Upgrades (Optional Ideas)
Add genre and IMDb ratings to enhance results

Add filters for year, language, or rating

Deploy on cloud (Render, AWS, or Vercel)

Build a hybrid model using collaborative filtering

🙌 Credits
TMDb for movie metadata and posters

Scikit-learn for similarity modeling

Flask and Jinja for building the backend/frontend

📄 License
This project is licensed under the MIT License. Feel free to use or modify it with credit.
