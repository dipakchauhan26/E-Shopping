

            function fetchCartFromLocalStorage() {
                if (localStorage.getItem('cart') == null) {
                    return {};
                } else {
                    return JSON.parse(localStorage.getItem('cart'));
                }
            }

            var cart = fetchCartFromLocalStorage();
            updateCart(cart);
            
            $('.divpr').on('click', 'button.cart', function(){
                var idstr = $(this).attr('id');
                console.log(idstr);

                if(cart[idstr] != undefined){
                    qty = cart[idstr][0] + 1;
                } 
                else {
                    qty = 1;
                    name = document.getElementById('name' + idstr).innerHTML;
                    price = document.getElementById('price' + idstr).innerHTML;
                    cart[idstr] = [qty, name, price];
                }
                
                updateCart(cart);
                localStorage.setItem('cart', JSON.stringify(cart));
                document.getElementById('cartcount').innerHTML = Object.keys(cart).length;
                console.log( Object.keys(cart).length);
                document.getElementById("popcart").click();
            });

            $('#popcart').popover();

            updatePopover(cart);

            function updatePopover(cart) {
                    console.log('we are  inside update popover');

                    var popStr = "";
                    var popStr = popStr + "<h5> cart for your items in shopping cart </h5> <div class='mx-2 my-2'>";
                    
                    var i = 1;

                    for (var item in cart) {
                            var element = document.getElementById('name' + item);
                        if(element){    
                            popStr = popStr + "<b>" + i + "</b>. ";
                            popStr = popStr + element.innerHTML.slice(0, 19) + "..." + "<b>" +cart[item][0] + "</b>"+ "Qty"  + '<br>';
                            i = i + 1;
                        }
                    }

                    popStr = popStr + "</div> <a href='/checkout'><button class='btn btn-success mb-3' id='clearCart'>Checkout</button></a>  <button class='btn btn-danger' onclick='clearCart()' id='clearCart'>ClearCart</button>"

                    var popcartElement = document.getElementById('popcart');
                    if (popcartElement) {
                        popcartElement.setAttribute('data-content', popStr);
                        $('#popcart').popover('show');
                        document.getElementById("popcart").click();
                    }
            }

            function clearCart() {
                    cart = JSON.parse(localStorage.getItem('cart'));
                    for (var item in cart) {
                            var element = document.getElementById('div' + item);
                            if (element){
                                element.innerHTML = '<button id="' + item + '" class="btn btn-danger cart btn-sm mt-0">AddToCart <i class="fa-solid fa-cart-shopping"></i></button>' 
                            }
                    }
                    localStorage.clear();
                    cart = {};
                    updateCart(cart);
      
                    
                    var popcartElement = document.getElementById("popcart");
                    if (popcartElement) {
                        popcartElement.click();
                    }
    
            } 
            function updateCart(cart) {
                    var sum = 0;
                    for (var item in cart) {
                            sum = sum + cart[item][0];

                            var element = document.getElementById('div' + item);
                            if (element) {
                            element.innerHTML = "<button id='minus" + item + "'class='btn btn-success minus'>-</button> <span id='val" + item + "''>"  + "<b>" + cart[item][0] + "</b>" + "</span> <button id='plus" + item + "' class='btn btn-success plus'> + </button>";
                            }
                    }
                localStorage.setItem('cart', JSON.stringify(cart));
                document.getElementById('cartcount').innerHTML = sum;
                console.log(cart);
                updatePopover(cart);
                document.getElementById("popcart").click();
            }

            $('.divpr').on("click", "button.minus", function() {

                a = this.id.slice(7, );
                cart['pr' + a][0] = cart['pr' + a][0] - 1;
                cart['pr' + a][0] = Math.max(0, cart['pr' + a][0]);
                document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
                updateCart(cart);
            })
            $('.divpr').on("click", "button.plus", function() {

                a = this.id.slice(6, );
                cart['pr' + a][0] = cart['pr' + a][0] + 1;
                document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
                updateCart(cart);
            })
            
