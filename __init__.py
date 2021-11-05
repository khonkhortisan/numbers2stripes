from aqt import gui_hooks, mw
numbers2stripes_js="""
	function number2stripes(n) { // █▓▒░
		var thousands=Math.floor(n/1000);
		var hundreds=Math.floor(n/100 % 10);
		var tens=Math.floor(n/10 % 10);
		var ones=Math.floor(n % 10);
		return "█".repeat(thousands)+"▓".repeat(hundreds)+"▒".repeat(tens)+"░".repeat(ones);
	}
	$(".stripecontainer").remove()
	$(".new-count").each(function(){
		$(this).after(" <span class='stripecontainer new-count'    style='font-family: Noto Sans CJK SC;'>"+number2stripes(this.innerText)+"</span>");
	});
	$(".review-count").each(function(){
		$(this).after(" <span class='stripecontainer review-count' style='font-family: Noto Sans CJK SC;'>"+number2stripes(this.innerText)+"</span>");
	});
	$(".learn-count").each(function(){
		$(this).after(" <span class='stripecontainer learn-count'  style='font-family: Noto Sans CJK SC;'>"+number2stripes(this.innerText)+"</span>");
	});
""";
def numbers2stripes_review(card):
	try:
		mw.bottomWeb.eval(numbers2stripes_js);
	except NameError:
		print("numbers2stripes: NameError: name 'mw' is not defined");
def numbers2stripes_overview(overview, *content):
		overview.web.eval(numbers2stripes_js);
def numbers2stripes_deck_browser(deck_browser, *content):
		deck_browser.web.eval(numbers2stripes_js);
gui_hooks.reviewer_did_show_question.append(numbers2stripes_review);
gui_hooks.overview_did_refresh.append(numbers2stripes_overview);
#gui_hooks.deck_browser_did_render(numbers2stripes_deck_browser);
