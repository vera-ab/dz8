from django.http import HttpResponse


def index_view(response):
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
        <title>Main page</title>    
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
        </body>
        </html>
            """
    )
