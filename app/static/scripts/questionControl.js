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