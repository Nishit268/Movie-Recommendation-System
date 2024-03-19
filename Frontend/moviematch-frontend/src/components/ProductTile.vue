<template>
    <div class="main_div">
        <div class="item_1">
            <div class="movie_image">
            <img class="poster" src="https://i.ebayimg.com/images/g/ujkAAOSwYEhjyt9a/s-l1200.webp" alt="">
            </div>
            <div class="movie_name">
                LAST OF US
            </div>
            <div class="ratings">
                IMDB 8/10
            </div>
        </div> 
        <div class="item_1">
            <div class="movie_image">
            <img class="poster" src="https://i.ebayimg.com/images/g/SQcAAOSwBxhkOA-s/s-l1600.jpg" alt="">
            </div>
            <div class="movie_name">
                STAR WARS
            </div>
            
            <div class="ratings">
                IMDB 8/10
            </div>
        </div>  
        <div class="item_1">
            <div class="movie_image">
            <img class="poster" src="https://m.media-amazon.com/images/I/71x1RHSaEhL._AC_UF894,1000_QL80_.jpg" alt="">
            </div>
            <div class="movie_name">
                HARRY POTTER
            </div>
            
            <div class="ratings">
                IMDB 8/10
            </div>
        </div> 
        <div class="item_1">
            <div class="movie_image">
            <img class="poster" src="https://m.media-amazon.com/images/I/71Jxq2p5YWL._AC_UF894,1000_QL80_.jpg" alt="">
            </div>
            <div class="movie_name">
                JOKER
            </div>
            <div class="ratings">
                IMDB 8/10
            </div>
        </div> 
        <div class="item_1">
            <div class="movie_image">
            <img class="poster" src="https://images.squarespace-cdn.com/content/v1/5a7f41ad8fd4d236a4ad76d0/1669842753281-3T90U1EY5HUNCG43XERJ/A2_Poster_DC_v80_PAYOFF_221029_12trimHD.jpg" alt="">
            </div>
            <div class="movie_name">
                AVATAR
            </div>
            <div class="ratings">
                IMDB 8/10
            </div>
        </div> 
        <div class="item_1">
            <div class="movie_image">
            <img class="poster" src="https://media.comicbook.com/2021/08/dune-movie-1278601.jpeg" alt="">
            </div>
            <div class="movie_name">
                DUNE
            </div>
            <div class="ratings">
                IMDB 8/10
            </div>
        </div> 
        <div class="item_1">
            <div class="movie_image">
            <img class="poster" src="https://media.comicbook.com/2017/10/iron-man-movie-poster-marvel-cinematic-universe-1038878.jpg" alt="">
            </div>
            <div class="movie_name">
                IRON MAN
            </div>
            <div class="ratings">
                IMDB 8/10
            </div>
        </div> 
    </div>
</template>

<style>
.main_div {
    display: flex;
    flex-wrap: wrap;
    max-width: 100vw;
    text-align: center;
    justify-content: center;
    border-radius: 10px;
    padding: 5px;
    color: white;
}
.poster {
    height: 300px;
    width: 200px;
    border-radius: 10px;
    background-size: cover;

}
.item_1 {
    margin: 5px;
    padding: 20px;
    background-color: transparent;
    border-radius: 10px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.item_1:hover {
    cursor: pointer;
    transform: scale(1.06);
    background: rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(7px);
    -webkit-backdrop-filter: blur(7px);
    -webkit-transition: background 3s;
    transition: background 0.9s;
}

.movie_name {
    /* text-align: left; */
    margin: 10px 10px 0px 10px;
    font-weight: bolder;
}

.ratings {
    font-size: small;
    margin-top: 10px;
}
</style>