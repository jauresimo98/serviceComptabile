$(function () {

    /* FUNCTIONS */
    var load_form = function () {
        btn = $(this)
        $.ajax({
            url: btn.attr("data-url"), 
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
            $("#modal-cannalvente").modal("show")
            },
            success: function (data) {
            $("#modal-cannalvente .modal-content").html(data.html_form)
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
              $("#cannalvente-table tbody").html(data.html_cannalvente_list)
              $("#modal-cannalvente").modal("hide")
            }
            else {
              $("#modal-cannalvente .modal-content").html(data.html_form)
            }
          }
        })
        return false
      }

    /* EVENTS */

    //CREATE
    $("#modal-cannalvente").on("submit", ".js-cannalvente-create-form", save_form)
    $(".js-create-cannalvente").click(load_form)

    //UPDATE
    $("#cannalvente-table").on("click", ".js-update-cannalvente", load_form)
    $("#modal-cannalvente").on("submit", ".js-cannalvente-update-form", save_form)

    //DELETE
    $("#cannalvente-table").on("click", ".js-delete-cannalvente", load_form)
    $("#modal-cannalvente").on("submit", ".js-cannalvente-delete-form", save_form)

});