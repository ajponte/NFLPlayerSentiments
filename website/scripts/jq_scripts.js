$(document).ready(function() {

	$('#team').val($(this).find(":selected").text());
	$('#submit').on('click', function() {
		var team = ($('#teamSelector').val());
		$('#team').text(team + " selected");
	});

});


