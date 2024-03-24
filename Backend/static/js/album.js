// album.js
// album.js
//document.addEventListener('DOMContentLoaded', function() {
//    // Get all elements with the class 'album-image'
//    var albumImages = document.querySelectorAll('.album-image');
//
//    // Add click event listener to each album image
//    albumImages.forEach(function(image) {
//        image.addEventListener('click', function() {
//            // Retrieve the image name from the 'data-image' attribute
//            var imageName = image.getAttribute('data-image');
//
//            // Construct the URL for the full-size image
//            var imageURL = '/images/' + imageName;
//
//            // Open the image in a new window or tab
//            window.open(imageURL, '_blank');
//        });
//    });
//});


document.addEventListener('DOMContentLoaded', function() {
    // Get all elements with the class 'album-image'
    var albumImages = document.querySelectorAll('.album-image');

    // Add click event listener to each album image
    albumImages.forEach(function(image) {
        image.addEventListener('click', function() {
            // Toggle the 'expanded' class on the clicked image
            image.classList.toggle('expanded');
        });
    });
});
