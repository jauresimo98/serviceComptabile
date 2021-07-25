$(function () {

    /* FUNCTIONS */
    var load_form = function () {
        btn = $(this)
        $.ajax({
            url: btn.attr("data-url"), 
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
            $("#modal-ville").modal("show")
            },
            success: function (data) {
            $("#modal-ville .modal-content").html(data.html_form)
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
              $("#ville-table tbody").html(data.html_ville_list)
              $("#modal-ville").modal("hide")
            }
            else {
              $("#modal-ville .modal-content").html(data.html_form)
            }
          }
        })
        return false
      }

    /* EVENTS */

    //CREATE
    $("#modal-ville").on("submit", ".js-ville-create-form", save_form)
    $(".js-create-ville").click(load_form)

    //UPDATE
    $("#ville-table").on("click", ".js-update-ville", load_form)
    $("#modal-ville").on("submit", ".js-ville-update-form", save_form)

    //DELETE
    $("#ville-table").on("click", ".js-delete-ville", load_form)
    $("#modal-ville").on("submit", ".js-ville-delete-form", save_form)

});