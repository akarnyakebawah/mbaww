(function($) {

    var result = $('#result');
    var coordinates;
    var canvas = document.getElementById("uploadimage");
    var context = canvas.getContext("2d");

    function processImage(img) {
      $('.image-hide, .text-content-2, .new-download').show();
      $('h2, figure, .attachment-1, .text-content-1').hide();
      $('.images-caman').addClass('images-caman-active');

        canvas.width = img.width;
        canvas.height = img.height;
        context.drawImage(img, 0, 0);
        var imageData = context.getImageData(0, 0,  canvas.width,  canvas.height);
        var px = imageData.data;
        var len = px.length;
        context.putImageData(imageData, 0, 0);

        $('#uploadimage').Jcrop({
          bgOpacity:   .4,
          allowResize: false,
          allowSelect: false,
          setSelect:   [ 0, 0, 800, 800 ],
          aspectRatio: 1,
          onSelect: function (coords) {
            coordinates = coords
          },
          onRelease: function () {
            coordinates = null
          }
        });
    $('#statusedit').hide();
    }

    function displayImage (file, options) {
      currentFile = file
      if (!loadImage(
          file,
          processImage,
          options
        )) {
          alert("Your browser does not support the URL or FileReader API");
        }
    }

    function dropChangeHandler (e) {
      e.preventDefault()
      e = e.originalEvent
      var target = e.dataTransfer || e.target
      var file = target && target.files && target.files[0]
      var options = {
          maxWidth: 800,
          canvas: true,
          pixelRatio: window.devicePixelRatio,
          downsamplingRatio: 0.5
      }
      if (!file) {
          return
      }

      loadImage.parseMetaData(file, function (data) {
          if (data.exif) {
            options.orientation = data.exif.get('Orientation')
          }
          displayImage(file, options)
      })
    }

  $('#attachment').on('change', dropChangeHandler)


  var img2 = loadImage('./assets/images/pigura.png');
  var crop_canvas = document.createElement('canvas');
  crop_canvas.width = 800;
  crop_canvas.height = 800;
  document.getElementById('download').addEventListener('click', function() {
       var ratioY = canvas.height / result.height(),
             ratioX = canvas.width / result.width();
          var getX = coordinates.x * ratioX,
             getY = coordinates.y * ratioY,
             getWidth = coordinates.h * ratioX,
             getHeight = coordinates.w * ratioY;

        crop_canvas.getContext('2d').drawImage(canvas, getX,getY,getWidth,getHeight,0,0,800,800);
        crop_canvas.getContext('2d').drawImage(img2, 0,0,800,800,0,0,800,800);
        crop_canvas.toBlobHD(function(blob) {
            saveAs(blob,"Twiggsy.png");
        }, "image/png");

    }, false);


})(jQuery);
