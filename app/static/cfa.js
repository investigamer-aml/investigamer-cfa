document.addEventListener('DOMContentLoaded', function() {
    const useCaseContainer = document.querySelector('.use-case-container');
    const totalUseCases = parseInt(document.querySelector('data-total-use-cases'));
    let completedUseCases = parseInt(document.querySelector('data-completed-use-cases'));

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


          if (responseData.isCorrect) {
            completedUseCases++;
            updateProgressBar();
            updateRemainingUseCases();
            displayFeedback(true); // Show success message
          } else {
            displayFeedback(false); // Show error message
          }

          if (responseData.nextUseCase) {
            loadNextUseCase(responseData.nextUseCase);
          } else {
            useCaseContainer.innerHTML = '<p>All use cases completed!</p>';
          }
        } catch (error) {
          console.error('Error:', error);
          displayFeedback(false, error.message); // Show error with message
        }
      }
    });

    function loadNextUseCase(useCase) {
      console.log('Loading next use case:', useCase);

      // Update the use case description
      const description = document.getElementById('use-case-description');
      description.innerHTML = useCase.description;

      // Update the hidden input for use case ID to the new ID
      const useCaseIdInput = document.querySelector('input[name="use_case_id"]');
      useCaseIdInput.value = useCase.useCaseId;

      // Update the questions section with new questions
      const questionsContainer = document.getElementById('questions-container');
      questionsContainer.innerHTML = generateQuestionHTML(useCase.firstQuestion);

      // Update any additional information that depends on the use case, like lesson ID and UseCase ID in the footer
      const lessonInfo = document.querySelector('.text-xs.text-gray-500.text-right.mt-4');
      lessonInfo.textContent = `Lesson ID: ${useCase.lessonId}, UseCase ID: ${useCase.useCaseId}`;
    }

    function updateProgressBar() {
      const progressBar = document.getElementById('progress-bar');
      let progressPercentage = (parseInt(completedUseCases) / totalUseCases) * 100;
      progressBar.style.width = `${progressPercentage}%`;
      progressBar.textContent = `${progressPercentage.toFixed(0)}%`;
    }

    function updateRemainingUseCases() {
      const remainingCount = document.getElementById('remaining-count');
      let remaining = totalUseCases - completedUseCases;
      remainingCount.textContent = remaining;
    }

    function playSound(file) {
      const audio = new Audio(`/static/${file}`);
      audio.play();
    }

    function displayFeedback(isCorrect, message = '') {
      const feedback = document.getElementById('answer-feedback');
      if (isCorrect) {
        feedback.textContent = 'Correct answer!';
        feedback.className = 'bg-green-500 text-center py-2 px-4 rounded text-white';
        playSound('correct.mp3'); // Assuming you have this audio file
      } else {
        feedback.textContent = message || 'Incorrect answer!';
        feedback.className = 'bg-red-500 text-center py-2 px-4 rounded text-white';
        playSound('wrong.mp3'); // Assuming you have this audio file
      }
      feedback.classList.remove('hidden');
      setTimeout(() => feedback.classList.add('hidden'), 3000);
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