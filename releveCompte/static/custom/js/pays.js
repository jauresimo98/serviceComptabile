$(function () {

    /* FUNCTIONS */
    var load_form = function () {
        btn = $(this)
        $.ajax({
            url: btn.attr("data-url"), 
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
            $("#modal-pays").modal("show")
            },
            success: function (data) {
            $("#modal-pays .modal-content").html(data.html_form)
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
              $("#pays-table tbody").html(data.html_pays_list)
              $("#modal-pays").modal("hide")
            }
            else {
              $("#modal-pays .modal-content").html(data.html_form)
            }
          }
        })
        return false
      }

    /* EVENTS */

    //CREATE
    $("#modal-pays").on("submit", ".js-pays-create-form", save_form)
    $(".js-create-pays").click(load_form)

    //UPDATE
    $("#pays-table").on("click", ".js-update-pays", load_form)
    $("#modal-pays").on("submit", ".js-pays-update-form", save_form)

    //DELETE
    $("#pays-table").on("click", ".js-delete-pays", load_form)
    $("#modal-pays").on("submit", ".js-pays-delete-form", save_form)

});