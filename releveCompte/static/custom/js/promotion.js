$(function () {

    /* FUNCTIONS */
    var load_form = function () {
        btn = $(this)
        $.ajax({
            url: btn.attr("data-url"), 
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
            $("#modal-promotion").modal("show")
            },
            success: function (data) {
            $("#modal-promotion .modal-content").html(data.html_form)
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
              $("#promotion-table tbody").html(data.html_promotion_list)
              $("#modal-promotion").modal("hide")
            }
            else {
              $("#modal-promotion .modal-content").html(data.html_form)
            }
          }
        })
        return false
      }

    /* EVENTS */

    //CREATE
    $("#modal-promotion").on("submit", ".js-promotion-create-form", save_form)
    $(".js-create-promotion").click(load_form)

    //UPDATE
    $("#promotion-table").on("click", ".js-update-promotion", load_form)
    $("#modal-promotion").on("submit", ".js-promotion-update-form", save_form)

    //DELETE
    $("#promotion-table").on("click", ".js-delete-promotion", load_form)
    $("#modal-promotion").on("submit", ".js-promotion-delete-form", save_form)

});