// import Submission from submission.models;

const isMobile = isMobileDevice();

const imgSubmitButton = document.getElementById('submitImage');
imgSubmitButton.addEventListener('click', () => {
    storeImage(getSelectedImage());
    submit = Submission(submission= retrieveImage());
    submit.save();
    location.href = '/game/test';
});

function isMobileDevice() {
    if(/Android|webOS|iPhone|iPad/i.test(navigator.userAgent)) return true;
    else return false
}

const player = document.getElementById('player');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const captureButton = document.getElementById('capture');

const constraints = {
    video: true,
}

captureButton.addEventListener('click', () => {
    // Draw the video frame to the canvas.
    context.drawImage(player, 0, 0, canvas.width, canvas.height);
});

// Attach the video stream to the video element and autoplay.
navigator.mediaDevices.getUserMedia(constraints)
    .then((stream) => {
        player.srcObject = stream;
    });
    
function getCanvasImage() {
    const canvas = document.getElementById('canvas');
    const img    = canvas.toDataURL('image/png');
    return img
}
function getSelectedImage () {
    var loadimg = document.getElementById('imgsub'),
    img = loadimg.files[0];
    out = URL.createObjectURL(img);
    return out
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