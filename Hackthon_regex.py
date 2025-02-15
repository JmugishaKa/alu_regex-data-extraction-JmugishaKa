//Importing re module to help us with matching regular expresions.

import re

def extract_info(text):
 //Regex to match phone number,credit cards, hashtags and currency amounts.

    phone_num_reg = r'\(?([0-9]){3}\)?[\s.-]?([0-9]){3}(\.|-)([0-9]){4}'

    credit_reg = r'\b([0-9]{4}(\s|-)){3}([0-9]){4}\b'
 
    hashtag_reg = r'#\w+'
 
    currency_reg = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'


 // Extracting all matches for each type of info.
    phone_numbers = re.findall(phone_num_reg, text)
    credit_cards = re.findall(credit_reg, text)
    hashtags = re.findall(hashtag_reg, text)
    currencies = re.findall(currency_reg, text)

// Return the values in a dictionary with the matches
    return {
        'phone_numbers': [f"({phone[0]}) {phone[1]}-{phone[3]}" for phone in phone_numbers],
        'credit_cards': credit_cards
	'hashtags': hashtags,
        'currencies': currencies
    }

// Our sample text
input_data= '''
Phone numbers (various formats):
(123) 456-7890
123-456-7890
123.456.7890
1234567890
123-45-7890
Credit card numbers:
1234 5678 9012 3456
1234-5678-9012-3456
1234567890123456
1234_5678_9012_3456
1234-5678-9012
Hashtags:
#example
#ThisIsAHashtag
Currency amounts
$19.99
$1,234.56
'''

// Invoking the function to then print the results
result = extract_info(input_data)

print('Phone Numbers:', result['phone_numbers'] if result['phone_numbers'] else 'No phone numbers found')
print('Credit Card Numbers:', result['credit_cards'] if result['credit_cards'] else 'No credit card numbers found')
print('Hashtags:', result['hashtags'] if result['hashtags'] else 'No hashtags found')
print('Currency Amounts:', result['currencies'] if result['currencies'] else 'No currency amounts found')
