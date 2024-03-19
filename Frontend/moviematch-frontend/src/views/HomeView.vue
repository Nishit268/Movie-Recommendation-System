<template>
  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">
  </head>
  <body>
    <img class="bg" src="../assets/bg.png" alt="">
    <div class="main-div">
      <!-- Header -->
      <div class="header">
        <!-- Logo -->
        <div class="logo">
        <img src="../assets/logo.png" alt="Logo" class="logo-image">
        <span class="website-name">MovieMatch</span>
        </div>
        <!-- Nav links -->
        <div class="navigation">
          <router-link to="/recommendations" class="nav-link">Recommendations</router-link>
          <router-link to="/about" class="nav-link">About</router-link>
        </div>
      </div>
      <!-- Content -->
      <div class="content-holder">
        <!-- searchbar container -->
        <div class="search_bar_container">
          <input type="text" class="search-input" placeholder="Search for recommendations...">
          <button class="search-button">Search</button>
        </div>
        <!-- Recommendation grid -->
        <div class="recommendations_grid">
          <div class="recommendation_grid_title">
            EXPLORE
          </div>
          <div class="item_container">
            <ProductTile />
          </div>
        </div>
      </div>
    </div>

    <!-- FOOTER -->
    <div class="footer">
        <div class="footer-container">
        <div class="logo">
            <img src="../assets/logo.png" alt="Logo" class="logo-image">
            <span class="website-name">MovieMatch</span>
            </div>
        <div class="footer-links">
          <ul>
            <li><a class="footer-nav-links" href="#">Home</a></li>
            <li><a class="footer-nav-links" href="#">About</a></li>
            <li><a class="footer-nav-links" href="#">Recommendations</a></li>
            <li><a class="footer-nav-links" href="#">Contact</a></li>
          </ul>
        </div>
        <div class="footer-social">
          <a href="#"><i class="fab fa-facebook"></i></a>
          <a href="#"><i class="fab fa-twitter"></i></a>
          <a href="#"><i class="fab fa-instagram"></i></a>
        </div>
      </div>
    </div>
  </body>
 

</template>

<script>
import ProductTile from '@/components/ProductTile.vue';
export default {
  name: 'HomeView',
  components: {
    ProductTile,
  }
}
</script>

<style scoped>
*, body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Roboto', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}


.bg {
  z-index: -100;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  position: fixed;
  background-size: cover;
  background-image: url("../assets/bg.png");
  background-repeat: no-repeat;
  border-radius: 0;
}

.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 999;
  background-color: black;
  color: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  /* box-shadow:  rgba(255, 0, 0, 0.4) 0px 2px 20px; */

}

.logo {
  display: flex;
  align-items: center;
  cursor: pointer;
  justify-content: center;
}

.logo-image {
  height: 40px;
  margin-right: 10px;
}

.website-name {
  margin-top: 2px;
  font-size: 40px;
  letter-spacing: 1.2px;
  margin-left: 10px;
  font-family: "Bebas Neue", sans-serif;
  font-weight: 400;
  font-style: normal;
}

.navigation {
  display: flex;
}

.nav-link {
    margin-left: 20px;
    color: #fff;
    text-decoration: none;
    padding: 8px 16px;
    border-radius: 4px; 
    transition: background-color 0.3s; 
    border: solid 1px rgba(255, 255, 255, 0.17); 
}

.nav-link:hover {
    background-color: rgba(219,0,0, 0.80);
}

.content-holder {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 55px;
  padding-top: 100px;
  margin-top: 84px;
}

.search_bar_container {
  background: rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(3.9px);
  -webkit-backdrop-filter: blur(3.9px);
  position: relative;
  border-radius: 10px;
  padding: 50px;
  width: max-content;
  height: max-content;
}

.search-input {
  width: 600px;
  padding: 20px;
  border: none;
  border-radius: 5px;
  margin-right: 10px;
}

.search-button {
  width: 150px;
  padding: 20px;
  background-color: #db0000;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #831010;
}

.recommendations_grid {
  margin-top: 12%;
}

.recommendation_grid_title {
  font-family: 'Roboto';
  font-weight: bolder;
  letter-spacing: 1px;
  font-size: xx-large;
  color: white;
  margin: 20px;
}

.footer {
  height: 150px;
  display: flex;
  align-content: center;
  background: rgba(255, 255, 255, 0.2);
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  color: white;
  bottom:0;
  left: 0;
  right: 0;
  margin: -6.85px;
}

.footer-container {
  padding: 20px;
  width: 100%;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-logo img {
  width: 100px;
}

.footer-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: center; 
}

.footer-links ul li {
  display: inline-block;
  margin-right: 20px;
}

.footer-links ul li a {
  color: #fff;
  text-decoration: none;
}

.footer-social a{
  color: #fff;
  text-decoration: none;
  transition: transform 0.35s ease;
  margin: 10px;
}

.footer-nav-links {
  padding: 10px;
  transition: transform 0.35s ease;
}
.footer-nav-links:hover {
  border-radius: 10px;
  transform: scale(1.5);
  background-color: #db0000a9;
}

.fab {
  padding: 6px;
  transition: transform 0.35s ease;
  margin: 10px;
}

.fab:hover {
  border-radius: 10px;
  transform: scale(1.5);
  background-color: #db0000a9;
}

.footer-bottom {
  background-color: #222;
  padding: 10px 0;
  text-align: center;
}


</style>
