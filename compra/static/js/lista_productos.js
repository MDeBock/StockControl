let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5] },
        { orderable: false, targets: [0, 5] },
        { searchable: false, targets: [0, 5] }
    ],
    pageLength: 4,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listaProductos();

    dataTable = $("#lista_productos").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listaProductos = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/compra/list_productos/");
        const data = await response.json();

        let content = ``;
        data.productos.forEach((producto, index) => {
            content += `
                <tr>
                    <td>${producto.id}</td>
                    <td>${producto.nombre}</td>
                    <td>${producto.precio}</td>
                    <td>${producto.stock_actual}</td>
                    <td>${producto.proveedor_id}</td>                    
                    <td>
                        <button class='btn btn-sm btn-warning'><i class='fa-solid fa-pencil'></i></button>
                        <button class='btn btn-sm btn-danger'><i class='fa-solid fa-trash-can'></i></button>
                    </td>
                </tr>`;
        });
        tabla_cuerpo.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});