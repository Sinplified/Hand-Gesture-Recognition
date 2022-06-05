$(document).ready(function () {
  let namespace = "/test";
  let video = document.querySelector("#videoElement");
  let canvas = document.querySelector("#canvasElement");
  let ctx = canvas.getContext('2d');
  // photo = document.getElementById('photo');
  var pos = document.getElementById('output');
  var localMediaStream = null;

  canvas.height = 480;
  canvas.width = 640;


  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

  function sendSnapshot() {
    if (!localMediaStream) {
      return;
    }

    ctx.drawImage(video, 0, 0, video.videoWidth, video.videoHeight, 0, 0, 640, 480);

    ctx.rect(9, 9, 321, 321);
    ctx.strokeStyle = "red";
    ctx.linewidth = 0.5;
    ctx.stroke();

    // let dataURL = canvas.toDataURL('image/jpeg');
    var croppedCan = crop(canvas, {x: 10, y: 10}, {x: 310, y: 310});
    let dataURL = croppedCan.toDataURL('image/jpeg');

    socket.emit('input image', dataURL);

    socket.on('out-image-event', function (data) {
      // photo.setAttribute('src', data.image_data);
      pos.innerHTML =  data.image_data;


    });


  }
  function crop(can, a, b) {
    // get your canvas and a context for it
    var ctx = can.getContext('2d');

    // get the image data you want to keep.
    var imageData = ctx.getImageData(a.x, a.y, b.x, b.y);

    // create a new cavnas same as clipped size and a context
    var newCan = document.createElement('canvas');
    newCan.width = b.x - a.x;
    newCan.height = b.y - a.y;
    var newCtx = newCan.getContext('2d');

    // put the clipped image on the new canvas.
    newCtx.putImageData(imageData, 0, 0);

    return newCan;
  }


  socket.on('connect', function () {
    console.log('Connected!');
  });

  var constraints = {
    video: {
      width: { min: 640 },
      height: { min: 480 }
    }
  };

  navigator.mediaDevices.getUserMedia(constraints).then(function (stream) {
    video.srcObject = stream;
    localMediaStream = stream;

    setInterval(function () {
      sendSnapshot();
    }, 100);
  }).catch(function (error) {
    console.log(error);
  });
});
