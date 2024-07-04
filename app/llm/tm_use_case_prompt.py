"""
This is a prompt for the LLM to generate use cases for the Investigamer CFA.
"""


prompt = """
Function: GenerateKYCTestScenario

Input Parameters:
1. showAuxiliaryData: boolean (true/false)
2. decisionOutcome: string ("escalate" or "close")
3. difficultyLevel: string ("easy", "medium", "hard")
4. suspiciousPattern: string ("none", "fast-in-fast-out", "large-atm-withdrawals", "high-volume-suspicious-countries")

Constants:
- ATM_WITHDRAWAL_LIMIT: 5000 (in euros)
- SUSPICIOUS_COUNTRIES: [List of countries known for financial risk]

Generate a KYC/TM test scenario for the Dutch financial context based on the following rules and input parameters:

1. Persona Generation:
   [No changes]

2. Financial Profile:
   [No changes]

3. Transaction Data:
   - Generate 6 months of detailed transaction data
   - Include transactions with believable local Dutch merchants
   - Include regular patterns for all expense categories
   - Inject suspicious transactions/patterns based on difficultyLevel and suspiciousPattern:
     * Easy: 1 suspicious activity
     * Medium: 2 suspicious activities
     * Hard: 3-4 suspicious activities or complex patterns
   - If suspiciousPattern is specified, incorporate the following behaviors:
     a. "fast-in-fast-out":
        - Large deposits followed by rapid withdrawals or transfers
        - Minimal time between incoming and outgoing transactions
     b. "large-atm-withdrawals":
        - Multiple ATM withdrawals near the ATM_WITHDRAWAL_LIMIT
        - Withdrawals from different locations in short time periods
     c. "high-volume-suspicious-countries":
        - Frequent transactions with entities in SUSPICIOUS_COUNTRIES
        - Varying transaction amounts to avoid consistent patterns

4. Suspicious Activity:
   - Types: [Large deposit, Unusual withdrawal, Frequent small transactions, International transfer, etc.]
   - Ensure adherence to ATM_WITHDRAWAL_LIMIT for cash withdrawals
   - Amount and frequency should deviate from normal patterns
   - Timing: Distribute within the 6-month period
   - Incorporate the specified suspiciousPattern if provided

5. Context and Explanation:
   - Provide a coherent explanation for the suspicious activity
   - Include relevant Dutch cultural, economic, or regulatory factors
   - Align the explanation with the given decisionOutcome
   - If a suspiciousPattern is specified, include relevant details in the context

6. Analyst Decision:
   - Correct action: Use the provided decisionOutcome
   - Key factors to consider: [List 3-5 critical points, including aspects of the suspiciousPattern if specified]

7. Difficulty Level:
   [No changes]

8. Auxiliary Data (if showAuxiliaryData is true):
   [No changes]

9. Quality Assurance:
   - Ensure all data is realistic and consistent for the Dutch context
   - Verify that suspicious activities align with the given decisionOutcome and suspiciousPattern
   - Confirm that the scenario difficulty matches the provided difficultyLevel
   - Check that all cash withdrawals respect the ATM_WITHDRAWAL_LIMIT
   - If a suspiciousPattern is specified, ensure it is prominently featured in the transaction data

Output Format:
Generate a JSON object containing:
- Persona details
- Financial profile
- 6-month transaction data (always included, with local merchant names)
- Suspicious activity details (including specified suspiciousPattern if any)
- Context and explanation
- Analyst decision criteria
- Difficulty level and score
- Auxiliary data (12-month category averages, if showAuxiliaryData is true)

Ensure all numerical data is formatted consistently (e.g., use of decimal points, thousands separators)
"""
