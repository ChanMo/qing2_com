/**
 * make input[type="city"] to city selector
 * @author chen
 * @date 2015-12-08
 * @version 1.0
 */

/** get input[type="city"] **/
var city = $("[type='city']");
city.attr("readonly", "readonly");

/** add new input[type="hidden"] **/
var input_name = city.attr("name");
city.removeAttr("name");
city.after("<input id='city_copy' type='hidden'\
 name='"+input_name+"' value=''>");

/** selector **/
var box = '<div id="city_box" data-current="0">\
<span id="city_box_close" onclick="close_city_box()">x</span>\
<h4>City selector</h4>\
<div id="city_content"></div>\
<ul id="city_box_category"><li>省份></li><li>city></li><li>zone></li><li>street</li></ul>\
</div>';
var box_bg = '<div id="city_box_bg" onclick="close_city_box()"></div>';


/** add click event to input[type="city"] **/
city.click(function(){
  $("body").append(box_bg);
  $("body").append(box);
  get_type_city();
});


/*************** set city string *******************/
/** set class(".city_value") to city string **/
var city_value_list = $(".input_city_value");
if(city_value_list.length > 0){
  for(var i=0; i<city_value_list.length; i++){
    set_city_name(city_value_list[i]);
  }
}

/**************** function ************************/
/** close city box event **/
function close_city_box(){
  $("#city_box_bg").remove();
  $("#city_box").remove();
}

/** get city string by city number **/
function set_city_name(item){
  var city_value = $(item).html();
  $.ajax({
    url: 'http://localhost:8000/city/get_display/'+city_value,
    type: 'GET',
    success: function(data){
      if(data.code == 'ok'){
        $(item).html(data.data);
      }
    }
  });
}


/** get city box **/
function get_city(e){
  var url = 'http://localhost:8000/city/'+$(e).data('id');
  var string = '';

  $.ajax({
    url: url,
    type: 'GET',
    dataType: 'json',
    success: function(data){
      if(data.code == 'ok'){
        var city_list = data.data;
        for(var i=0; i<city_list.length; i++){
          string += '<li onclick="get_city(this)" data-id="'+city_list[i].id+'">'+city_list[i].name+'</li>';
        }
        $("#city_content").html(string);
      }
    }
  });
}

function get_type_city(){
  var url = 'http://localhost:8000/city/0';
  var string = '';
  $.ajax({
    url: url,
    type: 'GET',
    dataType: 'json',
    success: function(data){
      if(data.code == 'ok'){
        var city_list = data.data;
        for(var i=0; i<city_list.length; i++){
          string += '<li onclick="get_city(this)" data-string="" data-id="'+city_list[i].id+'">'+city_list[i].name+'</li>';
        }
        $("#city_content").html(string);
      }
    }
  });
}


/** set city value to new input **/
function set_city(e)
{
  var id = $(e).data("id");
  var string = $(e).data("string");
  $("#city_box_bg").remove();
  $("#city_box").remove();

  city.data("id", id);
  city.val(string);
  $("#city_copy").val(id);
}
