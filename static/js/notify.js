
    function confirmlogout(){
  var url = $("#logoutUrl").attr("data-url"); 
      swal({
          title: "Sign Out",
          text: "Are You Sure You want To Sign Out And End Your Session?",
          icon: "info",
          buttons: [
            'No',
            'Yes'
          ],
        //   dangerMode: true,
        }).then(function(isConfirm) {
          if (isConfirm) {            
              location.href=url;
              
           
          }
        })
    }
    

  function clearallnotify(userid){
       
      event.preventDefault();   
      $.ajax({
        url:'clearallnotify',
        type: "POST", // or "get"
        data: {user_id:userid},
        headers: {'X-CSRFToken': '{{ csrf_token }}'}, // for csrf token
    
        success:function(){
            location.reload();
        }
          });
    }


    