$(document).ready(function() {
    $('#usernameDisplay').text(sessionStorage.getItem('username', 'Deliveryman'));

    $(document).on('click', '#logout', function() {
        sessionStorage.clear();
        localStorage.clear();
        window.location.href = '/';
    });

    const deliverymanId = sessionStorage.getItem('deliverymanId');

    $.ajax({
        url: '/delivery_routes',
        method: 'GET',
        data: { deliveryman_id: deliverymanId },
        success: function(response) {
            populateRoutesTable(response.routes);
        },
        error: function(error) {
            console.error("Error fetching delivery routes:", error);
        }
    });
});

function populateRoutesTable(routes) {
    const routesTableBody = $('#routes-table tbody');
    routesTableBody.empty();

    routes.forEach((route, index) => {
        const rowId = `orders${index + 1}`;
        let rowHtml = `
            <tr>
                <td style="color: ${route.type === 'pickup' ? 'blue' : 'green'};">${route.name} (${route.type === 'pickup' ? 'Farmer' : 'Customer'})</td>
                <td>
                    <button class="btn btn-link" type="button" data-bs-toggle="collapse" data-bs-target="#${rowId}" aria-expanded="false" aria-controls="${rowId}">
                        <i class="fas fa-plus"></i>
                    </button>
                    <div class="collapse" id="${rowId}">
                        <ul>`;

        for (const [productName, quantity] of Object.entries(route.products)) {
            rowHtml += `<li>${productName} (Quantity: ${quantity})</li>`;
        }

        rowHtml += `</ul></div></td>
                <td><a href="https://www.google.com/maps/dir/?api=1&destination=${route.latitude},${route.longitude}" class="btn btn-primary" target="_blank">Navigate</a></td>
            </tr>
        `;

        routesTableBody.append(rowHtml);
    });
}
