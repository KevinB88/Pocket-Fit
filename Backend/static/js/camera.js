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
