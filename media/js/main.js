$(document).ready(function(){
	$.get('/ajax/mydata/edit/', function(data) {
			$('#my_data_ajax_edit').html(data);
			$(function() {
			    $('input#id_birthday').datepicker({
			        dateFormat: 'yy-mm-dd',
			        changeMonth: true,
			        changeYear: true,
			        yearRange: '1900:2020',
			    });
			});
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
		 	} else {$('#load_msg').text("Error !!!");}
		});
}
