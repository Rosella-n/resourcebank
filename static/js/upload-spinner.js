$(document).ready(function() {
    $("#just_load_please").on("click", function(e) {
      e.preventDefault();
      $("#loadMe").modal({
        backdrop: "static", //remove ability to close modal with click
        keyboard: false, //remove option to close with keyboard
        show: true //Display loader!
      });
      setTimeout(function() {
        $("#loadMe").modal("hide");
      }, 3500);
    });
    
    });
 
  