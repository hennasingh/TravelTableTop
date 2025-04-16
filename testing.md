# Travel Table Top - Testing

This page contains all the testing details the website was run through.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org/) to validate all of my HTML files.

| Page | Screenshot | Result |
|------| ---------- | ------ |
| Home | ![landing page](./assets_readme/homeHTML.png) | PASS |
| Products | ![products](./assets_readme/productsHTML.png) | PASS |
| Product Detail |![product detail](./assets_readme/productDetailHTML.png) | PASS |
| Add a Product | ![addProduct](./assets_readme/addProductHTML.png) | PASS |
| Edit a Product | ![EditProduct](./assets_readme/editHTML.png) | PASS |
| Profile | ![profile page](./assets_readme/profileHTML.png) | PASS |
| Bag | ![bag page](./assets_readme/bagHTML.png) | PASS |
| Checkout |![checkout](./assets_readme/checkoutHTML.png) | PASS |
| Checkout Success | ![checkout success](./assets_readme/checkoutSuccessHTML.png) | PASS |
| Contact/FAQ | ![contact and FAQ](./assets_readme/contactHTML.png) | PASS |
| Signup | ![Signup](./assets_readme/signupHTML.png)| PASS |
| Login | ![login](./assets_readme/loginHTML.png) | PASS |
| Logout |![logout](./assets_readme/logoutHTML.png)| PASS |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Screenshot | Result |
| ---- | ---------- | ------ |
| base.css | ![base css](./assets_readme/baseCSS.png)| PASS |
| checkout.css | ![checkout css](./assets_readme/checkoutCSS.png) | PASS |
| profile.css | ![profile css](image.png) | PASS |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com/) to validate all of my JS files.

| File | Screenshot | Result |
| ---- | ---------- | ------ |
| countryfield.js |![country field JS Validate](./assets_readme/countryFieldJSS.png) | PASS |
| stripe_elements.js | ![stripe JS Validate](./assets_readme/stripeJSSValidate.png) | Undefined variable |
| product.js | ![product js validate](./assets_readme/productJSSValidate.png) | PASS |
| bag.js | ![bag js validate](./assets_readme/bagJSValidate.png) | PASS |

### Python

I used VS Code Extension Flake 8 to correct linting errors as and when I worked on my project. For the final test I used command `python -m flake8 --exclude .venv,.vscode,migrations` to test my python files. The auto generated code in ``settings.py`` and code in ``env.py`` was left as is

![python flake 8](./assets_readme/pythonTestResults.png)


## Lighthouse Testing

| Page | Screenshot | Result |
| ---- | ---------- | ------ |
| Home Desktop | ![ lighthouse-home](./assets_readme/homeLighthouse.png) | PASS |
| Home Mobile | ![lighthouse-mobile-home](./assets_readme/homeMobileLH.png) | PASS |
| Products Desktop | ![products-desktop](./assets_readme/products-desktopLH.png) | PASS |
| Products Mobile | ![products-mobile](./assets_readme/products-mobileLH.png) | PASS |
| Profile Desktop | ![profile-LH](./assets_readme/profile-desktopLH.png) | PASS |
| Profile Mobile | ![profile-mobile](./assets_readme/profileMobile-LH.png) | PASS |
| Bag Desktop | ![bag-desktop-lighthouse](./assets_readme/bag-desktopLH.png) | PASS |
| Bag Mobile | ![bag-mobile-lightouse](./assets_readme/bag-mobileLH.png) | PASS |
| Checkout  Desktop | ![ checkout-desktop lighthouse ](./assets_readme/checkout-desktopLH.png)| PASS |
| Checkout Mobile | ![checkout-mobile lighthouse](./assets_readme/checkout-mobileLH.png) | PASS |
| Admin Desktop | ![product management lighthouse](./assets_readme/admin-desktopLH.png) | PASS |
| Admin Mobile | ![add product mobile](./assets_readme/admin-mobileLH.png)  | PASS |

## Stripe 

- Order Created Successfully

![success-order](./assets_readme/successOrderNote.png)

- Stripe webhooks

![stripe webhooks](./assets_readme/stripeWebhooks.png)

- Stripe Events

![stripe events](./assets_readme/stripeEvents.png)
