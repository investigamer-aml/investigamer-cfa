document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('NewsArticleModal');
    const btn = document.getElementById('modalButton');
    const span = document.getElementsByClassName("close")[0];

    btn.onclick = function() {
        const useCaseId = document.getElementById('use_case_id').value;
        fetch(`/get-news-article?use_case_id=${useCaseId}`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById('news-article-content').innerHTML = data.content;
                    modal.style.display = "block";
                } else {
                    alert(data.message);
                }
            });
    };

    span.onclick = function() {
        modal.style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };
});