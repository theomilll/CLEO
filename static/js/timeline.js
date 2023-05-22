var listItems = document.querySelectorAll("#progressbar li");

var currentProgress = 0;

function advanceProgress() {
  if(currentProgress < 3){
    listItems[currentProgress].classList.add("active");
    currentProgress++;
  } else {
    clearInterval(progressInterval);
  }
}

var progressInterval = setInterval(advanceProgress, 2500);
document.getElementById('advance').addEventListener('click', function() {
  if(currentProgress < listItems.length){
    listItems[currentProgress].classList.add("active");
    currentProgress++;
  }
});