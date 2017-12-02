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
});