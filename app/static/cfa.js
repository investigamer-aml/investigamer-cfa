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
        <p>${useCase.description}</p>
        <form>
          <input type="hidden" name="use_case_id" value="${useCase.useCaseId}">
          ${generateQuestionHTML(useCase.firstQuestion)}
          <button type="submit" class="button">Submit Answer</button>
        </form>
      `;
    }

    function generateQuestionHTML(question) {
      if (!question) return '';
      return `
        <div>
          <h3>${question.text}</h3>
          ${question.options.map(option => `
            <label>
              <input type="radio" name="answer[${question.questionId}]" value="${option.id}">
              ${option.text}
            </label><br>
          `).join('')}
        </div>
      `;
    }
  });