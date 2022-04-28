$(function () {
  button=document.getElementById('btnshowcreated')
 var themodal=document.getElementById('loadMe')
  $(".js-upload-photos").click(function () {
    $("#id_temp_pdf_file").click();
  });

  $("#id_temp_pdf_file").fileupload({
    dataType: 'json',
    sequentialUploads: false,

    start: function (e) {
      $("#loadMe").modal("show");
    },

    stop: function (e) {
      $("#loadMe").modal("hide");
    },    

    done: function (e, data) {
      if (data.result.is_valid) {
        loadtable();
      }else{
        $("#loadMe").modal("hide");
        event.preventDefault();
        event.stopPropagation();
        swal(data.result.msg1,data.result.msg2 , "error");
                    
      }
    }

  });

});
