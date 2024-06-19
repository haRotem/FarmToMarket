$(document).ready(function() {
    $('#usernameDisplay').text(sessionStorage.getItem('username', 'Farmer'));

    $(document).on('click', '#logout', function() {
        sessionStorage.clear();
        localStorage.clear();
        window.location.href = '/';
    });

    function loadItems() {
        $.ajax({
            url: "/api/stock_management/list_items",
            method: "GET",
            beforeSend: function(xhr) {
                var farmerId = sessionStorage.getItem('farmerId');
                xhr.setRequestHeader('farmer-id', farmerId);
            },
            success: function(data) {
                $('#itemList').empty();
                data.items.forEach(item => {
                    $('#itemList').append(
                        `<tr>
                            <td>${item.name}</td>
                            <td>${item.quantity}</td>
                            <td>${item.validity}</td>
                            <td>₪${item.price}</td>
                            <td>${item.category}</td>
                            <td>
                                <span class="icon" onclick="deleteItem(${item.id})">&#128465;</span>
                                <span class="icon" onclick="editItem(${item.id}, '${item.name}', ${item.price}, ${item.quantity}, '${item.validity}')">&#9998;</span>
                            </td>
                        </tr>`
                    );
                });
            }
        });
    }

    function loadProductNames() {
        $.ajax({
            url: "/api/stock_management/list_product_names",
            method: "GET",
            success: function(data) {
                $('#productNames').empty();
                data.productNames.forEach(name => {
                    $('#productNames').append(
                        `<option value="${name}">${name}</option>`
                    );
                });
            }
        });
    }

    $('#itemForm').submit(function(e) {
        e.preventDefault();
        var id = $('#itemId').val();
        var url = "/api/stock_management/add_item";
        var method = "POST";
        if (id) {
            url = `/api/stock_management/update_item/${id}`;
            method = "PUT";
        }
        var itemData = {
            name: $('#itemName').val(),
            price: $('#itemPrice').val(),
            quantity: $('#itemQuantity').val(),
            validity: $('#itemValidity').val(),
        };
        $.ajax({
            url: url,
            method: method,
            contentType: "application/json",
            data: JSON.stringify(itemData),
            beforeSend: function(xhr) {
                var farmerId = sessionStorage.getItem('farmerId');
                xhr.setRequestHeader('farmer-id', farmerId);
            },
            success: function() {
                loadItems();
                $('#itemForm').trigger("reset");
                $('#itemModal').modal('hide');
                $('#itemId').val('');
            }
        });
    });

    window.deleteItem = function(id) {
        $.ajax({
            url: `/api/stock_management/delete_item/${id}`,
            method: "DELETE",
            beforeSend: function(xhr) {
                var farmerId = sessionStorage.getItem('farmerId');
                xhr.setRequestHeader('farmer-id', farmerId);
            },
            success: function() {
                loadItems();
            }
        });
    };

    window.editItem = function(id, name, price, quantity, validity) {
        $('#itemId').val(id);
        $('#itemName').val(name);
        $('#itemPrice').val(price);
        $('#itemQuantity').val(quantity);
        $('#itemValidity').val(validity);
        $('#itemModalLabel').text('Edit Item');
        $('#itemModal').modal('show');
    };

    $('#itemModal').on('shown.bs.modal', function () {
        loadProductNames();
    });

    $('#itemModal').on('hidden.bs.modal', function () {
        $('#itemModalLabel').text('Add New Item');
        $('#itemForm').trigger("reset");
        $('#itemId').val('');
    });

    loadItems();
});
