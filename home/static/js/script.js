
function wishlist(element, event){
    var str = element.id;
    var item = str.substring(4);
    $.ajax({
        dataType:"json",
        url:"/user/wishlist",
        data:{'item':item},
        type:'GET',
        contentType:"text/json; charset=utf-8",
        success:function(data){
                if(data.wishlist.indexOf(item)!=-1)
                {
                    element.lastChild.innerHTML='favorite';
                }
                else
                {
                element.lastChild.innerHTML='favorite_border';
                }
        },
        error:function(xhr,status,thrown){
        }
    });
    return false;
}

function cart(element, event){
    var str = element.id;
    console.log(str);
    var item = str.slice(4);
    console.log(item);
    $.ajax({
        dataType:"json",
        url:"/user/cart",
        data:{'item':item},
        type:'GET',
        contentType:"text/json; charset=utf-8",
        success:function(data){
            $("#cartlength").html(data.length)
            console.log(data.cart);
            console.log(data.length)
            if(data.cart.indexOf(item)!=-1)
            {
                element.lastChild.innerHTML='remove_shopping_cart';
            }
            else
            {
                element.lastChild.innerHTML='shopping_cart';
            }
        },
        error:function(xhr,status,thrown){
        }
    });
    return false;
}

function getVal(item){
    var quantity = item.value;
    var price = $("#price"+item.id.slice(6)).text();
    var total=price*quantity;
    $("#total"+item.id.slice(6)).html(total);
}

function removeFromCart(item){
    var product=document.getElementById("product").value;
    console.log(product);
    $.ajax({
        dataType:"json",
        url:"/user/cart/remove",
        data:{'item':product},
        type:'GET',
        contentType:"text/json; charset=utf-8",
        success:function(data){
            $(this).parent().parent().remove();
             document.location.reload();
        },
        error:function(xhr,status,thrown){
        }
    });

    return false;
}

function removeFromWishlist(item){
    var product=document.getElementById("product").value;
    console.log(product);
    $.ajax({
        dataType:"json",
        url:"/user/wishlist/removelist",
        data:{'item':product},
        type:'GET',
        contentType:"text/json; charset=utf-8",
        success:function(data){
            $(this).parent().parent().remove();
            document.location.reload();
        },
        error:function(xhr,status,thrown){
        }
    });
    document.location.reload();
    return false;
}

$(document).ready(function(){
    $("#new").hide();
    $("#address").click(function(){
        $("#new").show();
    });
    return false;
});

$(document).ready(function(){
     $("#cod").hide();
     $("#netbanking").hide();
      $("#card").hide();
      console.log("hii");
    $('input[type=radio][name=payMethod]').change(function(){
        if(this.value=='cod'){
            $("#cod").show();
            $("#netbanking").hide();
            $("#card").hide();
        }
        else if(this.value=='net'){
            $("#netbanking").show();
             $("#cod").hide();
              $("#card").hide();
        }
        else if(this.value=='card'){
            $("#card").show();
             $("#cod").hide();
            $("#netbanking").hide();
        }
    });
});


function searchItem(query){
    console.log(query);
    $.ajax({
        dataType:"json",
        url:"/product/search",
        data:{'query':query},
        type:'GET',
        contentType:"text/json; charset=utf-8",
        success:function(data){

        },
        error:function(xhr,status,thrown){
        }
    });
    return false;
}
