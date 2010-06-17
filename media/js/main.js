 $(document).ready(function(){
	 $('#my_data_ajax_edit').load('/ajax/mydata/edit/');
 });
 
 function mydata_save(path){
	 $('#load_msg').text("Save ....");
	 $.post(path, $("#my_data_ajax_edit_form").serialize(),
		function(data, textStatus){
		 	if (textStatus == "success"){
		 		$('#my_data_ajax_edit_form').replaceWith(data);
		 		$('#load_msg').text("OK");
		 		$('form#my_data_ajax_edit_form > *').attr("disabled","disabled");
		 		$('form#my_data_ajax_edit_form > * > *').attr("disabled","disabled");
		 	} else {$('#load_msg').text("Save Error !!!");}
		});
 }
