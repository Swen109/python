#指派值

letter = '''Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
略{amount}
略略{product}
再略{percent}%{verbed}.

ry

Sincerely,
{spokesman}
{job_title}'''

print(letter.format(salutation = '1', name = '2', product = '3', verbed = '4', room = '5',
    animals = '6', amount = '7', percent = '8', spokesman = '9', job_title = '0'))