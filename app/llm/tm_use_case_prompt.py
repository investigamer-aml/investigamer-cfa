"""
This is a prompt for the LLM to generate use cases for the Investigamer CFA.
"""


prompt = """
Function: GenerateTMTestScenario

Input Parameters:
1. showAuxiliaryData: boolean (true/false)
2. decisionOutcome: string ("escalate" or "close")
3. difficultyLevel: string ("easy", "medium", "hard")
4. accountType: string ("retail", "business")
5. suspiciousPattern: string ("fast-in-fast-out", "large-atm-withdrawals", "high-volume-suspicious-countries")

Input Parameter Validation:
  - Validate each input parameter against its allowed values:
    - showAuxiliaryData (boolean): true, false
    - decisionOutcome (string): "escalate", "close"
    - difficultyLevel (string): "easy", "medium", "hard"
    - accountType (string): "retail", "business"
    - suspiciousPattern (string): "fast-in-fast-out", "large-atm-withdrawals", "high-volume-suspicious-countries"

  - If any parameter is invalid:
    - Immediately halt the scenario generation process
    - Return an error message listing all invalid parameters and their allowed values

**Clarify Business Account Types**
When the accountType parameter is set to "business", randomly select one of the following subtypes:
   1. Traditional Business (80% probability)
   2. Freelance/Self-employed (20% probability)

Constants:
- ATM_WITHDRAWAL_ALERT_THRESHOLD: 10000 (in euros, accumulative within a short time)
- SUSPICIOUS_COUNTRIES: [List of countries known for financial risk]
- WELL_KNOWN_INTERNATIONAL_COMPANIES: [List of real, well-known international companies]

Generate a KYC/TM test scenario for the Dutch financial context based on the following rules and input parameters:

1. Persona Generation:
   - Occupation
     - If accountType is "retail": [Generate relevant Dutch job title]
   - If accountType is "business":
      - For Traditional Business: [Generate job title such as "Business Owner", "CEO", "Managing Director"]
      - For Freelance/Self-employed: [Generate job title such as "Freelance Designer", "Self-employed Consultant", "Independent Contractor"]

   - Name: [Generate Dutch first and last name]
   - Age: [25-75]
   - Occupation: [Relevant Dutch job title, matching accountType]
   - Family status: [Single/Married/Divorced/Widowed]
   - Brief background: [3-5 sentences, including randomly determined traits like frequent traveler, young professional, family person, etc.]
   - Previously flagged: [Randomly determine based on difficultyLevel, more likely for higher difficulties]

2. Financial Profile:
   - Monthly income:
     - Retail: [€2,000 - €10,000]
     - Business: [€5,000 - €50,000]
     - Business (freelance/self-employed): [€3,000 - €20,000]

   - Savings balance:
     - Retail: [€1,000 - €100,000]
     - Business: [€10,000 - €500,000]
     - Business (freelance/self-employed): [€5,000 - €250,000]

   - Investment portfolio:
     - Retail:
       - Presence: Yes/No
       - If Yes: [€5,000 - €500,000]
     - Business: [€50,000 - €2,000,000]
     - Business (freelance/self-employed): [€10,000 - €1,000,000]

3. Transaction Data:
   - Generate 6 months of detailed daily transaction data
   - Each transaction should include:
     * Date
     * Description
     * Amount
     * Country (use "Netherlands" for local transactions)
     * Merchant (use specific merchant names)
     * Type ("incoming" or "outgoing")
   - Include transactions with believable local Dutch merchants for day-to-day expenses
   - For retail accounts: Focus on personal expenses (groceries, dining, entertainment, etc.)
   - For business accounts: Include business-related expenses and payments, using real company names
   - If persona is a frequent traveler, include relevant foreign transactions (e.g., restaurants in visited countries)
   - For freelance business accounts: Vary salary amounts and payment intervals
   - Include regular patterns for all relevant expense categories
   - Inject suspicious transactions/patterns based on difficultyLevel and suspiciousPattern:
     * Easy: 2-3 suspicious activity
     * Medium: 3-5 suspicious activities
     * Hard: 5-8 suspicious activities or complex patterns
   - Randomly determine frequency of suspicious activities based on difficultyLevel
   - If suspiciousPattern is specified, incorporate the following behaviors:
     a. "fast-in-fast-out":
        - Large deposits followed by rapid withdrawals or transfers
        - Minimal time between incoming and outgoing transactions
        - Include high incoming payment before cash withdrawals
     b. "large-atm-withdrawals":
        - Multiple ATM withdrawals near or exceeding the ATM_WITHDRAWAL_ALERT_THRESHOLD
        - Withdrawals from different locations in short time periods
     c. "high-volume-suspicious-countries":
        - Frequent transactions with entities in SUSPICIOUS_COUNTRIES
        - Varying transaction amounts to avoid consistent patterns
        - Use real, well-known international company names for these transactions

    - For business accounts:
      - Traditional Business:
        - Include regular, consistent payments from major clients
        - Add business-related expenses (e.g., inventory, payroll, rent) using real company names
        - Use real company names for both incoming and outgoing transactions

      - For freelance/self-employed:
        - Include irregular, project-based incoming payments
        - Mix personal and business expenses
        - Use a combination of individual client names and company names for incoming payments
        - Include business-related expenses (e.g., equipment, software subscriptions, home office)

   3.1. Guidelines for Transaction Frequency and Volume
      - Transaction Frequency and Volume Guidelines:
         a. Retail Accounts:
         - Daily transactions: 0-3 per day
         - Weekly large transactions (e.g., rent, major purchases): 1-2 per week
         - Monthly recurring transactions (e.g., subscriptions, utilities): 2-5 per month
         - Quarterly transactions (e.g., insurance payments): 1-2 per quarter
         - Total transactions per month: 40-80

         b. Business Accounts (Traditional):
         - Daily transactions: 3-8 per day
         - Weekly large transactions (e.g., payroll, inventory purchases): 1-3 per week
         - Monthly recurring transactions (e.g., rent, utilities, subscriptions): 5-10 per month
         - Quarterly transactions (e.g., tax payments, large contract payments): 2-3 per quarter
         - Total transactions per month: 80-160

         c. Business Accounts (Freelance/Self-employed):
         - Daily transactions: 1-4 per day
         - Weekly large transactions (e.g., client payments, major purchases): 1-2 per week
         - Monthly recurring transactions (e.g., subscriptions, utilities): 4-8 per month
         - Quarterly transactions (e.g., tax payments): 1-2 per quarter
         - Total transactions per month: 50-125

      - Transaction Volume Adjustments:
      - Adjust the number of transactions based on the account's financial profile (e.g., higher income/revenue = more transactions)
      - For higher difficulty levels, increase the number of transactions by 10-20%
      - Ensure that the transaction volume aligns with the suspicious activity patterns when applicable

      - Seasonal Variations:
      - Incorporate seasonal variations in transaction frequency and volume:
         - Retail: Increase transactions during holiday seasons (e.g., December)
         - Business: Adjust for industry-specific busy seasons or fiscal year-end activities

      - Weekend vs. Weekday Patterns:
      - Retail: More transactions on weekends, fewer on weekdays
      - Business (Traditional): More transactions on weekdays, fewer on weekends
      - Freelance/Self-employed: More evenly distributed, with slight increase on weekdays

      - Generating Transaction Dates:
      - Distribute transactions across the 6-month period using a weighted random approach
      - Ensure recurring transactions (e.g., rent, subscriptions) occur on consistent dates each month
      - Avoid generating transactions on inappropriate days (e.g., no business transactions on public holidays)

   3.2 Statistical Guidelines for Transaction Data:

      1. Transaction Amount Distributions:
         a. Retail Accounts:
            SMALL_TRANS_RETAIL = {range: [0, 50], percentage: [50, 60]}
            MEDIUM_TRANS_RETAIL = {range: [50, 500], percentage: [30, 40]}
            LARGE_TRANS_RETAIL = {range: [500, Infinity], percentage: [5, 15]}

         b. Business Accounts (Traditional):
            SMALL_TRANS_BUSINESS = {range: [0, 500], percentage: [30, 40]}
            MEDIUM_TRANS_BUSINESS = {range: [500, 5000], percentage: [40, 50]}
            LARGE_TRANS_BUSINESS = {range: [5000, Infinity], percentage: [15, 25]}

         c. Business Accounts (Freelance/Self-employed):
            SMALL_TRANS_FREELANCE = {range: [0, 100], percentage: [40, 50]}
            MEDIUM_TRANS_FREELANCE = {range: [100, 1000], percentage: [35, 45]}
            LARGE_TRANS_FREELANCE = {range: [1000, Infinity], percentage: [10, 20]}

      2. Transaction Type Distribution:
         INCOMING_TRANS_PERCENTAGE = [40, 60]
         OUTGOING_TRANS_PERCENTAGE = [60, 40]

      3. Recurring Transaction Patterns:
         FIXED_RECURRING_RETAIL = {percentage: [5, 10]}
         FIXED_RECURRING_BUSINESS = {percentage: [3, 7]}
         VARIABLE_RECURRING_RETAIL = {percentage: [3, 7]}
         VARIABLE_RECURRING_BUSINESS = {percentage: [2, 5]}

      4. Day of Week Distribution:
         a. Retail Accounts:
            WEEKDAY_TRANS_RETAIL = {percentage: [60, 70]}
            WEEKEND_TRANS_RETAIL = {percentage: [30, 40]}

         b. Business Accounts:
            WEEKDAY_TRANS_BUSINESS = {percentage: [80, 90]}
            WEEKEND_TRANS_BUSINESS = {percentage: [10, 20]}

      5. International Transaction Frequency:
         INTERNATIONAL_TRANS_RETAIL = {percentage: [2, 10]}
         INTERNATIONAL_TRANS_BUSINESS = {percentage: [5, 25]}

      6. Cash Transaction Frequency:
         CASH_TRANS_RETAIL = {percentage: [5, 15]}
         CASH_TRANS_BUSINESS = {percentage: [1, 10]}

      7. Transaction Description Variety:
         MIN_UNIQUE_MERCHANTS_RETAIL = 50
         MIN_UNIQUE_MERCHANTS_BUSINESS = 100

      8. Balance Fluctuations:
         // Ensure balance stays within realistic ranges and shows natural growth/decline

      9. Seasonal Variations:
         SEASONAL_INCREASE = {percentage: [10, 30]}

      10. Correlation with Persona:
         // Ensure transaction patterns align with persona's occupation, age, and background

      Notes:
      - Percentages are represented as ranges [min, max]
      - All monetary values are in euros
      - Adjust ranges as needed to fit specific scenarios and suspicious activity patterns
      - For business accounts, adapt guidelines based on whether it's traditional or freelance/self-employed

   3.3 Incorporating Dutch Cultural Elements:

      To ensure scenarios reflect authentic Dutch cultural and financial practices, incorporate the following elements:

      1. Dutch Holidays and Events:
         - NEW_YEARS_DAY = "January 1"
         - KINGS_DAY = "April 27"
         - LIBERATION_DAY = "May 5"
         - SINTERKLAAS = "December 5"
         - CHRISTMAS = ["December 25", "December 26"]

         Incorporate increased spending patterns around these dates.

      2. Common Dutch Banks:
         - ING_BANK = "ING"
         - RABOBANK = "Rabobank"
         - ABN_AMRO = "ABN AMRO"
         - SNS_BANK = "SNS Bank"
         - REVOLUT = "Revolut Bank"
         - BUNQ = "Bunq"
         - TRIODOS_BANK = "Triodos Bank"

         Use these names in transaction descriptions for transfers between banks.

      3. Popular Dutch Retailers:
         - ALBERT_HEIJN = "Albert Heijn"
         - JUMBO = "Jumbo"
         - HEMA = "HEMA"
         - BOL_COM = "bol.com"
         - COOLBLUE = "Coolblue"
         - MEDIA_MARKT = "Media Markt"
         - ACTION = "Action"
         - LIDL = "Lidl"
         - DIRK = "Dirk"
         - BLOKKER = "Blokker"
         - KRUIDVAT = "Kruidvat"
         - SPAR = "Spar"

         Include these in transaction descriptions for everyday purchases.

      4. Dutch Payment Methods:
         - IDEAL = "iDEAL"
         - PIN_TRANSACTION = "PIN transaction"
         - TIKKIE = "Tikkie"

         Reference these in transaction descriptions for online and in-person payments.

      5. Dutch Financial Practices:
         - DUTCH_VAT = 0.21  // 21% VAT rate
         - MORTGAGE_INTEREST_DEDUCTION = True  // Common tax benefit
         - HEALTH_INSURANCE_MANDATORY = True
         - PENSION_CONTRIBUTION = 0.15  // Typical pension contribution around 15% of salary

         Incorporate these elements in financial profiles and transaction patterns.

      6. Geographic Elements:
         - RANDSTAD = ["Amsterdam", "Rotterdam", "The Hague", "Utrecht"]
         - BORDER_COUNTRIES = ["Germany", "Belgium"]

         Use these for location-based transactions and international transfers.

      7. Dutch Education System:
         - DUTCH_UNIVERSITIES = ["University of Amsterdam", "Utrecht University", "Leiden University", "Delft University of Technology", "Erasmus University Rotterdam", "Vrije Universiteit Amsterdam", "Tilburg University", "Radboud University", "Maastricht University"]
         - STUDENT_FINANCE = "DUO"

         Include for scenarios involving students or education-related transactions.

      8. Transportation:
         - OV_CHIPKAART = "OV-chipkaart"
         - NS_RAILWAYS = "NS"
         - GVB = "GVB"

         Use in transaction descriptions for public transportation expenses.

      9. Housing:
         - RENTAL_PLATFORMS = ["Funda", "Pararius", "Huurwoningen", "Kamernet"]
         - HOUSING_CORPORATIONS = ["Vestia", "Ymere", "Eigen Haard", "Woonstad Rotterdam", "De Key"]

         Reference these in housing-related transactions.

      10. Utility Providers:
         - ENERGY_PROVIDERS = ["Vattenfall", "Eneco", "Essent", "Greenchoice", "Budget Energie"]
         - WATER_COMPANIES = ["Vitens", "Evides", "PWN", "Waternet", "Brabant Water"]

         Use these names for utility bill payments.

      When generating scenarios, weave these elements into transaction descriptions, persona backgrounds, and contextual details to create authentic Dutch financial scenarios.

4. Suspicious Activity:

   - Types: Use the specific suspiciousPattern provided in the input parameter. Possible values are:
     - "fast-in-fast-out": Large deposits followed by rapid withdrawals or transfers
     - "large-atm-withdrawals": Multiple ATM withdrawals near or exceeding the ATM_WITHDRAWAL_ALERT_THRESHOLD
     - "high-volume-suspicious-countries": Frequent transactions with entities in SUSPICIOUS_COUNTRIES

   - For each type, incorporate the following behaviors:
     - "fast-in-fast-out":
       - Large deposits followed by rapid withdrawals or transfers
       - Minimal time between incoming and outgoing transactions
       - Include high incoming payment before cash withdrawals
     - "large-atm-withdrawals":
       - Multiple ATM withdrawals near or exceeding the ATM_WITHDRAWAL_ALERT_THRESHOLD (10,000 euros)
       - Withdrawals from different locations in short time periods
     - "high-volume-suspicious-countries":
       - Frequent transactions with entities in SUSPICIOUS_COUNTRIES
       - Varying transaction amounts to avoid consistent patterns
       - Use real, well-known international company names for these transactions

   - Ensure adherence to ATM_WITHDRAWAL_ALERT_THRESHOLD (10,000 euros accumulative within a short time) for cash withdrawals/deposits
   - Amount and frequency should deviate from normal patterns
   - For large transactions, ensure proportionality to monthly income
   - Timing: Distribute suspicious activities within the 6-month period
   - Number of suspicious transactions/patterns based on difficultyLevel and suspiciousPattern:
      * Easy: 2-3 suspicious activity
      * Medium: 3-5 suspicious activities
      * Hard: 5-8 suspicious activities or complex patterns

   - Randomly determine frequency of suspicious activities based on difficultyLevel
   - For cash withdrawals, consider travel patterns in the persona's background
   - For cash deposits, treat as more suspicious than withdrawals

   Additional considerations:
   - Ensure that the suspicious activity aligns with the account type (retail or business)
   - For business accounts, especially freelance/self-employed, adjust patterns to fit with expected business operations
   - Consider the persona's background story when crafting suspicious activities
   - For higher difficulty levels, combine multiple suspicious elements or create more subtle patterns

5. Context and Explanation:
   - Provide a coherent explanation for the suspicious activity
   - Include relevant Dutch cultural, economic, or regulatory factors
   - Align the explanation with the given decisionOutcome
   - Include details relevant to the specified suspiciousPattern
   - For easy difficulty, make the pattern more obvious in the explanation
   - For higher difficulties, introduce more complexity and potential mitigating factors in the explanation
   - Incorporate the persona's background story into the explanation

6. Analyst Decision:
   - Correct action: Use the provided decisionOutcome
   - Key factors to consider: [List 1-5 non-repetitive, critical points, including aspects of the suspiciousPattern if specified]
   - For easy difficulty, make the decision factors more straightforward
   - For hard difficulty, ensure the factors reflect the intricacy of the situation and include potential mitigating circumstances

7. Difficulty Level:
   - Use the provided difficultyLevel
   - Assign a score: Easy (1-3), Medium (4-7), Hard (8-10)
   - For hard difficulty, ensure patterns are complex and not immediately obvious

   7.1. Difficulty Level Scoring:
      - Easy (1-3):
      - Score 1: Very obvious suspicious pattern, minimal transaction complexity
      - Score 2: Clear suspicious pattern, slight increase in transaction volume
      - Score 3: Noticeable suspicious pattern, introduction of minor complexities
      - Medium (4-7):
      - Score 4: Suspicious pattern requires some analysis, increased transaction volume
      - Score 5: Pattern is less obvious, requires correlation between multiple transactions
      - Score 6: Introduction of potential mitigating factors, higher complexity in transaction patterns
      - Score 7: Multiple subtle instances of suspicious pattern, requires thorough investigation
      - Hard (8-10):
      - Score 8: Complex implementation of suspicious pattern, high volume of transactions
      - Score 9: Very subtle pattern implementation, potential legitimate explanations present
      - Score 10: Extremely complex scenario, multiple intertwined patterns, highest level of analysis required

      - Scoring Guidelines:
         1. Base Score: Start with the middle score of the difficulty level (Easy: 2, Medium: 5, Hard: 9)
         2. Adjust based on:
            - Number of suspicious transactions (+1 for more, -1 for fewer)
            - Complexity of the pattern implementation (+1 for more complex, -1 for simpler)
            - Presence of mitigating factors or potential legitimate explanations (+1 if present)
            - Volume and complexity of overall transactions (+1 for higher, -1 for lower)
         3. Ensure the final score remains within the range for the chosen difficulty level

      - Usage in Scenario Generation:
      - Use the score to fine-tune the complexity of the generated scenario
      - Higher scores within each difficulty level should correspond to:
         - More sophisticated implementation of the suspicious pattern
         - Increased overall transaction volume and complexity
         - More nuanced context and potential explanations
         - More challenging analyst decision factors

8. Auxiliary Data (if showAuxiliaryData is true):
   Include 6-month averages for the following categories:
   - Daily expenses (groceries, dining out)
   - Housing (rent/mortgage, utilities)
   - Transportation
   - Healthcare
   - Entertainment
   - Savings/Investments
   - International transfers
   - Cash withdrawals/deposits

   8.1. Calculating 6-Month Averages for Auxiliary Data
      - Calculating Auxiliary Data Averages:
         - For each category, use the following methods to calculate the 6-month averages:
         a. Daily Expenses (groceries, dining out):
            - Sum all transactions labeled as groceries or dining out over 6 months
            - Divide the sum by 180 (average days in 6 months)

         b. Housing (rent/mortgage, utilities):
            - Sum all housing-related expenses over 6 months
            - Divide by 6 to get the monthly average

         c. Transportation:
            - Sum all transportation-related expenses (fuel, public transport, car payments) over 6 months
            - Divide by 6 to get the monthly average

         d. Healthcare:
            - Sum all healthcare-related expenses over 6 months
            - Divide by 6 to get the monthly average

         e. Entertainment:
            - Sum all entertainment-related expenses over 6 months
            - Divide by 6 to get the monthly average

         f. Savings/Investments:
            - Calculate the net increase in savings and investment accounts over 6 months
            - Divide by 6 to get the monthly average

         g. International Transfers:
            - Sum the absolute value of all international transfers (both incoming and outgoing) over 6 months
            - Divide by 6 to get the monthly average

         h. Cash Withdrawals/Deposits:
            - Sum the absolute value of all cash withdrawals and deposits over 6 months
            - Divide by 6 to get the monthly average

      - General Formula:
      - Monthly Average = (Sum of all relevant transactions over 6 months) / 6
      - Notes:
      - Ensure that the averages are consistent with the persona's financial profile and transaction patterns
      - For business accounts, adjust the calculations to reflect business-specific patterns (e.g., higher transaction volumes, regular large payments)
      - For categories with irregular expenses (like healthcare or international transfers), consider using a weighted average that accounts for months with unusually high or low activity

9. Quality Assurance:
   - Ensure all data is realistic and consistent for the Dutch context
   - Verify that suspicious activities align with the given decisionOutcome and suspiciousPattern
   - Confirm that the scenario difficulty matches the provided difficultyLevel
   - Check that cash withdrawals/deposits respect the ATM_WITHDRAWAL_ALERT_THRESHOLD
   - If a suspiciousPattern is specified, ensure it is prominently featured in the transaction data
   - Verify that the transaction data feels realistic, mimicking a real bank app's level of detail
   - For business accounts, ensure the use of real, well-known international company names where appropriate
   - Ensure that freelance and self-employed individuals are correctly classified as business accounts
   - For freelance/self-employed business accounts, verify that the transaction patterns reflect the irregular nature of project-based income and expenses
   - Check that the financial profile and transaction data are consistent with the specific type of business account (traditional business vs. freelance/self-employed)

Note: When the accountType parameter is set to "business", the scenario generator should randomly decide whether it's a traditional business or a freelance/self-employed individual, and adjust the financial profile and transaction patterns accordingly.


**Output Format:**

More information about the output format. Belowe you will find the
1. Persona details (including background story and previous flagging status)
  - name: Full name of the generated persona (string)
  - age: Age of the persona (number)
  - occupation: Job title or profession of the persona (string)
  - familyStatus: Marital/family status (string: "Single", "Married", "Divorced", or "Widowed")
  - background: Brief background story of the persona (string)
  - previouslyFlagged: Whether the persona has been flagged in the past (boolean)

2. Financial profile
  - monthlyIncome: Average monthly income in euros (number)
  - savingsBalance: Current savings account balance in euros (number)
  - investmentPortfolio:
    - hasInvestments: Whether the persona has investments (boolean)
    - investmentAmount: Total value of investments in euros (number, null if hasInvestments is false)

3. transactionData: 6-month transaction data (array of objects)
  - Each transaction contains:
    - date: Date of the transaction (string in "YYYY-MM-DD" format)
    - description: Brief description of the transaction (string)
    - amount: Transaction amount in euros (number, positive for incoming, negative for outgoing)
    - country: Country where the transaction occurred (string)
    - merchant: Name of the merchant or counterparty (string)
    - type: Whether the transaction is incoming or outgoing (string: "incoming" or "outgoing")

4. suspiciousActivity: Suspicious activity details
  - types: Array of suspicious activity types present in the scenario (array of strings)
  - timing: Array of time periods when suspicious activities occurred (array of strings)
  - amounts: Array of amounts involved in suspicious activities (array of numbers)
  - pattern: The specific suspicious pattern used in this scenario (string)
  - frequencies: Array of frequencies for each type of suspicious activity (array of numbers)

5. Detailed explanation of the scenario, including the suspicious activities and their context (string)

6. analystDecision: Analyst decision criteria
   - action: The correct decision for this scenario (string: "escalate" or "close")
   - keyFactors: Array of critical points to consider in making the decision (array of strings, non-repetitive and appropriately complex)

7. difficultyLevel: Difficulty level and score
   - level: The overall difficulty level of the scenario (string: "easy", "medium", or "hard")
   - score: Numeric score representing the specific difficulty within the level (number: 1-10)

8. auxiliaryData: Auxiliary data (only included if showAuxiliaryData is true) 6-month category averages:
   - dailyExpenses: Monthly average of daily expenses in euros (number)
   - housing: Monthly average of housing-related expenses in euros (number)
   - transportation: Monthly average of transportation expenses in euros (number)
   - healthcare: Monthly average of healthcare expenses in euros (number)
   - entertainment: Monthly average of entertainment expenses in euros (number)
   - savingsInvestments: Monthly average of savings and investments in euros (number)
   - internationalTransfers: Monthly average of international transfers in euros (number)
   - cashWithdrawalsDeposits: Monthly average of cash withdrawals and deposits in euros (number)

Generate a JSON object containing the following structure. All fields must be present, even if some are null or empty arrays:

{
  "persona": {
    "name": "string",
    "age": "number",
    "occupation": "string",
    "familyStatus": "string",
    "background": "string",
    "previouslyFlagged": "boolean"
  },
  "financialProfile": {
    "monthlyIncome": "number",
    "savingsBalance": "number",
    "investmentPortfolio": {
      "hasInvestments": "boolean",
      "investmentAmount": "number"
    }
  },
  "transactionData": [
    {
      "date": "string (YYYY-MM-DD)",
      "description": "string",
      "amount": "number",
      "country": "string",
      "merchant": "string",
      "type": "string (incoming or outgoing)"
    }
  ],
  "suspiciousActivity": {
    "types": ["string"], // List of suspicious activity types based on the given suspiciousPattern
    "timing": ["string"], // List of time periods when suspicious activities occurred
    "amounts": ["number"], // List of amounts involved in suspicious activities
    "pattern": "string", // The specific suspiciousPattern provided in the input
    "frequencies": ["number"] // List of frequencies for each type of suspicious activity
  },
  "context": "string",
  "analystDecision": {
    "action": "string (escalate or close)",
    "keyFactors": ["string"]
  },
  "difficultyLevel": {
    "level": "string (easy, medium, hard)",
    "score": "number (1-10)"
  },
  "auxiliaryData": {
    "dailyExpenses": "number (monthly average)",
    "housing": "number (monthly average)",
    "transportation": "number (monthly average)",
    "healthcare": "number (monthly average)",
    "entertainment": "number (monthly average)",
    "savingsInvestments": "number (monthly average)",
    "internationalTransfers": "number (monthly average)",
    "cashWithdrawalsDeposits": "number (monthly average)"
  }
}

Error Output Format JSON:

{
  "error": "Invalid input parameters",
  "invalidParameters": [
    {
      "parameter": "string (name of the invalid parameter)",
      "providedValue": "string or boolean (the invalid value provided)",
      "allowedValues": ["array of allowed values for this parameter"]
    }
  ]
}

Ensure all numerical data is formatted consistently (e.g., use of decimal points, thousands separators)


GenerateKYCTestScenario(
"showAuxiliaryData": "true",
"decisionOutcome: "escalate",
"difficultyLevel": "medium",
"accountType": "retail",
"suspiciousPattern": "high-volume-suspicious-countries")
"""
