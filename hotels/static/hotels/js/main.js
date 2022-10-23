$(window).load(function () {
    $(".radio_option").change(function () {
        let value = $(this).attr("data-filter");
        let elem = $(".elemys");
        let item = $(".hotelys");
        $(elem).not("." + value).hide();
        $(elem).filter("." + value).css({display:'flex'});
        $(item).not("." + value).hide();
        $(item).filter("." + value).show();
    });
    $(".check_option").change(function () {
        let value = $(this).attr("data-filter");
        let item = $(".hot");
        $(item).not("." + value).hide();
        $(item).filter("." + value).show();
    });
    $('.radio').first().attr('checked', true);
    $('.r_radio').first().prop('checked', true);
})