$(function() {
  $('button').on('click', function(e) {
    e.preventDefault();
    
    var numArray = [];
    
    while( numArray.length < 5 ) {
      var number = Math.floor((Math.random() * 55 ) + 1);
      if( $.inArray( number, numArray ) == -1 ) {
        numArray.push( number );
      }
    }
    numArray.push( Math.floor((Math.random() * 25 ) + 1) );
    $('#meow').html( "<input type='text' value='" + numArray.join("' /> <br/> <input type='text' value='") + "' />" );
  });
});