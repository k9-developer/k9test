$(document).ready(function(){
	$.get('/ajax/mydata/edit/', function(data) {
			$('#my_data_ajax_edit').html(data);
			datepicker_bind();
		});
});
 
function mydata_save(path){
	sendData = $("#my_data_ajax_edit_form").serialize()
    $('form#my_data_ajax_edit_form > *').attr("disabled","disabled");
	$('form#my_data_ajax_edit_form > * > *').attr("disabled","disabled");
	$('#load_msg').text("Saving");
	$.post(path, sendData,
		function(data, textStatus){
		 	if (textStatus == "success"){
		 		$('#my_data_ajax_edit_form').replaceWith(data);
		 		$('#load_msg').text("OK");
		 		$('form#my_data_ajax_edit_form > *').removeAttr("disabled");
		 		$('form#my_data_ajax_edit_form > * > *').removeAttr("disabled");
		 		datepicker_bind();
		 	} else {$('#load_msg').text("Error !!!");}
		});
	
};

function datepicker_bind(){
	$(function() {
		currentTime = new Date();
		yearString = '1900:'+ currentTime.getFullYear();
	    $('input#id_birthday').datepicker({
	        dateFormat: 'yy-mm-dd',
	        changeMonth: true,
	        changeYear: true,
	        yearRange: yearString,
	    });
	});
};