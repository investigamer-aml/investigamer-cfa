# Alembic for db migrations
- alembic revision --autogenerate -m "Add is_admin to Users"
- check the changes in alembic/version/revision_id_name.py
- alembic upgrade head


# Anthropic Suggestod improvements
Great! Since you have already added the `risk_factors` column of type `JSONB` to the `UseCases` model, we can proceed with the implementation.

Here's a detailed implementation guide based on the steps I provided earlier:

1. Modify the `submit_answer` route:
   - After recording the user's answers and checking for correctness, add a condition to check if the user made any mistakes.
   - If the user made a mistake, call the `find_similar_use_case` function (to be implemented) to retrieve a similar use case based on the risk factors.
   - If a similar use case is found, store its ID in the session or a temporary storage to be served after the user completes the current use case.

2. Update the `get_next_use_case` function:
   - Check if there is a similar use case ID stored in the session or temporary storage due to a previous mistake.
   - If a similar use case ID exists, retrieve the corresponding use case from the database and remove the ID from the storage.
   - If there is no similar use case and the user has completed all the use cases in the current lesson, call the `get_next_lesson` function to move on to the next lesson.
   - If there are more use cases in the current lesson, retrieve the next use case based on the user's progress.

3. Modify the `practice.html` template:
   - Add a placeholder element (e.g., a `<div>`) to display the notification when the user is being served a similar use case due to a mistake.
   - Update the template to conditionally display the notification based on a variable passed from the server (e.g., `{% if is_similar_use_case %}`).

4. Update the `record_attempt` function:
   - Modify the function signature to include additional parameters such as the lesson ID and whether the attempt was correct or not.
   - Store the user's progress in the database, including the lesson ID, use case ID, and whether the attempt was correct.

5. Implement the `find_similar_use_case` function:
   - Query the database to find a use case with the same risk factors as the current use case where the user made a mistake.
   - Exclude use cases that the user has already answered correctly by checking the `user_answers` table.
   - Return the ID of the similar use case if found, otherwise return `None`.

6. Modify the `get_next_lesson` function:
   - Query the database to find the next lesson that the user hasn't completed yet based on their progress in the `user_answers` table.
   - Return the lesson details along with its associated use cases.

7. Update the `practice` route:
   - Retrieve the current lesson and use case based on the user's progress.
   - If the user has completed all the use cases in the current lesson, call the `get_next_lesson` function to move on to the next lesson.
   - If there is a similar use case ID stored in the session or temporary storage due to a previous mistake, retrieve that use case and pass it to the template.
   - Otherwise, retrieve the next use case in the current lesson based on the user's progress.
   - Pass a variable to the template indicating whether the current use case is a similar one served due to a mistake.

8. Test the implementation:
   - Verify that when a user makes a mistake, a similar use case is served after they complete the current use case.
   - Ensure that the user's progress is tracked correctly and they move on to the next lesson when they have completed all the use cases in the current lesson.
   - Test different scenarios, such as making multiple mistakes, completing lessons successfully, and navigating through different lessons.


# Loading a new db version
- sudo -u postgres psql
- DROP DATABASE ig_data_admin;
- CREATE DATABASE ig_data_admin;
- sudo -u postgres psql ig_data_admin < investigamer.sql
- psql -h localhost -U postgres -d ig_data_admin
