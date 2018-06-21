$( document ).ready(function() {
    console.log( "ready!" );
});

function addingClick(){
  var html = '<div style="height: 100px;" class="alert alert-secondary" role="alert">'+
               '<input id="content" type="text" style="width: 100%;">'+
               '<div class="margintop10">'+
                '<button onclick="submitClick()" type="button" class="btn btn-outline-primary floatright marginleft5">등록</button>'+
               '</div>'+
             '</div>';

   $('.adding-layer').html(html);

}

function checkClick(hello){

  var content = $('#' + hello).text().split("체크")[0].trim();

  var html = '<div class="alert alert-success" role="alert">'+
             content + '(2018.04.01)'+
             '</div>';

  $('.check-layer').prepend(html);
  $('#' + hello).remove()
}

function deleteClick(hello){
  $('#' + hello).remove()
}

function submitClick(){
  var content = $('#content').val()

  var html = '<div style="height: 100px;" class="alert alert-secondary" role="alert">'+
             content +
             '<div class="margintop10">'+
             '<button onclick="checkClick()" type="button" class="btn btn-outline-success floatright marginleft5">체크</button>'+
             '<button onclick="deleteClick()" type="button" class="btn btn-outline-danger floatright">삭제</button>'+
             '</div>'+
             '</div>';

   $('.plus-layer').prepend(html);
   $('.adding-layer').html("");
}
