$(function() {
    $('.location').change(function() {
        var data = $('.location').val();
        
        if(data == "true") {
            
            $( ".location-form" ).append('<div class="form-group form-group-default location-form-input">\
            <input type="text" id="sample6_postcode" placeholder="우편번호">\
            <input type="button" class="from-control" onclick="sample6_execDaumPostcode()" value="우편번호 찾기"><br>\
            <input type="text" id="sample6_address" class="from-control" name="location" placeholder="주소">\
            </div>');
        } else {
            $('.location-form-input').remove();
        }
    });

    $('.category').change(function() {
        var data = $('.category').val();
        location.href="/api/v1/resume/?category="+data;
        console.log(data);
    });

    $('.category-ad').change(function() {
        var data = $('.category-ad').val();
        location.href="/api/v1/ad/?category="+data;
        console.log(data);
    });
});