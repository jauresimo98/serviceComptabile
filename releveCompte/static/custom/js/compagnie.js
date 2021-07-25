$(function () {

    /* FUNCTIONS */
    var load_form = function () {
        btn = $(this)
        $.ajax({
            url: btn.attr("data-url"), 
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
            $("#modal-compagnie").modal("show")
            },
            success: function (data) {
            $("#modal-compagnie .modal-content").html(data.html_form)
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
              $("#compagnie-table tbody").html(data.html_compagnie_list)
              $("#modal-compagnie").modal("hide")
            }
            else {
              $("#modal-compagnie .modal-content").html(data.html_form)
            }
          }
        })
        return false
      }

    /* EVENTS */

    //CREATE
    $("#modal-compagnie").on("submit", ".js-compagnie-create-form", save_form)
    $(".js-create-compagnie").click(load_form)

    //UPDATE
    $("#compagnie-table").on("click", ".js-update-compagnie", load_form)
    $("#modal-compagnie").on("submit", ".js-compagnie-update-form", save_form)

    //DELETE
    $("#compagnie-table").on("click", ".js-delete-compagnie", load_form)
    $("#modal-compagnie").on("submit", ".js-compagnie-delete-form", save_form)

});