
function shiftSubmit(){
  var shiftSize = $('.shift').length;

  for(var i=1; i<shiftSize+1; i++){
      var post = $('#post' + i).val()

      if(post != ''){
          console.log( post );
          if(post == 'A'){
            $('#post' + i).val('09:00 ~ 18:00');
          }
          else if(post == 'B'){
            $('#post' + i).val('12:15 ~ 21:15');
          }
          else if(post == 'C'){
            $('#post' + i).val('10:00 ~ 19:00');
          }
          else if(post == 'D'){
            $('#post' + i).val('09:00 ~ 18:00');
          }
          else if(post == 'E'){
            $('#post' + i).val('10:00 ~ 20:00');
          }
          else if(post == 'F'){
            $('#post' + i).val('09:00 ~ 20:00');
          }
          else if(post == 'G'){
            $('#post' + i).val('09:00 ~ 21:00');
          }
          else if(post == 'H'){
            $('#post' + i).val('10:00 ~ 21:00');
          }
          else if(post == 'I'){
            $('#post' + i).val('09:00 ~ 18:30');
          }
          else if(post == 'J'){
            $('#post' + i).val('09:00 ~ 19:30');
          }
          else if(post == 'K'){
            $('#post' + i).val('09:00 ~ 20:30');
          }
          else if(post == 'L'){
            $('#post' + i).val('10:00 ~ 20:30');
          }

      }
      else{
          console.log("null");
      }

  }

  //console.log(shiftSize);
}
