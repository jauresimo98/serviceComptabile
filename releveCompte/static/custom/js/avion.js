$(function () {

    /* FUNCTIONS */
    var load_form = function () {
        btn = $(this)
        $.ajax({
            url: btn.attr("data-url"), 
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
            $("#modal-avion").modal("show")
            },
            success: function (data) {
            $("#modal-avion .modal-content").html(data.html_form)
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
              $("#avion-table tbody").html(data.html_avion_list)
              $("#modal-avion").modal("hide")
            }
            else {
              $("#modal-avion .modal-content").html(data.html_form)
            }
          }
        })
        return false
      }

    /* EVENTS */

    //CREATE
    $("#modal-avion").on("submit", ".js-avion-create-form", save_form)
    $(".js-create-avion").click(load_form)

    //UPDATE
    $("#avion-table").on("click", ".js-update-avion", load_form)
    $("#modal-avion").on("submit", ".js-avion-update-form", save_form)

    //DELETE
    $("#avion-table").on("click", ".js-delete-avion", load_form)
    $("#modal-avion").on("submit", ".js-avion-delete-form", save_form)

});