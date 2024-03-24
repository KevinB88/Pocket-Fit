// camera.js
document.getElementById('activateButton').onclick = function() {
    var videoFeed = document.getElementById('videoFeed');
    videoFeed.style.display = "block";  // Show the video feed
    document.getElementById('snapshotBtn').style.display = "inline";
    this.style.display = "none";  // Hide the activate button
};

document.getElementById('snapshotBtn').onclick = function(){
    fetch ('/take_snapshot', {method: 'POST'})
        .then(response => {
            if(response.ok){
                return response.text();
            }
            throw new Error('Request failed.');
        })
        .then(data => alert("Snapshot taken!"))
        .catch(error => console.error(error));
};

document.getElementById('loadImagesButton').addEventListener('click', function(){
    fetch('/get-images')
        .then(response => response.json())
        .then(images => {
            const container = document.getElementById('imageContainer');
            container.innerHTML = '';
            images.forEach(img => {
                const imgElement = document.createElement('img');
                imgElement.src = `/images/${img}`;
                imgElement.style.width = '100px';
                imgElement.style.cursor = 'pointer';
                imgElement.onclick = function(){
                    document.getElementById('modalContent').src = imgElement.src;
                    document.getElementById('imageModal').style.display = 'block';
                };
                container.appendChild(imgElement);
            });
        })
        .catch(error => console.error('Error loading images:', error));

        document.getElementById('closeModal').onclick = function(){
            document.getElementById('imageModal').style.display = 'none';
        };
});
