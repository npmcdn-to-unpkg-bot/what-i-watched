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
        $(".loading").hide();
        $(".success").show();
        $("#title").val(data.title);
        $("#original_title").val(data.original_title);
        $("#year").val(data.year);
        $("#rating").val(data.rating.average);
        $("#image-preview").attr("src", data.images.large);
        $("#images").val(data.images.large);
        $("#summary").val(data.summary);
    });
});

//detail page
$(document).ready(function() {
    var douban_id = $('#douban_id').val();
    if (douban_id) {
        pullFromDouban(douban_id, function(data) {
            if (data.casts) {
                var casts = '';
                for (var i=0; i<data.casts.length; i++) {
                    if (data.casts[i].avatars) {
                        cast = '<div class="columns large-2 medium-3 small-4">' +
                                    '<img src="' + data.casts[i].avatars.large +  '" />' +
                                '</div>';
                        casts += cast;
                    }
                }
                $('#casts').append(casts);
            }
        });
    }
    
    $('#submit-review').on('click', function() {
        var content = $('#submit-review-content').val();
        $.ajax({
            type: 'POST',
            url: '/visual/ajax_submit_review',
            data: {
                'content' : content,
                'visual_id' : $('#visual_id').val(),
            },
            success: function(res) {
                if (res.status == 'success') {
                    var review = '<div class="media-object">' +
                                    '<div class="media-object-section">' +
                                        '<div class="thumbnail">' +
                                            '<img src="http://dummyimage.com/50x50/000/ffffff.jpg&text=' + res.user + '" />' +
                                        '</div>' +
                                    '</div>' +
                                    '<div class="media-object-section">' +
                                        '<p>' + content + '</p>' +
                                    '</div>' +
                                '</div>';
                    $('#reviews-container').prepend(review);
                }
            }
        });
    });
});
//list page
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