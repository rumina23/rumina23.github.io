
 

 

let basket = [];

let basketDb = JSON.parse(localStorage.getItem("starbucks"));

const basketContainer = document.querySelector(".main-basket");

if (basketDb == null) localStorage.setItem("starbucks", JSON.stringify([]));

else basket = basketDb;

const allProducts = [

  {id: 1, img: "img/shop1.png", price: 3.99, title: "StarBucks Coffee"},

  {id: 2, img: "img/shop2.png", price: 4.99, title: "StarBucks Fapuccino"},

  {id: 3, img: "img/shop3.png", price: 4.99, title: "StarBucks cappucino"},

]

const show = (products) => {

  products.forEach(p=>{

    let product = allProducts.find(ap=> ap.id==p)

 

  let div = document.createElement("div");

  div.classList.add("product");

  div.innerHTML = ` <div class="box">

  <div class="box-img">

    <img src="${product.img}" alt="">

  </div>

 

  <div class="stars">

    <i class='bx bxs-star'></i>

    <i class='bx bxs-star'></i>

    <i class='bx bxs-star'></i>

    <i class='bx bxs-star'></i>

    <i class='bx bxs-star-half'></i>

  </div>

  <h2>${product.title}</h2>

  <span class="price">${product.price}</span>

  <a href="#" data-id="${product.id}" class="btn remove">Remove from Basket</a>

</div>`;

  basketContainer.appendChild(div);

  let b = div.querySelector(".remove");

  b.addEventListener("click", ()=>{

    basket.splice(basket.splice(basket.indexOf(product.id)), 1)

    localStorage.setItem("starbucks", JSON.stringify(basket));

    div.classList.add("removed");

    checkCart();

    setTimeout(() => {

        div.style.width = "0px";

    }, 500);

  })

  });

};

const checkCart = () => {

    if(basket.length == 0 ) {

        basketContainer.innerHTML = `<p>Please add some products in the basket <a href="./index.html">here</a></h3>`

    }

}

if (document.body.classList.contains("basket-b")) {

  if (basket.length > 0) {

    show(basket);

  } else {

    basketContainer.innerHTML = `<p>Please add products to your basket <a href="./index.html">here</a></p>`;

  }

}

else{

  let menu = document.querySelector("#menu-icon");

let navbar = document.querySelector(".navbar");

 

menu.onclick = () => {

  menu.classList.toggle("bx-x");

  navbar.classList.toggle("active");

};

window.onscroll = () => {

  menu.classList.remove("bx-x");

  navbar.classList.remove("active");

};

let buttons = document.querySelectorAll(".box .btn");

 

 

const productHandling = (id) => {

  if (basket.includes(id)) {

    basket.splice(basket.indexOf(id), 1);

    localStorage.setItem("starbucks", JSON.stringify(basket));

    return true;

  } else {

    basket.push(id);

    localStorage.setItem("starbucks", JSON.stringify(basket));

    return false;

  }

};

 

buttons.forEach((b) => {

    let id = b.dataset.id;

    if(basket.includes(id)) b.innerText = "Added to Basket";

 

  b.addEventListener("click", e => {

    e.preventDefault();

    let p = productHandling(id);

    if (p) {

      b.textContent = "Order Now";

    } else {

      b.textContent = "Added to Basket";

    }

  });

});

}

