document.addEventListener('DOMContentLoaded', function() {
    const useCaseContainer = document.querySelector('.use-case-container');

    // Event delegation for form submission
    useCaseContainer.addEventListener('submit', async function(event) {
      if (event.target.tagName === 'FORM') {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);
        const data = {
          use_case_id: formData.get('use_case_id'),
          answers: []
        };
        formData.forEach((value, key) => {
          if (key.startsWith('answer[')) {
            const questionId = key.match(/\[(.*?)\]/)[1];
            data.answers.push({ questionId, answer: value });
          }
        });
        try {
          const response = await fetch('/submit-answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
          });
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          const responseData = await response.json();
          console.log('Response data:', responseData);
          if (responseData.nextUseCase) {
            loadNextUseCase(responseData.nextUseCase);
          } else {
            useCaseContainer.innerHTML = '<p>All use cases completed!</p>';
          }
        } catch (error) {
          console.error('Error:', error);
        }
      }
    });

    function loadNextUseCase(useCase) {
      console.log('Loading next use case:', useCase);
      useCaseContainer.innerHTML = `
        <p id="use-case-description" class="text-lg mb-4">${useCase.description}</p>
        <form id="questions-form" action="/submit-answer" method="post" enctype="application/json">
          <input type="hidden" name="use_case_id" value="${useCase.useCaseId}">
          <div id="questions-container">
            ${generateQuestionHTML(useCase.firstQuestion)}
          </div>
          <button type="submit" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">
            Submit Answer
          </button>
        </form>
      `;
    }

    function generateQuestionHTML(question) {
      if (!question) return '';
      return `
        <div class="mb-6">
          <p class="font-bold mb-2">${question.text}</p>
          ${question.options.map(option => `
            <label class="block mb-2">
              <input type="radio" name="answer[${question.questionId}]" value="${option.id}" class="mr-2">
              ${option.text}
            </label>
          `).join('')}
        </div>
      `;
    }
  });