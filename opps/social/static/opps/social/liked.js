$.get(
  "/api/v1/social/liked/?path="+window.location.pathname,
  function(data){
    obj = data.objects[0];
    like = 0;
    dislike = 0;
    total = 0;
    if(obj){
      like = obj.like;
      dislike = obj.dislike;
      total = obj.total;
    }
    div = $("<div id='opps-social-liked'>")
    div.html("like: "+ like +" | dislike" + dislike)
  }
)
