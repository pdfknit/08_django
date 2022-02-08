window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        $.ajax({
            url: "/basket/edit/" + event.target.name + "/" + event.target.value + "/",

            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });

        event.preventDefault();
    });
}