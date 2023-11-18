# Salvador M. Olavarrieta
# Create Custom Messages
# 11/14/2023

def your_function_name(s):
    if s == 'grades':
        info = "We will send you information on getting good grades in school."
    elif s == 'study':
        info = "We will send you information on workshops to build better study habits."
    elif s == 'campus':
        info = "We will send you information about clubs and other campus events that you can attend."
    elif s == 'balance':
        info = "We will send you information about time management, stress management, and finding that work/school balance."
    else:
        info = "We will send you information about current campus events."
    return info

def your_function_name(first_name, last_name, email_address, custom):
    # create a unique file name using first, last, and adding .txt
    # build the message
    message = # add the info and use `\n` for new lines
    message += #
    ...

    # write each file out separately
    ...

    # give the user some output so they know what happened

csvfile = open('newsletter-signup.csv')
signup_reader = ...

for row in signup_reader:
    first_name = row[0]
    last_name = row[1]
    email_address = row[2]
    know_more = row[3]

    # call your function with the attributes
    # remember to also call the function for "know_more"