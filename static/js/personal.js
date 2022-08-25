$(document).ready(function(){

	$(".paper").hide();

    $(".size").on('click',function(){

        $(".paper").removeClass('active p');
		$(".size").removeClass('active s');
		$(this).addClass('active s');

		var _size=$(this).attr('product-size');
        

		$(".paper").hide();
		$(".size"+_size).show();
		$(".size"+_size).first().addClass('active p');

        var _price=$(".size"+_size).first().attr('product-price');
		$(".product-price-variation").text(_price);
		var _id=$(this).attr('size-id');
		$(".size-id").val(_id);
	});

    $(".paper").on('click',function(){
		$(".paper").removeClass('active p');
		$(this).addClass('active p');

		var _price=$(this).attr('product-price');
		var _id=$(this).attr('paper-id');
		$(".product-price-variation").text(_price);
		$(".paper-id").val(_id);
	})

	var _id=$(".paper").attr('paper-id');
	var _id=$(".size").attr('size-id');
	$(".size-id").val(_id);
	$(".paper-id").val(_id);

	$(".size").first().addClass('active s');
    var _size=$(".size").first().attr('product-size');
    var _price=$(".paper").first().attr('product-price');
    $('.size'+_size).show();
    $('.size'+_size).first().addClass('active p');
    $(".product-price-variation").text(_price);


    $('.btt-link').on('click',function() {
        document.body.scrollTop = 0; 
        document.documentElement.scrollTop = 0; 
    })


	// add to cart
	$(document).on('click', ".add-to-cart", function(){
		var _vm=$(this);
		var _qty=$(".product-qty-").val();
		var _productId=$(".product-id-").val();
		var _productName=$(".product-name-").val();
		var _productSizeId=$(".size-id").val();
		var _productPaperId=$(".paper-id").val();
		var _productSize=$(".s").text();
		var _productPaper=$(".p").text();
		var _productPrice=$(".product-price-variation").text();
		//Ajax
		$.ajax({
			url:'/products/add-to-cart',
			data:{
				'id':_productId,
				'qty':_qty,
				'name':_productName,
				'price':_productPrice,
				'size':_productSize,
				'paper':_productPaper,
				'paper-id':_productPaperId,
				'size-id':_productSizeId
			},
			dataType:'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				$(".cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
			}
		})


	});

});

