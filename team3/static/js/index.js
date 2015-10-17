function newloc(){
    var place = document.getElementById("searchloc").value;
    var themap = document.getElementById("googlemap");
    themap.src="https://www.google.com/maps/embed/v1/search?key=AIzaSyApcX1rlj7GBKpbWhvd83CjRWUB9pYzJvc&q=clinics+in+" + place;
    console.log(themap.src);
}