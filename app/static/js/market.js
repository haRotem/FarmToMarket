$(document).ready(function() {
    $('#loginForm').submit(function(e) {
        e.preventDefault();
        var username = $('#username').val();
        $.ajax({
            url: "/api/login",
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify({ username: username }),
            success: function(data) {
                sessionStorage.setItem('user_id', data.user_id);
                sessionStorage.setItem('is_farmer', data.is_farmer);
                sessionStorage.setItem('farmerId', data.farmer_id);
                sessionStorage.setItem('is_deliveryman', data.is_deliveryman);
                sessionStorage.setItem('deliverymanId', data.deliveryman_id);
                sessionStorage.setItem('username', username);
                sessionStorage.setItem('region', data.region);

                $('#loginModal').modal('hide');
                updateNavbarForLoggedInUser();
                loadProducts();
            },
            error: function() {
                alert("Login failed. Please check the username.");
            }
        });
    });

    function updateNavbarForLoggedInUser() {
        var username = sessionStorage.getItem('username');
        var isFarmer = sessionStorage.getItem('is_farmer');
        var isDeliveryman = sessionStorage.getItem('is_deliveryman');

        $('#loginButton').addClass('d-none');
        $('#regionSelector').addClass('d-none');
        $('#userDropdown').removeClass('d-none');
        $('#usernameDisplay').text(username);

        var menu = $('#userDropdownMenu');
        menu.empty();

        if (isFarmer === 'true') {
            menu.append('<li><a class="dropdown-item" href="/stock_management">Stock Management</a></li>');
        }
        if (isDeliveryman === 'true') {
            menu.append('<li><a class="dropdown-item" href="/deliveries">Deliveries</a></li>');
        }
        if (isFarmer === 'false' && isDeliveryman === 'false') {
            menu.append('<li><a class="dropdown-item" href="#">My Orders</a></li>');
            $('#shoppingCartIcon').removeClass('d-none');
        }
        menu.append('<li><hr class="dropdown-divider"></li>');
        menu.append('<li><a class="dropdown-item" href="#" id="logout">Logout</a></li>');
    }

    $(document).on('click', '#logout', function() {
        sessionStorage.clear();
        localStorage.clear();
        location.reload();
    });

    $('#regionSelector .dropdown-item').click(function() {
        var selectedRegion = $(this).text();
        sessionStorage.setItem('selectedRegion', selectedRegion);
        loadProducts();
    });

    function loadProducts() {
        var region = sessionStorage.getItem('selectedRegion') || 'Center';
        var user_id = sessionStorage.getItem('user_id');

        if (user_id) {
            region = sessionStorage.getItem('region');
        }

        $.ajax({
            url: '/api/products',
            method: 'GET',
            data: { category: category, region: region },
            success: function(data) {
                var productsContainer = $('#productsContainer');
                productsContainer.empty();

                data.forEach(function(product) {
                    var productCard = `
                        <div class="col mx-auto mb-5" style="max-width: 25rem; min-width: 15rem; max-height: 30rem; min-height: 30rem;">
                            <div class="card" style="height: 100%;">
                                <img src="../static/images/produce/${product.imageName}" class="img-fluid rounded-start" alt="${product.name}" style="height: 70%;">
                                <div class="card-body text-center" style="background-color: #D6DAC8; height: 30%">
                                    <h5 class="card-title">${product.name}</h5>
                                    <p class="card-text">${product.price} nis</p>
                                    <div class="container text-center" style="width: 100%;">
                                        <div class="mx-auto quantity-selector" data-sku="${product.SKU}" data-name="${product.name}" data-price="${product.price}" data-id="${product.id}">
                                            <button class="btn decrement">-</button>
                                            <input type="text" value="0" readonly>
                                            <button class="btn increment">+</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                    productsContainer.append(productCard);
                });

                updateCartDisplay();
            },
            error: function() {
                alert("Failed to load products.");
            }
        });
    }

    function initializeCart() {
        if (!localStorage.getItem('cart')) {
            localStorage.setItem('cart', JSON.stringify([]));
        }
    }

    function updateCart(sku, name, price, id, quantity) {
        let cart = JSON.parse(localStorage.getItem('cart'));
        let productIndex = cart.findIndex(item => item.sku === sku);

        if (productIndex > -1) {
            cart[productIndex].quantity += quantity;
            if (cart[productIndex].quantity <= 0) {
                cart.splice(productIndex, 1);
            }
        } else if(quantity > 0) {
            cart.push({ sku: sku, quantity: quantity, name: name, price: price, id: id });
        }

        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartDisplay();
    }

    function updateCartDisplay() {
        let cart = JSON.parse(localStorage.getItem('cart'));
        $('.quantity-selector').each(function() {
            let sku = $(this).data('sku');
            let product = cart.find(item => item.sku === sku);
            let quantity = product ? product.quantity : 0;
            $(this).find('input').val(quantity);
        });
    }

    $(document).on('click', '.increment', function() {
        if(!sessionStorage.getItem('user_id')) {
            alert('Please login first');
            return;
        }

        let sku = $(this).closest('.quantity-selector').data('sku');
        let name = $(this).closest('.quantity-selector').data('name');
        let price = $(this).closest('.quantity-selector').data('price');
        let id = $(this).closest('.quantity-selector').data('id');
        updateCart(sku, name, price, id, 1);
    });

    $(document).on('click', '.decrement', function() {
        if(!sessionStorage.getItem('user_id')) {
            alert('Please login first');
            return;
        }

        let sku = $(this).closest('.quantity-selector').data('sku');
        let name = $(this).closest('.quantity-selector').data('name');
        let price = $(this).closest('.quantity-selector').data('price');
        let id = $(this).closest('.quantity-selector').data('id');
        updateCart(sku, name, price, id, -1);
    });

    $(document).on('click', '#shoppingCartIcon button', function() {
        populateCartModal();
    });

    function populateCartModal() {
        let cart = JSON.parse(localStorage.getItem('cart'));
        let cartItemsTableBody = $('#cartItemsTableBody');
        cartItemsTableBody.empty();
        let totalOrderPrice = 0;

        if (cart.length === 0) {
            cartItemsTableBody.append('<tr><td colspan="4">Your cart is empty.</td></tr>');
            $('#totalOrderPrice').text('');
            $('#placeOrderButton').hide();
        } else {
            $('#placeOrderButton').show();
            cart.forEach(item => {
                let itemTotalPrice = item.price * item.quantity;
                totalOrderPrice += itemTotalPrice;
                let cartItem = `
                    <tr>
                        <td>${item.name}</td>
                        <td>${item.price} nis</td>
                        <td>${item.quantity}</td>
                        <td>${itemTotalPrice.toFixed(2)} nis</td>
                    </tr>
                `;
                cartItemsTableBody.append(cartItem);
            });
            localStorage.setItem('total_price', totalOrderPrice.toFixed(2));
            $('#totalOrderPrice').text(`Total Order Price: ${totalOrderPrice.toFixed(2)} nis`);
            $('#placeOrderButton').html(`
            <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target='_blank'>
                <input type="hidden" name="business" value="michalshn@mta.ac.il">
                <input type="hidden" name="cmd" value="_xclick">
                <input type="hidden" name="item_name" value="vegetables_order">
                <input type="hidden" name="amount" value="${totalOrderPrice.toFixed(2)}">
                <input type="hidden" name="currency_code" value="ILS">
                <input type="image"  name="submit" border="0" src="https://www.paypalobjects.com/en_US/i/btn/btn_buynow_LG.gif" alt="Buy Now">
                <img alt="" border="0" width="1" height="1" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif">
            </form>
            `);
        }
    }

    $(document).on('click', '#placeOrderButton', function() {
        let cart = JSON.parse(localStorage.getItem('cart'));
        let user_id = sessionStorage.getItem('user_id');
        let totalOrderPrice = localStorage.getItem('total_price');

        $.ajax({
            url: '/place_order',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                user_id: user_id,
                total_price: totalOrderPrice,
                cart_items: cart
            }),
            success: function(response) {
                alert('Order placed successfully!');
                localStorage.setItem('cart', JSON.stringify([]));
                updateCartDisplay();
                $('#cartModal').modal('hide');
            },
            error: function(error) {
                alert('Failed to place order', error);
            }
        });
    });

    // Initial load
    initializeCart();
    loadProducts();
    if (sessionStorage.getItem('user_id')) {
        updateNavbarForLoggedInUser();
    }
});
