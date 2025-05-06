# Mood-Book-Generator
A Python desktop application that recommends books based on the user's mood, detected through psychological questions. The app uses a series of questions to assess the user's emotional state and then suggests a curated list of books based on the detected mood.

#Features
10+ Psychological Questions to detect the user's mood.

Mood Detection based on user responses.

Book Recommendations for various moods like Happy, Sad, Calm, Motivated, etc.

Scrollable User Interface created using Tkinter.

Modern and Clean Design for a smooth user experience.

Customizable Moods and Books (easily extendable with more questions and books).

#Tech Stack
Python 3.x

Tkinter (for GUI)

Messagebox (for displaying recommendations)

No external libraries (can be extended with libraries like requests for API calls)

#Setup Instructions
  #Prerequisites
    Make sure you have Python 3.x installed on your system. If not, you can download it from here.

  #Installation
    Clone the repository or download the code files.

  Open a terminal and navigate to the project directory.

  Install any necessary dependencies (if any).

  Run the app using the following command:
    python app.py
  Running the Application
  Once the application is running:

  Answer the 10+ psychological questions.

  Click on "Get Recommendations".

  Based on your answers, the app will suggest a list of 5–10 books tailored to your detected mood.

#Project Structure
mood_book_generator/
├── mood_book_generator.py  # Main Python file with Tkinter UI
├── README.md              # Project documentation
└── requirements.txt       # (Optional) List of dependencies

#Future Enhancements
Mood-specific emojis for a more personalized experience.

Book cover images using APIs like Google Books API or Open Library.

Real-time sentiment analysis using external libraries like TextBlob or transformers.

Save recommendations to a file for later review.

Web app version using Flask or Django for wider access.
