# Accessibility 

## Generate token

Open Git Bash and enter this

      curl 'https://opendata.nationalrail.co.uk/authenticate' \
     --data-urlencode 'username=jonathanpturnbull8788@gmail.com' \
     --data-urlencode 'password=HungryApple13$'

The response will be e.g.

      {"username":"jonathanpturnbull8788@gmail.com","roles":{"ROLE_DARWIN":true,"ROLE_KB_REAL_TIME":true,"ROLE_STANDARD":true,"ROLE_KB_API":true,"ROLE_DTD":true,"ROLE_HSP_USER":true},"token":"jonathanpturnbull8788@gmail.com:1741963003000:VRYBKJFKkh5M1Nn5T9hCVA7dk5f2i54u2bk6QXBlU64="}

