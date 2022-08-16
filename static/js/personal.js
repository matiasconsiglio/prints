$(document).ready(function(){

	$(".paper").hide();

    $(".size").on('click',function(){

        $(".paper").removeClass('active');
		$(".size").removeClass('active');
		$(this).addClass('active');

		var _size=$(this).attr('product-size');
        

		$(".paper").hide();
		$(".size"+_size).show();
		$(".size"+_size).first().addClass('active');

        var _price=$(".size"+_size).first().attr('product-price');
		$(".product-price-variation").text(_price);
	});

    $(".paper").on('click',function(){
		$(".paper").removeClass('active');
		$(this).addClass('active');

		var _price=$(this).attr('product-price');
		$(".product-price-variation").text(_price);
	})

	$(".size").first().addClass('active');
    var _size=$(".size").first().attr('product-size');
    var _price=$(".paper").first().attr('data-price');
    $('.size'+_size).show();
    $('.size'+_size).first().addClass('active');
    $(".product-price-variation").text(_price);


});
