const isMobile = isMobileDevice();

const imgSubmitButton = document.getElementById('submitImage');
if (imgSubmitButton){
    imgSubmitButton.addEventListener('click', () => {
        /******************for base 64 *****************************/
        var binImage = uploadFile();
        window.location.href = `/game/test?a=${binImage}`;
    });
}

function isMobileDevice() {
    if(/Android|webOS|iPhone|iPad/i.test(navigator.userAgent)) return true;
    else return false
}

if (document.URL == "game/take_picture") {
    const player = document.getElementById('player');
    const canvas = document.getElementById('canvas');
    if (canvas) {const context = canvas.getContext('2d')};
    const captureButton = document.getElementById('capture');
    
    const constraints = {
        video: true,
    }
    
    if (captureButton) {
        captureButton.addEventListener('click', () => {
            // Draw the video frame to the canvas.
            context.drawImage(player, 0, 0, canvas.width, canvas.height);
        });
    }
    
    // Attach the video stream to the video element and autoplay.
    navigator.mediaDevices.getUserMedia(constraints)
    .then((stream) => {
            player.srcObject = stream;
        });
}
    
function getCanvasImage() {
    const canvas = document.getElementById('canvas');
    const img    = canvas.toDataURL('image/png');
    return img
}

function getSelectedImage () {
    var loadimg = document.getElementById('imgsub'),
    img = loadimg.files[0];
    var out = URL.createObjectURL(img);
    // var out = 
    return img
}

function storeImage(img){
    localStorage.imageSubmitted = img;
}

function retrieveImage(){
    return localStorage.imageSubmitted;
}

function showImage(){
    var img = document.createElement('img');
    img.src = localStorage.imageSubmitted;
    document.body.appendChild(img);
}

function uploadFile() {
    var file = getSelectedImage();
    var reader = new FileReader();
    reader.onloadend = function() {
        console.log('Encoded Base 64 File String:', reader.result);
        
        /******************* for Binary ***********************/
        var data=(reader.result).split(',')[1];
        var binaryBlob = atob(data);
        console.log('Encoded Binary File String:', binaryBlob);
        return binaryBlob;
    }
    reader.readAsDataURL(file);
}