window.onload = function() {
    var text = document.getElementById('moving-text');
    var leftPosition = 0;

    function moveText() {
        leftPosition += 5;
        text.style.left = leftPosition + 'px';

        if (leftPosition > window.innerWidth) {
            leftPosition = -text.offsetWidth;
        }
    }

    setInterval(moveText, 50);
};