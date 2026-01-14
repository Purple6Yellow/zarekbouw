$(document).ready(function(){
    $('#menulogo').on('click', function(event){
        console.log("drukt op menulogo");
       //alert ('op sandwich logo geklikt')
        event.stopPropagation();
        $('#menuMobiel').slideToggle();
    });

    $('#menuMobiel').click(function(){
        //alert('weer op logo geklikt - om te sluiten')
        $('#menuMobiel').slideUp();
    });

});
