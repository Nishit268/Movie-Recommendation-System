import streamlit as st
import pickle
import requests
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
st.set_page_config(page_title="MovieMatch", page_icon="https://media.istockphoto.com/id/1642381175/vector/cinema.jpg?s=612x612&w=0&k=20&c=owIct55daWlWRwPbTYLI9Y1IsrgYiqJcpvvgycvxBhE=", layout="wide")

movies = pickle.load(open('movies.pkl', 'rb'))
#Creating vectors for alll the movies.
vectorizer = TfidfVectorizer(stop_words='english')
vector = vectorizer.fit_transform(movies['tags'])
cosine_similarity = cosine_similarity(vector)

def fetch_movie_details(movie_id):
    api_key = "760927dfa125b06d62d56c02c27a110f"
    details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    details_response = requests.get(details_url)
    if details_response.status_code == 200:
        details_data = details_response.json()
        average_voting = details_data.get('vote_average', 'N/A')
        poster_path = details_data.get('poster_path', 'N/A')
        full_poster_path = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path != 'N/A' else 'N/A'
        return average_voting, full_poster_path
    return 'N/A', 'N/A'

def generate_recommendations(user_input=""):
    recommendation_list = {}
    processed_movie_name = user_input.lower().replace(' ', '')
    for index, row in movies.iterrows():
        if processed_movie_name in row['tags']:
            movie_title = row['title']
            movie_index = movies[movies['title'] == movie_title].index[0]
            similar_movies = sorted(list(enumerate(cosine_similarity[movie_index])), key=lambda x: x[1], reverse=True)[:50]
            for i in similar_movies:
                movie_id = movies.iloc[i[0]].movie_id
                recommendation_list.setdefault(movie_id, movies.iloc[i[0]].title)
            return recommendation_list
    return {}

st.markdown("""
<style>
/* Custom styles */
.reportview-container {
    background: url(bg.png) no-repeat center center fixed;
    background-size: cover;
}
.column {
    margin: 10px 5px;
    display: inline-block;
    width: 18vw;
}
.stImage img {
    border-radius: 15px;
}
.grid-item {
    margin-bottom: 10px;
}
/* Hide Streamlit's default icons */
.stImage > div > div > div > button {
    display: none;
}
header .decoration {
    display: none !important;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.block-container>div {
    padding: 10px;
}
.stImage > div > div > div > button {
    display: none;
}
.StyledLinkIconContainer a{
    display: none;
}
header .decoration {
    display: none !important;
}
.custom-header {
    color: #ffffff;
    font-family: 'Roboto';
    text-align: center;
    font-size: 60px !important;
    margin-bottom: 30px;
    margin-right: 50px;
}
.stTextInput input {
    border-radius: 10px;
    padding: 12px;
    height: 38px;
}
button[data-baseweb="button"] {
    background-color: #4CAF50;
    color: white;
    border-radius: 5px;
    border: none;
    padding: 8px 16px;
    cursor: pointer;
    height: 52px;
    transform: translateY(-2px);
}
button[data-baseweb="button"]:hover {
    background-color: #45a049;
}
.stTextInput, .stButton {
    display: flex;
    align-items: center;
    justify-content: center;
}
.css-1d391kg {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
    padding-right: 0.75rem;
    padding-left: 0.75rem;
}
.css-1d391kg e1tzin5v2, .element-container .stImage {
    display: none;
}
.custom-header::before {
    content: none;
}
hr {
    border-top: 2px solid #ccc;
    margin: 20px 0;
}
.logo {
    height: 50px;
    margin-right: 10px;
    vertical-align: middle;
}
.flex-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 30px
}
.logo {
    height: 50px; /* Adjust the size to match your logo */
    display: inline-block; /* Inline-block display for alignment */
    margin-right: 10px; /* Space between logo and header text */
}

.custom-header {
    display: inline-block; /* Inline-block display for alignment */
    font-size: 3rem; /* Large font size for the header text */
    color: white; /* White text color */
    margin: 0; /* Removes default margins */
    padding: 0; /* Adjust or remove padding as needed */
}


</style>
""", unsafe_allow_html=True)


# Header with logo and title centered
st.markdown("""
<div class="flex-container">
    <img src="https://media.istockphoto.com/id/1642381175/vector/cinema.jpg?s=612x612&w=0&k=20&c=owIct55daWlWRwPbTYLI9Y1IsrgYiqJcpvvgycvxBhE=" class="logo">
    <h1 class="custom-header">MovieMatch</h1>
</div>
""", unsafe_allow_html=True)

# Your columns for the search bar and button
left_spacer, mid_section, right_spacer = st.columns([1, 2, 1])
with mid_section:
    search_col, button_col = st.columns([3, 1], gap="small")
    with search_col:
        search_query = st.text_input('', placeholder='Search for a movie...', key='search_bar')
    with button_col:
        search_button = st.button('Recommend', key='search_button')

# Divider
st.markdown('<hr>', unsafe_allow_html=True)

# Recommendations
if search_button and search_query.strip():
    with st.spinner('Generating Recommendations...'):
        recommendations = generate_recommendations(search_query.strip())
else:
    recommendations = generate_recommendations("")

if recommendations:
    n_cols = 5
    n_rows = (len(recommendations) + n_cols - 1) // n_cols
    for i in range(n_rows):
        cols = st.columns(n_cols)
        for j in range(n_cols):
            idx = i * n_cols + j
            if idx < len(recommendations):
                movie_id, movie_name = list(recommendations.items())[idx]
                average_voting, full_poster_path = fetch_movie_details(movie_id)
                with cols[j]:
                    if full_poster_path != 'N/A':
                        st.image(full_poster_path, use_column_width=True)
                    st.markdown(f'<h6>{movie_name}</h6>', unsafe_allow_html=True)
                    st.markdown(f'<p>{"{:.1f}".format(average_voting)} ⭐</p>', unsafe_allow_html=True)
elif search_button:
    st.error("No recommendations found.")
