$(function () {

    /* FUNCTIONS */
    var load_form = function () {
        btn = $(this)
        $.ajax({
            url: btn.attr("data-url"), 
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
            $("#modal-client").modal("show")
            },
            success: function (data) {
            $("#modal-client .modal-content").html(data.html_form)
            }
        })
    }

    var save_form = function () {
        var form = $(this)
        $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          success: function (data) {
            if (data.form_is_valid) {
              $("#client-table tbody").html(data.html_client_list)
              $("#modal-client").modal("hide")
            }
            else {
              $("#modal-client .modal-content").html(data.html_form)
            }
          }
        })
        return false
      }

    /* EVENTS */

    //CREATE
    $("#modal-client").on("submit", ".js-client-create-form", save_form)
    $(".js-create-client").click(load_form)

    //UPDATE
    $("#client-table").on("click", ".js-update-client", load_form)
    $("#modal-client").on("submit", ".js-client-update-form", save_form)

    //DELETE
    $("#client-table").on("click", ".js-delete-client", load_form)
    $("#modal-client").on("submit", ".js-client-delete-form", save_form)

});