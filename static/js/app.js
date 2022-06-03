const message = document.querySelector('.message');


if (message) {
   setTimeout(() => {
     message.classList.add("message-hide");
   }, 2000);
}
// Load more posts
const results = document.querySelector('.results')
const loadButton = document.querySelector('.load-btn')

async function render() {
  try {
    const res = await fetch('/posts/')
    const data = await res.json()

    if (res.ok) {
      loadButton.style.display = 'none'
    }

    const html = data.map((post) => `<li>${post.title}</li>`).join(' ')

    // for (let i ; i < data.length; i++) {
    //   `<li>${post[i].title}</li>`
    // }
    
    results.insertAdjacentHTML('afterbegin', html)
  } catch (ex) {
    console.log(ex)
  }
}

if (loadButton) {
  loadButton.addEventListener('click', render)
}



// Add To Cart
const cartButtons = Array.from(document.querySelectorAll('.cart-btn'))

function handleProduct() {
  // const id = this.dataset.id;
  // const action = this.dataset.action;
  const { id, action } = this.dataset;
  addToCart(id, action)
}

async function addToCart(id, action) {
  try {
    fetch('/add_to_cart/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({id, action})
    })

    location.reload()
  } catch (error) {
    console.log(error)
  }
}

cartButtons.forEach((button) => button.addEventListener('click', handleProduct))



// Place order
const shippingForm = document.querySelector('.shipping-form');

let shippingData = {}

async function placeOrder(e) {
  e.preventDefault()

  shippingData.city = this.city.value
  shippingData.postcode = this.postcode.value
  shippingData.address = this.address.value
  shippingData.total = +total

  console.log(shippingData)


  try {
    const res = await fetch('/place_order/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify(shippingData)
    })

    const data = await res.json()

    console.log(data)

    const stripe = Stripe(data.stripe_public_key)
    await stripe.redirectToCheckout({ sessionId: data.session_id })
  } catch (error) {
    console.log(error)
  }

}

if (shippingForm) {
  shippingForm.addEventListener('submit', placeOrder)
}
