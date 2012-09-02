/*!
 * themestrap
 *
 * LOADS MISC JAVASCRIPTS

 */




 // HOME SCRIPTS.



           $(function() {
    $("body").css("display", "none");

    $("body").fadeIn(2000);



});
      $(function() {
    $("#foo2").carouFredSel({
  responsive  : true,
  scroll    : {
    fx      : "crossfade"
  },
  items    : {
    visible    : 1,
    height    : "46%"
  }
});

      });



 // Wookmark Grid JQuery Plugin


 $('#tiles').imagesLoaded(function() {
      // Prepare layout options.
      var options = {
        autoResize: true, // This will auto-update the layout when the browser window is resized.
        container: $('#main'), // Optional, used for some extra CSS styling
        offset: 10, // Optional, the distance between grid items
        itemWidth: 210 // Optional, the width of a grid item
      };

      // Get a reference to your grid items.
      var handler = $('#tiles li');

      // Call the layout function.
      handler.wookmark(options);

      // Capture clicks on grid items.
      handler.click(function(){


        // Update the layout.
        handler.wookmark();
      });
    });








    // PORTFOLIO



 // Fancy Zoom Plugin.

      $(function(){



$.fn.fancyzoom.defaultsOptions.imgDir='assets/img/';

        $('#demo > a:first').fancyzoom({Speed:400,showoverlay:true});
        $('#demo > a:last').fancyzoom({Speed:400,showoverlay:false});
        $('#nooverlay').fancyzoom({Speed:400,showoverlay:false});
        $('img.fancyzoom').fancyzoom();
      });

     



