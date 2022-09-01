let basket = [];

let basketDb = JSON.parse(localStorage.getItem("shoes"));

const basketContainer = document.querySelector(".main-basket");

if (basketDb == null) localStorage.setItem("shoes", JSON.stringify([]));

else basket = basketDb;

const allProducts = [

  {id: 1, img: "images/product-1.png", price: 100,o_price:150, title: "Shoes"},


  {id: 2, img: "images/product-2.png", price: 100,o_price:150, title: "Shoes"},


  {id: 3, img: "images/product-3.png", price: 100,o_price:150, title: "Shoes"},


  {id: 4, img: "images/product-4.png", price: 100,o_price:150, title: "Shoes"},


  {id: 5, img: "images/product-5.png", price: 100,o_price:150, title: "Shoes"},


  {id: 6, img: "images/product-6.png", price: 100,o_price:150, title: "Shoes"},



]

const show = (products) => {

  products.forEach(p=>{

    let product = allProducts.find(ap=> ap.id==p)

 

  let div = document.createElement("div");

  div.classList.add("box");

  div.innerHTML = ` 
<img src="${product.img}" alt="" />
<div class="content">
  <h3>${product.title}</h3>
  <div class="price">£${product.price}<span>£${product.o_price}</span></div>
  <div class="stars">
    <i class="fas fa-star"></i>
    <i class="fas fa-star"></i>
    <i class="fas fa-star"></i>
    <i class="fas fa-star"></i>
    <i class="far fa-star"></i>
  </div>
  <a href="#" class="btn">Remove from cart</a>
</div>`;

  basketContainer.appendChild(div);

  let b = div.querySelector(".btn");

  b.addEventListener("click", ()=>{

    basket.splice(basket.splice(basket.indexOf(product.id)), 1)

    localStorage.setItem("shoes", JSON.stringify(basket));

    div.classList.add("removed");

    checkCart();

    setTimeout(() => {

        div.style.width = "0px";

    }, 500);

  })

  });

};

const checkCart = () => {

    // if(basket.length == 0 ) {

    //     basketContainer.innerHTML = `<p>Please add some products in the basket <a href="./index.html">here</a></h3>`

    // }

}

if (document.body.classList.contains("basket-b")) {
console.log(basket);
  if (basket.length > 0) {

    show(basket);

  } else {

    basketContainer.innerHTML = `<p>Please add products to your basket <a href="./index.html">here</a></p>`;

  }

}

else{
 

 

const productHandling = (id) => {
console.log(basket);
  if (basket.includes(id)) {

    basket.splice(basket.indexOf(id), 1);

    localStorage.setItem("shoes", JSON.stringify(basket));

    return true;

  } else {

    basket.push(id);

    localStorage.setItem("shoes", JSON.stringify(basket));

    return false;

  }

};

 let buttons= document.querySelectorAll(".btn");

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