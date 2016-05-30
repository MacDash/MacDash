(function($) {
    $(document).ready(function($) {
         $(".submit-row").hide();
         $("input").prop("disabled", true)
         $('select').prop("disabled", true)
         $('textarea').prop("disabled", true)
         var searchbar = $('#searchbar')
         searchbar.prop("disabled", false)
         searchbar.next().prop("disabled", false)
         $(".actions").hide()
         $(".action-checkbox-column").hide()
         $(".action-checkbox").hide()
    });
})(django.jQuery);