var button = $('.button');
var mic = button.find('svg');
var active = $('.active-wrapper');
var stop = $('.stop-button');
var dotCol = $('.dots-col');
var w = $(window);
var vw = w.innerWidth();
var vh = w.innerHeight();
var bw = button.innerWidth();
var bh = button.innerHeight();
var s;

var clone = button.clone();
clone.find('svg').remove();
button.before(clone);

var open = function() {
	if (vw > vh) {
		s = vw / bw * 1.5;
	} else {
		s = vh / bh * 1.5;
	}
	var scale = 'scale(' + s + ') translate(-50%,-50%)';
	
	clone.css({
		transform: scale
	});
	
	mic.css({
		fill: 'rgba(0,0,0,0.2)',
		transform: 'scale(4)'
	});
	
	var data = {
		name: 'hoge', 
		age: 'unknown'
	};
	button.on('transitionend', function() {
		active.addClass('active');
		$(this).off('transitionend');
		console.log("click");
		$.ajax({
			type:'POST', 
			url:'/start', 
			data:JSON.stringify(data),  
			contentType:'application/json', 
			dataType: 'json', 
			success:function(data) {
				var result = $.parseJSON( data );
				document.write("This is the score of your song");
			}
		});
	});

//	button.on({
//		'transitionend': function(){
//			active.addClass('active');
//			$(this).off('transitionend');
//		}, 'write': function(){
//			console.log('click');
//		}
//	});
	
	return false;
};

var close = function() {
	active.removeClass('active');
	clone.removeAttr('style');
	mic.removeAttr('style');
};

var write = function(){
	console.log("click");
};

button.on('click',open);
stop.on('click', close);

$('#timerOlympic').yycountdown({
  endDateTime   : '2020/07/24 00:00:00'
});
