$(document).ready(function(){


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

	$(".size").first().addClass('active s');
	var _size=$(".size").first().attr('product-size');
	$(".paper").hide();
	$('.size'+_size).show();
    $('.size'+_size).first().addClass('active p');
	var _price=$('.size'+_size).first().attr('product-price');
	$(".product-price-variation").text(_price);
	var _id=$(".size").attr('size-id');
	$(".size-id").val(_id);
	var _id=$(".paper").attr('paper-id');
	$(".paper-id").val(_id);


    $('.btt-link').on('click',function() {
        document.body.scrollTop = 0; 
        document.documentElement.scrollTop = 0; 
    })

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
			success:function(){
				_vm.attr('disabled',false);
				location.reload();
			}
		})


	});


	$(document).on('click','.update-cart',function(){

		var _pId=$(this).attr('data-item');
		var _pQty=$(".new-qty-"+_pId).val();
		var _vm=$(this);
		$.ajax({
			url:'/bag/update-cart',
			data:{
				'update_id':_pId,
				'update_qty':_pQty
			},
			dataType:'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(){
				_vm.attr('disabled',false);
				location.reload();
			}
		});
	});

	$(document).on('click','.delete-cart',function(){
		var _pId=$(this).attr('data-item');
		var _vm=$(this);
		$.ajax({
			url:'/bag/delete-cart',
			data:{
				'delete_id':_pId,
			},
			dataType:'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(){
				_vm.attr('disabled',false);
				location.reload();
			}
		});
	});

    function handleEnableDisable(itemId) {
        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 99;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    var allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        var itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }


    $('.increment-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue + 1);
       var itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });

    $('.decrement-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue - 1);
       var itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });

});

