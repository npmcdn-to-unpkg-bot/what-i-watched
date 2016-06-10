function pullFromDouban(douban_id, callback) {
    var doubanData = "error";
    $.ajax({
        type: "GET", 
        url: "https://api.douban.com/v2/movie/subject/" + $("#douban_id").val(),
        data: {},
        dataType: "jsonp",
        async: false,
        success: function (data) {
            console.log(data);
            $(".loading").hide();
            $(".success").show();
            callback(data);
        }
    });
}

//add && edit page
$("#douban").on("click", function() {
    $(".loading").show();
    var douban_id = $("#douban_id").val();
    if (douban_id == "") {
        alert("no douban id");
        return;
    }
    pullFromDouban(douban_id, function(data) {
        $("#title").val(data.title);
        $("#original_title").val(data.original_title);
        $("#year").val(data.year);
        $("#rating").val(data.rating.average);
        $("#image-preview").attr("src", data.images.large);
        $("#images").val(data.images.large);
        $("#summary").val(data.summary);
    });
});
$(window).load(function() {
    $('.visuals').isotope({
      // set itemSelector so .grid-sizer is not used in layout
      itemSelector: '.visual-wrapper',
      percentPosition: true,
      masonry: {
        // use element for option
        columnWidth: '.visual-sizer'
      }
    })
})