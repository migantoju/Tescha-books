
$("#id_username").change(function () {
  var form = $(this).closest("form");
  $.ajax({
    url: form.attr("data-validate-username-url"),
    data: form.serialize(),
    dataType: 'json',
    success: function (data) {
      if (data.is_taken) {
        alert(data.error_message);
      }
    }
  });

});

$("#id_email").change(function () {
  var form = $(this).closest("form");
  $.ajax({
    url: form.attr("data-validate-username-url"),
    data: form.serialize(),
    dataType: 'json',
    success: function (data) {
      if (data.is_taken) {
        alert(data.error_message);
      }
    }
  });

});

$("#deleteBook").click(function(){
  var deleteB = $(this).parent()
  if(confirm("¿Estas seguro(a) que deseas eliminar este archivo?")){
    $.ajax({
      type: 'DELETE',
      url: $(this).data('url'),
      beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      },
      success: function() {
        deleteB.fadeOut(1000);
      }
    });
  }
});
