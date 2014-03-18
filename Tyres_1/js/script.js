$(document).ready( function() {

	// Show registration-block
	$("#reg-button").click( function() {
		$("#registration-block").show(300);
	});

	// Hide registration-block when user click on cancel
	$("#hibeBlock").click( function() {
		$("#registration-block").hide(300);
	})

	// Stop hide event when user click on the reg-button
	$("#reg-button").click( function(event) {
		event.stopPropagation();
	})

	// Stop hide event when user click on the form
	$("#registration-block").click( function(event) {
		event.stopPropagation();
	})

	// Hide registration-block when user press escape
	$(document).keydown( function(e) {
		if (e.keyCode == 27) {
 			$("#registration-block").hide(300);
		};
	})

	// Hide registration-block when user click outside the form
	$("body").click( function() {
		$("#registration-block").hide(300);
	})
});