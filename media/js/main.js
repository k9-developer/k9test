 $(document).ready(function(){
   // Your code here
	// alert("Thanks for visiting!");
	 $('#my_data_ajax_edit').load('/ajax/mydata/edit/');

 });
 
 function mydata_save(){
	 $('#load_msg').text("Save ....");
	 $.post("/ajax/mydata/edit/", $("#my_data_ajax_edit_form").serialize(),
		function(data, textStatus){
		 	if (textStatus == "success"){
		 		$('#my_data_ajax_edit_form').replaceWith(data);
		 		$('#load_msg').text("OK");
		 		$('form#my_data_ajax_edit_form > *').attr("disabled","disabled");
		 		$('form#my_data_ajax_edit_form > * > *').attr("disabled","disabled");
		 	} else {$('#load_msg').text("Save Error !!!");}
		});
 }
