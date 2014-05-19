$(document).ready(function() {

	$('#team').val($(this).find(":selected").text());
	$('#submit').on('click', function() {
		var team = $('#teamSelector').text($(this).find(":selected").text());
		$('#team').text(team + " selected");
	});

});



