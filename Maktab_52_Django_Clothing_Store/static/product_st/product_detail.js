// Cookie

function loadJson(selector) {
    return document.querySelector(selector).getAttribute('data-json');
}

function OnloadProductDetail() {
    const id = loadJson('#jsonData-id');
    console.log(id)
    $('#addToCartBtn').on('click', function () {
        alert('Successfully Added');
        $.post("http://127.0.0.1:8000/product/product_detail/" + id, $('#form').serialize(),
            function () {
                console.log($('#form').serialize());
            },
        )
    });
}


///////////////////////////////////////////////////////////////////////////////////////////
// Local Storage

// function loadJson(selector) {
//     return document.querySelector(selector).getAttribute('data-json');
// }
//
// function appendToStorage(name, data) {
//     let old = localStorage.getItem(name);
//     if (old === null) old = "";
//     localStorage.setItem(name, old + data);
// }
//
// function SaveDataToLocalStorage(data) {
//     let a = [];
//     // Parse the serialized data back into an aray of objects
//     a = JSON.parse(localStorage.getItem('products')) || [];
//     // Push the new data (whether it be an object or anything else) onto the array
//
//     // if (a) {
//     //     console.log('if a')
//     //     for (let i = 0; i < a.length; i++) {
//     //         if (parseInt(a[i]['id']) === parseInt(data['id'])) {
//     //             console.log('Added already')
//     //         } else {
//     //             a.push(data);
//     //         }
//     //     }
//     // } else {
//     //     console.log('else')
//     //     a.push(data);
//     // }
//
//     a.push(data);
//
//     // Alert the array value
//     // alert(a);  // Should be something like [Object array]
//     // Re-serialize the array back into a string and store it in localStorage
//     localStorage.setItem('products', JSON.stringify(a));
// }
//
//
// function OnloadProductDetail() {
//
//     const id = loadJson('#jsonData-id');
//     const name = loadJson('#jsonData-name');
//     const price = loadJson('#jsonData-price');
//     const final_price = loadJson('#jsonData-final-price');
//     const image = loadJson('#jsonData-image');
//     const leftovers = loadJson('#jsonData-leftovers');
//     const qty = 1
//     console.log(id, name, price, final_price, image, leftovers, qty)
//
//     $('#addToCartBtn').on('click', function () {
//             alert('Successfully Added')
//
//             let item = {
//                 'id': id,
//                 'name': name,
//                 'price': price,
//                 'final_price': final_price,
//                 'image': image,
//                 'leftovers': leftovers,
//                 'qty': qty
//             }
//
//             SaveDataToLocalStorage(item)
//             console.log(JSON.parse(localStorage.getItem('products')))
//
//             // if (localStorage.getItem('products')) {
//             //     let products = JSON.parse(localStorage.getItem('products'))
//             //     // console.log(products)
//             //
//             //     const list = []
//             //     for (let i = 0; i < products.length; i++) {
//             //         let x = products[i]['id']
//             //         list.push(parseInt(x))
//             //     }
//             //     console.log(list)
//             //
//             //     if (list.includes(parseInt(id))) {
//             //         console.log(`list contains ${id} so qty++`)
//             //         for (let i = 0; i < products.length; i++) {
//             //             let my_id = products[i]['id']
//             //             if (list.includes(parseInt(my_id))) {
//             //                 let qty = parseInt(products[i]['qty'])
//             //                 // qty = qty+1
//             //                 products[i]['qty'] = qty++
//             //                 console.log(qty)
//             //             }
//             //             console.log(JSON.parse(localStorage.getItem('products')))
//             //
//             //         }
//             //
//             //     } else {
//             //         console.log(`list does not contain ${id} so added to cart`)
//             //
//             //         let new_products = [];
//             //         new_products.push({
//             //             'id': id,
//             //             'name': name,
//             //             'price': price,
//             //             'final_price': final_price,
//             //             'image': image,
//             //             'leftovers': leftovers,
//             //             'qty': qty,
//             //         });
//             //         SaveDataToLocalStorage(JSON.stringify(new_products));
//             //         console.log(JSON.parse(localStorage.getItem('products')))
//             //
//             //     }
//             //
//             // }
//
//             // if (!!!localStorage.getItem('products') || !!!localStorage) {
//             //     let new_products = [];
//             //     new_products.push({
//             //         'id': id,
//             //         'name': name,
//             //         'price': price,
//             //         'final_price': final_price,
//             //         'image': image,
//             //         'leftovers': leftovers,
//             //         'qty': qty,
//             //     });
//             //     localStorage.setItem('products', JSON.stringify(new_products));
//             //
//             //     console.log(localStorage.getItem('products'))
//             //     // console.log(products)
//             // }
//
//         }
//     )
// }
//
///////////////////////////////////////////////////////////////////////////////////////////

