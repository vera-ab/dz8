from html import escape

from django.http import HttpResponse, request
from datetime import datetime


def my_whoami(request, font=None):
    browser = str(request.headers.get('User-Agent'))
    ip_address = str(request.META.get('REMOTE_ADDR'))
    server_time = str(datetime.now().strftime('%H:%M:%S'))
    return HttpResponse(
        f"""
       <!DOCTYPE html>
        <html>
        <head>      
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity=
        "sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <title>About page</title>    
        </head>    
            
        <body>
        <div class="container-lg">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="http://127.0.0.1:8000/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://127.0.0.1:8000/about/whoami/">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/about/source_code">Source code</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://127.0.0.1:8000/random/?length=42&specials=1&digits=0">Generate random string</a>
        </li>
        </ul>   
        </div>
       <div class="container-lg">
        <p >
        <h3>Whoami page</h3><br/>
        Your browser: {browser}<br />
        Your ip address:{ip_address}<br />
        Server time:{server_time}
        </p>
        </div>
    </body>
    </html>
    """
    )


def source_code(response):
        with open(__file__, 'r') as f:
            file = f.readlines()
            code = escape("".join(file))
        return HttpResponse(f"""
        <!DOCTYPE html>
        <html>
        <head>      
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity=
        "sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <title>Source code page page</title>    
        </head>    
            
        <body>
        <div class="container-lg">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="http://127.0.0.1:8000/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://127.0.0.1:8000/about/whoami/">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/about/source_code">Source code</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://127.0.0.1:8000/random/?length=42&specials=1&digits=0">Generate random string</a>
        </li>
        </ul>   
        </div>
        <div class="container-lg">
        <p >
        <h3>Source code</h3><br/>
        <pre>{code}</pre>
        </p>
        </div>
    </body>
    </html>
    """)
