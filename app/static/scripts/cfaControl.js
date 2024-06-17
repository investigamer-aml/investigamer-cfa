import { updateProgressBar, updateRemainingUseCases } from './utils.js';
import { generateQuestionHTML } from './questionControl.js';

document.addEventListener('DOMContentLoaded', function() {
    const useCaseContainer = document.querySelector('.use-case-container');
    const useCaseDataElement = document.querySelector('#use-case-data');
    let totalUseCases = parseInt(useCaseDataElement.dataset.totalUseCases, 10);
    let completedUseCases = parseInt(useCaseDataElement.dataset.completedUseCases, 10);

    updateProgressBar(totalUseCases, completedUseCases);
    updateRemainingUseCases(totalUseCases, completedUseCases);

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
                const responseData = await response.json();

                if (response.ok && responseData.isCorrect) {
                    completedUseCases++;
                    updateProgressBar(totalUseCases, completedUseCases);
                    updateRemainingUseCases(totalUseCases, completedUseCases);
                    displayFeedback(true);  // Assuming displayFeedback is defined or refactored similarly
                } else {
                    displayFeedback(false, responseData.message || "Incorrect answer!");
                }

                if (responseData.nextUseCase) {
                    loadNextUseCase(responseData.nextUseCase);  // Assuming loadNextUseCase is defined
                } else {
                    useCaseContainer.innerHTML = '<p>All use cases completed!</p>';
                }
            } catch (error) {
                console.error('Error:', error);
                displayFeedback(false, error.message);
            }
        }
    });

    function displayFeedback(isCorrect, message = '') {
        const feedback = document.getElementById('answer-feedback');
        if (isCorrect) {
            feedback.textContent = 'Correct answer!';
            feedback.className = 'bg-green-500 text-center py-2 px-4 rounded text-white';
            // playSound('sounds/correct.mp3'); Assuming playSound is defined
        } else {
            feedback.textContent = message || 'Incorrect answer!';
            feedback.className = 'bg-red-500 text-center py-2 px-4 rounded text-white';
            // playSound('sounds/wrong.mp3'); Assuming playSound is defined
        }
        feedback.classList.remove('hidden');
        setTimeout(() => feedback.classList.add('hidden'), 3000);
    }

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
    // Define other helper functions like loadNextUseCase and playSound here
});