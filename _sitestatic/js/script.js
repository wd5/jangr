jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

$("body").on("mouseenter",".news-img",function(e){
	$(".news-img").addClass("opacity-40");
	$(".news-img:hover").each(function(){
		$(this).removeClass("opacity-40").addClass("on-top");
		$(".news-link").parent().removeClass("active");
		$("#news-link-"+$(this).data('number')).parent().addClass("active");
	})
})

$("body").on("mouseleave",".news-img",function(e){
	$(".news-img").removeClass("opacity-40").removeClass("on-top");
})

$("body").on("click",'a[href^="/settings"]',function(e){
	e.preventDefault();
	$("#main").addClass("blur");
	$(".settings").fadeIn(200);
})

$(".settings").on("click",'a.settings-close',function(e){
	e.preventDefault();
	$("#main").removeClass("blur");
	$(".settings").fadeOut(200);
})

$(".settings").on("click","a.open-page",function(e){
	e.preventDefault();
	$(".settings section").fadeOut();
	$(".settings section#settings-"+$(this).data('what')).fadeIn();
}) 	

/*$(".comments").on("mouseenter",".comment",function(e){
	e.stopPropagation()
	$(this).addClass("hovered")
})

$(".comments").on("mouseleave",".comment",function(e){
	$(this).removeClass("hovered")
})*/

function next_news_item() {
	var active = $("#news-list li.active").first();
	var next = active.next();

	if (next.length === 0) next = $("#news-list li").first();
	
	active.removeClass("active");
	next.addClass("active");
}

$(function(){
	setInterval("next_news_item()",4000);
	
	$(".has-tooltip").tooltip();
	
	if ($("html").hasClass("inlinesvg")) {
		
	}
})

$("body").on("click",".fn-vote",function(e){
	e.preventDefault();
	$(this).closest("article").fadeOut()
	$("#feed-thanks").fadeIn()
	$.get(
		"/red/",
		{
			'do':	'feed-vote',
			'id':	$(this).data("id"),
			'vote': $(this).data("vote")
		}
	)
})

tint2 = $(".tint-2")
logo  = $("#logo")
stored_scrolltop = $(window).scrollTop()

setInterval(function(){
	if ($(window).scrollTop() !== stored_scrolltop)
	{
		stored_scrolltop = $(window).scrollTop()
		tint2.css({'background-position':"center "+(-(stored_scrolltop/4))+"px"});
		logo.css({'background-position':"center "+((stored_scrolltop/2.5))+"px"});
	}
},5);