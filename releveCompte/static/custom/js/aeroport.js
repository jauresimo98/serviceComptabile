$(function () {

    /* FUNCTIONS */
    var load_form = function () {
        btn = $(this)
        $.ajax({
            url: btn.attr("data-url"), 
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
            $("#modal-aeroport").modal("show")
            },
            success: function (data) {
            $("#modal-aeroport .modal-content").html(data.html_form)
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
              $("#aeroport-table tbody").html(data.html_aeroport_list)
              $("#modal-aeroport").modal("hide")
            }
            else {
              $("#modal-aeroport .modal-content").html(data.html_form)
            }
          }
        })
        return false
      }

    /* EVENTS */

    //CREATE
    $("#modal-aeroport").on("submit", ".js-aeroport-create-form", save_form)
    $(".js-create-aeroport").click(load_form)

    //UPDATE
    $("#aeroport-table").on("click", ".js-update-aeroport", load_form)
    $("#modal-aeroport").on("submit", ".js-aeroport-update-form", save_form)

    //DELETE
    $("#aeroport-table").on("click", ".js-delete-aeroport", load_form)
    $("#modal-aeroport").on("submit", ".js-aeroport-delete-form", save_form)

});