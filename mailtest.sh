curl -s --user 'api:key-38472dd41dc2a3b3a50247b5e57afff4' \
    https://api.mailgun.net/v3/mail.it-q.space/messages \
    -F from='Excited User <mailgun@mail.it-q.space>' \
    -F to=polyun@mail.it-q.space \
    -F to=bar@example.com \
    -F subject='Hello Polyun' \
    -F text='Testing some Mailgun awesomness!'