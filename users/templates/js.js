<script>
$(document).ready(function(){
    $("#myBtn2").click(function(){
        $("#myModal").modal();
    });
});

function login_to_user(){

    var uname = document.getElementById('id_username');
    var pass = document.getElementById('id_pass');


  $.ajax({
              url : /login_user/,
              type : "POST",
              dataType : "json",
              data : {'csrfmiddlewaretoken': '{{ csrf_token }}', 'uname':uname,'pass':pass},

              success : function(data){
                console.log(data.username);

              },
              error : function(data){alert(data.response);}
          });

  }
</script>