$( document ).ready(function() {
    console.log( "movieSubmit!" );
});

function movieSubmit(){

  var movie_name = $('#movie_name').val();
  var movie_subject = $('#movie_subject').val();
  var movie_start = $('#movie_start').val();
  var movie_runtime = $('#movie_runtime').val();
  var movie_contry = $('#movie_contry').val();
  var movie_url = $('#movie_url').val();
  var movie_sumnail = $('.dz-filename').text()

  console.log("movie_name = ", movie_name);
  console.log("movie_subject = ", movie_subject);
  console.log("movie_start = ", movie_start);
  console.log("movie_runtime = ", movie_runtime);
  console.log("movie_contry = ", movie_contry);
  console.log("movie_url = ", movie_url);
  console.log("movie_sumnail = ", movie_sumnail);

  $.post( "/apiMovieCreate", {
    movie_name: movie_name,
    movie_subject: movie_subject,
    movie_start: movie_start,
    movie_runtime: movie_runtime,
    movie_contry: movie_contry,
    movie_url: movie_url,
    movie_sumnail: movie_sumnail,
  })
  .done(function( data ) {
    if(data.return == 'success'){
      alert("success");
    }
    else{
      alert('error');
    }
  });
}
